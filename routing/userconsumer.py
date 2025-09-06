import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"Users Service - received new message: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# exchange type: ExchangeType.direct, ExchangeType.topic
channel.exchange_declare(exchange="mytopicexchange", exchange_type=ExchangeType.topic)
queue = channel.queue_declare(queue="", exclusive=True)

# binding key: user.# - this will match any routing key that starts with user.
channel.queue_bind(
    exchange="mytopicexchange",
    queue=queue.method.queue,
    routing_key="user.#"
)

channel.basic_consume(
    queue=queue.method.queue,
    auto_ack=True,
    on_message_callback=on_message_received
)

print("Starting consuming, to exit press CTRL+C")
channel.start_consuming()
