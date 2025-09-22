import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    # Acknowledge the message when the delivery tag is a multiple of 5
    if (method.delivery_tag % 5 == 0):
        # acknowledge the message
        # ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)
        # reject the message, requeue it to the queue
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True, multiple=True)
    print(f"Received new message: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="acceptrejectexchange", exchange_type=ExchangeType.fanout)

channel.queue_declare(queue="letterbox")
channel.queue_bind(
    queue="letterbox",
    exchange="acceptrejectexchange",
    routing_key="test"
)

channel.basic_consume(
    queue="letterbox",
    auto_ack=False,
    on_message_callback=on_message_received
)

print("Starting Consuming")
channel.start_consuming()
