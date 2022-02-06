#amqps://pareugzs:yj54Z-04mze4PNQ7ym8k4c5gf6vAF1Dw@puffin.rmq2.cloudamqp.com/pareugzs
from django.db import connection
import pika

params = pika.URLParameters('amqps://pareugzs:yj54Z-04mze4PNQ7ym8k4c5gf6vAF1Dw@puffin.rmq2.cloudamqp.com/pareugzs')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()