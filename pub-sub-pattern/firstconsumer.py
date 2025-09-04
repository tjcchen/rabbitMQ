import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"firstconsumer - received new message: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare an Fanout Exchange
channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

# give a random name to the queue
# when the connection is closed, the queue will be deleted
queue = channel.queue_declare(queue="", exclusive=True)

# this is most important step
# bind the queue to the exchange, `queue.method.queue` is the random name of the queue
channel.queue_bind(exchange="pubsub", queue=queue.method.queue)

channel.basic_consume(
    queue=queue.method.queue,
    on_message_callback=on_message_received,
    auto_ack=True
)

print("Starting consuming, to exit press CTRL+C")
channel.start_consuming()
