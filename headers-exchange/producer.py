import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare a Headers Exchange
channel.exchange_declare(exchange="headersexchange", exchange_type=ExchangeType.headers)

message = "This message will be sent with headers exchange"

# send header message with properties
# headers: {"name": "brian"}
channel.basic_publish(
    exchange="headersexchange",
    routing_key="",
    body=message,
    properties=pika.BasicProperties(headers={"name": "brian"})
)

print(f"Sent message: {message}")
connection.close()
