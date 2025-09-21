#
# Alternate Exchange
# The Alternate Exchange (AE) in RabbitMQ is a fallback mechanism. It ensures that if a message cannot be routed by the original exchange (because no queue matches the routing key), the message won’t just vanish — it gets sent to another exchange you designate as the alternate.
# Useful for logging, monitoring, auditing, or fallback handling
#

import pika
from pika.exchange_type import ExchangeType

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

message = "Hello this is my first message"

# important
# eg: update routing key to 'simple' to make it fail
channel.basic_publish(
    exchange="mainexchange",
    routing_key="simple",
    body=message
)

print(f"Sent message: {message}")
connection.close()
