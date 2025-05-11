import boto3
from botocore.exceptions import ClientError

# Inicializa os clientes do SQS e CloudWatch
sqs = boto3.client('sqs')
cloudwatch = boto3.client('cloudwatch')

# 1. Crie uma fila no SQS
response_queue = sqs.create_queue(
    QueueName='OrderProcessingQueue',
)
queue_url = response_queue['QueueUrl']
queue_arn = sqs.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=['QueueArn']
)['Attributes']['QueueArn']

print(f'Fila criada: {queue_url}')

# 2. Configuração de métrica personalizada no CloudWatch para monitorar a fila
# Métrica: Número de mensagens disponíveis na fila
def put_custom_metric():
    try:
        cloudwatch.put_metric_data(
            Namespace='SQSMonitoring',
            MetricData=[
                {
                    'MetricName': 'MessagesInQueue',
                    'Dimensions': [
                        {'Name': 'QueueName', 'Value': 'OrderProcessingQueue'}
                    ],
                    'Unit': 'Count',
                    'Value': int(sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['ApproximateNumberOfMessages'])['Attributes']['ApproximateNumberOfMessages'])
                }
            ]
        )
        print("Métrica personalizada criada no CloudWatch.")
    except ClientError as e:
        print(f"Erro ao criar a métrica: {e}")

# 3. Configuração de alarmes no CloudWatch
def create_cloudwatch_alarm():
    try:
        cloudwatch.put_metric_alarm(
            AlarmName='HighNumberOfMessagesInQueue',
            MetricName='ApproximateNumberOfMessages',
            Namespace='AWS/SQS',
            Statistic='Average',
            Dimensions=[
                {'Name': 'QueueName', 'Value': 'OrderProcessingQueue'}
            ],
            Period=60,
            EvaluationPeriods=1,
            Threshold=10,  # Alarme se mais de 10 mensagens estiverem na fila
            ComparisonOperator='GreaterThanThreshold',
            AlarmActions=[
                'arn:aws:sns:us-east-1:123456789012:YourSNSTopic'  # Trocar pelo ARN de um tópico SNS
            ]
        )
        print("Alarme criado no CloudWatch.")
    except ClientError as e:
        print(f"Erro ao criar o alarme: {e}")

# 4. Enviar mensagens para a fila
def send_message_to_queue(message_body):
    try:
        sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
        print(f'Mensagem enviada: {message_body}')
    except ClientError as e:
        print(f'Erro ao enviar a mensagem: {e}')

# 5. Receber e processar mensagens da fila
def receive_messages_from_queue():
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
                # Após processar a mensagem, excluí-la da fila
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
                print("Mensagem processada e excluída.")
        else:
            print('Nenhuma mensagem recebida.')
    except ClientError as e:
        print(f'Erro ao receber a mensagem: {e}')

# Enviando algumas mensagens para testar
send_message_to_queue("Pedido #12345")
send_message_to_queue("Pedido #12346")

# Monitorando o número de mensagens na fila (custom metric)
put_custom_metric()

# Recebendo mensagens da fila para simulação
receive_messages_from_queue()

# Criação de alarme para monitorar se o número de mensagens na fila é maior que 10
create_cloudwatch_alarm()
