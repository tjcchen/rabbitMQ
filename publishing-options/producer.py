import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# 1. Enables publish confirms
channel.confirm_delivery()
# 1. Enables Transactions
channel.tx_select()

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

# Create a durable queue that survives restarts
channel.queue_declare(queue="Test", durable=True)

message = "Hello I want to broadcast this message"

channel.basic_publish(
    exchange="pubsub",
    routing_key="",
    properties=pika.BasicProperties(
        headers={ "name": "Andy" },
        delivery_mode=2,           # 2 = persistent， 1 = transient
        expiration=13443434,
        content_type="application/json",
    ),
    body=message,
    # Set the publish to be mandatory - eg: receive a notification if the message is failed
    mandatory=True
)

# 2. Commit a transaction
channel.tx_commit()
# 2. Rollback a transaction
channel.tx_rollback()

print(f"Sent message: {message}")
connection.close()
