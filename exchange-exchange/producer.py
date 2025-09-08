# Exchange-to-exchange routing in RabbitMQ allows you to build complex message
# routing topologies by binding exchanges to other exchanges.
# This creates a powerful, multi-stage pipeline where messages can be filtered and transformed as they travel through a series of exchanges.
# 
# Use Cases: 
# 1. Chained Processing and Workflows
# 2. Multicast Routing
# 3. Auditing and Logging
# 4. Flexible Load Balancing and Scaling

import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="firstexchange", exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange="secondexchange", exchange_type=ExchangeType.fanout)

channel.exchange_bind(
    destination="secondexchange",
    source="firstexchange"
)

message = "This message has gone through multiple exchanges"
channel.basic_publish(
    exchange="firstexchange",
    routing_key="",
    body=message
)

print(f"Sent message: {message}")
connection.close()
