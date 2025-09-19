## RabbitMQ

## Publishing Options

In RabbitMQ, `publishing options` let a producer control how a message is routed, stored, and delivered. The producer specifies the `exchange` and `routing key` (to decide where the message goes), the `delivery mode` (transient or persistent), the `mandatory flag` (return unroutable messages or drop them), and extra properties like headers, TTL, priority, correlation ID, or reply-to. Combined with `publisher confirms` for reliability, these options ensure you can fine-tune message durability, routing, and metadata handling when sending messages.

- **ContentType**: application/json, application/pdf
- **ContentEncoding**: gzip, compress, deflate
- **Timestamp**: 1640030010
- **appId**: ShopService
- **userId**: Admin21
- **DeliveryMode**: 1 (non-persistent, does not persist to disk), 2 (persist to disk before send to client)
- **Mandatory**: true (return unroutable messages to the sender), false (drop unroutable messages)
- **Expiration**: 10000 (message expiration in milliseconds)


## Code Example
```python
import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange (optional, depends on your setup)
exchange = 'my_exchange'
routing_key = 'my_routing_key'

# Message body
msg = "Hello RabbitMQ"

# Publishing options (properties)
properties = pika.BasicProperties(
    delivery_mode=2,           # make message persistent
    content_type='text/plain', # metadata
    headers={'source': 'python-producer'}
)

# Publish
channel.basic_publish(
    exchange=exchange,
    routing_key=routing_key,
    body=msg.encode('utf-8'),
    properties=properties,
    mandatory=True   # mandatory flag, if the message is unroutable, it will be returned to the sender
)

print(" [x] Sent message")

connection.close()
``` 
