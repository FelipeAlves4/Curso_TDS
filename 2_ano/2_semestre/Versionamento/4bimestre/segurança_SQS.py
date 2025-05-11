import boto3
from botocore.exceptions import ClientError

# Inicializa o cliente SQS e KMS
sqs = boto3.client('sqs')
kms = boto3.client('kms')

# 1. Crie uma chave no KMS para uso com a fila do SQS
response_kms = kms.create_key(
    Description='Chave KMS para criptografia de mensagens SQS',
    KeyUsage='ENCRYPT_DECRYPT',
    Origin='AWS_KMS'
)
key_id = response_kms['KeyMetadata']['KeyId']
print(f'Chave KMS criada com ID: {key_id}')

# 2. Crie uma fila SQS com criptografia
response_queue = sqs.create_queue(
    QueueName='SecureFinancialTransactionsQueue',
    Attributes={
        'KmsMasterKeyId': key_id,  # Vincula a chave KMS à fila
        'KmsDataKeyReusePeriodSeconds': '86400'  # Tempo de reutilização da chave de dados
    }
)
queue_url = response_queue['QueueUrl']
print(f'Fila segura criada: {queue_url}')

# 3. Definição de políticas do IAM para restringir o acesso à fila
queue_arn = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['QueueArn'])['Attributes']['QueueArn']
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sqs:SendMessage",
            "Resource": queue_arn,
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "203.0.113.0/24"  # Endereço IP permitido
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sqs:ReceiveMessage",
            "Resource": queue_arn,
            "Condition": {
                "DateGreaterThan": {"aws:CurrentTime": "2024-10-14T09:00:00Z"},  # Permitir acesso após uma data/hora específica
                "DateLessThan": {"aws:CurrentTime": "2024-10-14T17:00:00Z"}     # Limitar o acesso até uma data/hora
            }
        }
    ]
}

# Aplica a política à fila
sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'Policy': str(policy)
    }
)
print('Política de controle de acesso aplicada à fila.')

# 4. Função para enviar mensagem criptografada
def send_encrypted_message(queue_url, message_body):
    try:
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        print(f'Mensagem enviada: {message_body}')
    except ClientError as e:
        print(f'Erro ao enviar mensagem: {e}')

# 5. Função para receber a mensagem criptografada
def receive_encrypted_message(queue_url):
    try:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10
        )
        messages = response.get('Messages', [])
        if messages:
            for message in messages:
                print(f'Mensagem recebida: {message["Body"]}')
                # Excluir a mensagem após recebimento
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
        else:
            print('Nenhuma mensagem recebida.')
    except ClientError as e:
        print(f'Erro ao receber mensagem: {e}')

# Enviando uma mensagem criptografada
send_encrypted_message(queue_url, "Transação financeira #12345")

# Recebendo a mensagem criptografada
receive_encrypted_message(queue_url)

# 6. Limpeza: apague a fila e a chave KMS
sqs.delete_queue(QueueUrl=queue_url)
kms.schedule_key_deletion(KeyId=key_id, PendingWindowInDays=7)
print('Fila e chave KMS agendadas para exclusão.')
