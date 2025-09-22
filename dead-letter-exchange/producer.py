#
# A Dead Letter Exchange is an exchange to which RabbitMQ automatically re-publishes “dead” messages.
# A message is considered dead when it can’t be delivered inside a queue (not at the exchange level).
# 
# Use cases:
# Retry mechanism - process messages again later
# Error handling - store problematic messages for manual review
# Audit - keep track of failed/expired messages without losing them
#

import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="mainexchange", exchange_type=ExchangeType.direct)

message = "This message will expire..."

channel.basic_publish(
    exchange="mainexchange",
    routing_key="test",
    body=message
)

print(f"Sent message: {message}")
connection.close()
