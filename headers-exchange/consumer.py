import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="headersexchange", exchange_type=ExchangeType.headers)
channel.queue_declare(queue="letterbox")

# delete the old queue if its cached:
# rabbitmqctl delete_queue letterbox

# list all bindings for the exchange:
# rabbitmqctl list_bindings | grep headersexchange

# list all queues and their arguments:
# rabbitmqctl list_queues name arguments

# x-match: any or all
bind_args = {
    "x-match": "any",
    "name": "brian",
    "age": "53"
}
# bind the queue to the exchange with arguments
channel.queue_bind(
    exchange="headersexchange",
    queue="letterbox",
    arguments=bind_args
)

channel.basic_consume(
    queue="letterbox",
    auto_ack=True,
    on_message_callback=on_message_received
)

print("Starting Consuming, to exit press CTRL+C")
channel.start_consuming()
