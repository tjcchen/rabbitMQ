import pika
from pika.exchange_type import ExchangeType

def on_message1_received(ch, method, properties, body):
    print(f"queue 1 received new message: {body}")

def on_message2_received(ch, method, properties, body):
    print(f"queue 2 received new message: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="simplehashing", exchange_type="x-consistent-hash")

# declare two queues
channel.queue_declare(queue="letterbox1")
channel.queue_declare(queue="letterbox2")

# bind the queues to the exchange with routing key
channel.queue_bind(
    exchange="simplehashing",
    queue="letterbox1",
    routing_key="1"
)
channel.queue_bind(
    exchange="simplehashing",
    queue="letterbox2",
    routing_key="4"
)

# consume the queues
channel.basic_consume(
    queue="letterbox1",
    auto_ack=True,
    on_message_callback=on_message1_received
)
channel.basic_consume(
    queue="letterbox2",
    auto_ack=True,
    on_message_callback=on_message2_received
)

print("Starting Consuming, to exit press CTRL+C")
channel.start_consuming()
