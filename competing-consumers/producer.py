import pika
import time
import random

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue="letterbox")

message_id = 1

while(True):
    message = f"Sending messageId: {message_id}"
    processing_time = random.randint(1, 4)

    channel.basic_publish(exchange="", routing_key="letterbox", body=message)
    print(f"sent message: {message}")

    time.sleep(processing_time)
    message_id += 1

# keep the connection open at the moment
# connection.close()
