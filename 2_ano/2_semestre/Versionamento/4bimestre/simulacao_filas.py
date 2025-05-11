import time
import random
import pika  # RabbitMQ
import boto3  # Amazon SQS
from confluent_kafka import Producer, Consumer, KafkaException  # Apache Kafka

# Simulando a geração de mensagens
# Simulando o envio de mensagens
# Simulando o recebimento de mensagens
# Simulando um loop de mensageria para RabbitMQ, SQS e Kafka
# Executando a simulação para cada sistema

def rabbitmq_setup():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='order_queue')
    return channel

def sqs_setup():
    sqs = boto3.client('sqs', region_name='us-east-1')
    queue_url = sqs.create_queue(QueueName='OrderQueue')['QueueUrl']
    return sqs, queue_url

def kafka_setup():
    producer_config = {'bootstrap.servers': 'localhost:9092'}
    consumer_config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'order_group',
        'auto.offset.reset': 'earliest'
    }
    producer = Producer(producer_config)
    consumer = Consumer(consumer_config)
    return producer, consumer

def send_rabbitmq_message(channel, message):
    channel.basic_publish(exchange='', routing_key='order_queue', body=message)
    print(f"RabbitMQ: Enviado {message}")

def send_sqs_message(sqs, queue_url, message):
    sqs.send_message(QueueUrl=queue_url, MessageBody=message)
    print(f"SQS: Enviado {message}")

def send_kafka_message(producer, topic, message):
    producer.produce(topic, message.encode('utf-8'))
    producer.flush()
    print(f"Kafka: Enviado {message}")

def receive_rabbitmq_message(channel):
    def callback(ch, method, properties, body):
        print(f"RabbitMQ: Recebido {body.decode('utf-8')}")
    channel.basic_consume(queue='order_queue', on_message_callback=callback, auto_ack=True)
    print('RabbitMQ: Aguardando mensagens...')
    channel.start_consuming()

def receive_sqs_message(sqs, queue_url):
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    messages = response.get('Messages', [])
    if messages:
        message = messages[0]
        print(f"SQS: Recebido {message['Body']}")
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])

def receive_kafka_message(consumer, topic):
    consumer.subscribe([topic])
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        print(f"Kafka: Recebido {msg.value().decode('utf-8')}")
def simulate_messaging():
    # RabbitMQ setup
    rabbit_channel = rabbitmq_setup()

    # SQS setup
    sqs, sqs_queue_url = sqs_setup()

    # Kafka setup
    kafka_producer, kafka_consumer = kafka_setup()

    # Simulação de envio de mensagens
    messages = ["Pedido Criado", "Pagamento Processado", "Pedido Enviado", "Pedido Entregue"]

    for message in messages:
        # Enviando mensagens para RabbitMQ
        send_rabbitmq_message(rabbit_channel, message)

        # Enviando mensagens para SQS
        send_sqs_message(sqs, sqs_queue_url, message)

        # Enviando mensagens para Kafka
        send_kafka_message(kafka_producer, 'order_topic', message)

        time.sleep(random.uniform(0.5, 1.5))

    # Recebendo mensagens de RabbitMQ
    print("\nRecebendo mensagens de RabbitMQ:")
    receive_rabbitmq_message(rabbit_channel)

    # Recebendo mensagens de SQS
    print("\nRecebendo mensagens de SQS:")
    receive_sqs_message(sqs, sqs_queue_url)

    # Recebendo mensagens de Kafka
    print("\nRecebendo mensagens de Kafka:")
    receive_kafka_message(kafka_consumer, 'order_topic')

simulate_messaging()
