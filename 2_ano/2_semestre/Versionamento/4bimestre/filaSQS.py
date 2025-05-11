import boto3
from botocore.exceptions import NoCredentialsError

#definindo o SQS
sqs = boto3.client('sq')

#criando uma fila padrão 

response_standard = sqs.create_queue(QueueName='StandardQueue')
standard_queue_url = response_standard['QueueUrl']
print(f'Fila padrão criada: {standard_queue_url}')

# Cria uma fila FIFO
response_fifo = sqs.create_queue(
    QueueName='FifoQueue.fifo',
    Attributes={
        'FifoQueue': 'true',
        'ContentBasedDeduplication': 'true'
    }
)
fifo_queue_url = response_fifo['QueueUrl']
print(f'Fila FIFO criada: {fifo_queue_url}')

# Função para enviar mensagens
def send_messages(queue_url, messages, fifo=False):
    for i, msg in enumerate(messages):
        message_attributes = {
            'Id': str(i),
            'MessageBody': msg
        }

        if fifo:
            sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=msg,
                MessageGroupId="default"
            )
        else:
            sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=msg
            )
        print(f'Mensagem enviada: {msg}')

# Enviando mensagens para a fila padrão
messages = ["Pedido 1", "Pedido 2", "Pedido 3"]
send_messages(standard_queue_url, messages)

# Enviando mensagens para a fila FIFO
send_messages(fifo_queue_url, messages, fifo=True)

# Função para receber mensagens
def receive_messages(queue_url, fifo=False):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=2
    )
    messages = response.get('Messages', [])
    for message in messages:
        print(f'Mensagem recebida: {message["Body"]}')
        # Exclui a mensagem após o recebimento
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])

# Recebendo mensagens da fila padrão
print("Recebendo mensagens da fila padrão:")
receive_messages(standard_queue_url)

# Recebendo mensagens da fila FIFO
print("Recebendo mensagens da fila FIFO:")
receive_messages(fifo_queue_url)

# Limpeza: Apaga as filas
sqs.delete_queue(QueueUrl=standard_queue_url)
sqs.delete_queue(QueueUrl=fifo_queue_url)
print('Filas apagadas para limpeza.')
