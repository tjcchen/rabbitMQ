import pika
from pika.exchange_type import ExchangeType

def alt_queue_on_message_received(ch, method, properties, body):
    print(f"Alt: received new message: {body}")

def main_queue_on_message_received(ch, method, properties, body):
    print(f"Main: received new message: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="altexchange", exchange_type=ExchangeType.fanout)
# Specify the alternate exchange, namely altexchange, for mainexchange
channel.exchange_declare(
    exchange="mainexchange",
    exchange_type=ExchangeType.direct,
    arguments={
        "alternate-exchange": "altexchange"
    }
)

# Declare the alt exchange queue, and bind it to altexchange
channel.queue_declare(queue="altexchangequeue")
channel.queue_bind(
    queue="altexchangequeue",
    exchange="altexchange"
)

# Declare the main exchange queue, and bind it to mainexchange
channel.queue_declare(queue="mainexchangequeue")
channel.queue_bind(
    queue="mainexchangequeue",
    exchange="mainexchange",
    routing_key="test"
)

channel.basic_consume(
    queue="altexchangequeue",
    auto_ack=True,
    on_message_callback=alt_queue_on_message_received
)

channel.basic_consume(
    queue="mainexchangequeue",
    auto_ack=True,
    on_message_callback=main_queue_on_message_received
)

print("Starting Consuming")
channel.start_consuming()
