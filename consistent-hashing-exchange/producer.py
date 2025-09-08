
# The primary use case for the x-consistent-hash exchange is to
# ensure that messages with the same routing key are always
# delivered to the same queue.
# This is crucial for maintaining message order and state for a specific entity.
# 
# Use Cases:
# 1. Maintaining Causal Order
# 2. Stateful Processing
# 3. Load Balancing with Affinity
# 
# Instead of a typical routing key match, the x-consistent-hash exchange
# uses the message's routing key to calculate a hash value.
# This hash value determines which queue on a conceptual "hash ring"
# the message will be delivered to.
# Queues are also placed on this ring, and messages are sent to the
# next available queue on the ring. The consistency of this
# process ensures that the same routing key will always hash
# to the same position, and therefore the same queue.

import pika

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare a Consistent Hashing Exchange
channel.exchange_declare(exchange="simplehashing", exchange_type="x-consistent-hash")

routing_key = "Hash ae89d3bs84d8ss39e9 me!"
message = "This is the core message"

# send message with routing key
channel.basic_publish(
    exchange="simplehashing",
    routing_key=routing_key,
    body=message
)

print(f"Sent message: {message}")
connection.close()
