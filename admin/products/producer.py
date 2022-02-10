#amqps://pareugzs:yj54Z-04mze4PNQ7ym8k4c5gf6vAF1Dw@puffin.rmq2.cloudamqp.com/pareugzs
import pika, json

params = pika.URLParameters('amqps://pareugzs:yj54Z-04mze4PNQ7ym8k4c5gf6vAF1Dw@puffin.rmq2.cloudamqp.com/pareugzs')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

