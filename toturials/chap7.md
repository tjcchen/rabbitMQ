# RabbitMQ

## Pub-Sub Pattern

In the pub/sub pattern, multiple consumers subscribe to a topic, and messages are distributed to all subscribers based on the topic.


## How It Works

In the pub/sub pattern:
- Multiple consumers connect to the same queue
- RabbitMQ distributes messages in round-robin fashion
- Each message is processed by only one consumer
- This enables load balancing and parallel processing

## Exchange Type: Fanout

In RabbitMQ, a `fanout exchange` is a type of exchange that broadcasts all messages it receives to all queues bound to it, regardless of the routing key. It's a simple and powerful way to distribute the same message to multiple consumers. Think of it like a public announcement system: when a message is sent to the fanout exchange, every listener (queue) gets a copy.


## Pub/Sub Pattern Diagram

![Pub/Sub Pattern Diagram](../resources/pub-sub.png)
