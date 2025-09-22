#
# Accept and Reject Messages
# In RabbitMQ, once a consumer receives a message from a queue, it must decide what to do with it.
# The two key actions are accept (acknowledge) and reject (nack/reject).
#
# Typical Use:
# - Accept: after successful processing.
# - Reject/Nack with requeue=true: temporary failure (try again later).
# - Reject/Nack with requeue=false: permanent failure (e.g., bad data) → send to Dead Letter Queue.
#

import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(
    exchange="acceptrejectexchange",
    exchange_type=ExchangeType.fanout
)

message = "Let's send this message"

while True:
    channel.basic_publish(
        exchange="acceptrejectexchange",
        routing_key="test",
        body=message
    )
    print(f"Sent message: {message}")
    input("Press any key to continue...")


# Temporary comment out the following line to keep the connection open
# connection.close()
