import pika
import time
import random

def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"received: {body}, will take {processing_time} to process")

    time.sleep(processing_time)
    print(f"finished processing: {body}")
    # manual acknowledgment
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing the message")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue="letterbox")

# qos = quality of service
# prefetch_count=1 ensures that only one message is processed at a times
# auto_ack=False ensures that the message is not acknowledged automatically
channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue="letterbox",
    auto_ack=False,
    on_message_callback=on_message_received
)

print("Starting consuming, to exit press CTRL+C")
channel.start_consuming()
