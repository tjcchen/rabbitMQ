import pika
from pika.exchange_type import ExchangeType

def dlx_queue_on_message_received(ch, method, properties, body):
    print(f"DLX: received new message: {body}")

def main_queue_on_message_received(ch, method, properties, body):
    print(f"Main: received new message: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="mainexchange", exchange_type=ExchangeType.direct)
channel.exchange_declare(
    exchange="dlx",
    exchange_type=ExchangeType.fanout
)

# Declare the main exchange queue
channel.queue_declare(
    queue="mainexchangequeue",
    arguments={'x-dead-letter-exchange': 'dlx', 'x-message-ttl': 1000} # 1s to expire
)
channel.queue_bind(
    queue="mainexchangequeue",
    exchange="mainexchange",
    routing_key="test"
)

# Declare the dlx queue
channel.queue_declare(queue="dlxqueue")
channel.queue_bind(queue="dlxqueue", exchange="dlx")

channel.basic_consume(
    queue="mainexchangequeue",
    auto_ack=True,
    on_message_callback=main_queue_on_message_received
)

channel.basic_consume(
    queue="dlxqueue",
    auto_ack=True,
    on_message_callback=dlx_queue_on_message_received
)

print("Starting Consuming")
channel.start_consuming()
