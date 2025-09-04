import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare an Fanout Exchange
channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

message = "Hello I want to broadcast this message"

# in a pub-sub pattern, we need to keep exchange same as the exchange we declared
# in this case, it is "pubsub"
channel.basic_publish(exchange="pubsub", routing_key="", body=message)

print(f"sent message: {message}")
connection.close()
