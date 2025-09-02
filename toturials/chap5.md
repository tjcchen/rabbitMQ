# RabbitMQ 

## AMQP (Advanced Message Queuing Protocol)

AMQP is a protocol that RabbitMQ implements. It defines a set of rules for how messages are sent and received. Not just RabbitMQ, but other message brokers also implement AMQP, such as Apache ActiveMQ, Azure Service Bus, and ZeroMQ.

AMQP uses a binary protocol to communicate between clients and servers. It uses a Remote Procedure Call (RPC) pattern to exchange messages.

## AMQP Frames

AMQP (Advanced Message Queuing Protocol) is the wire-level protocol RabbitMQ uses. When your app talks to RabbitMQ over a connection, all communication is broken into `frames` — think of them like packets in a conversation.

A frame is the smallest unit of communication on an AMQP connection. Each frame contains: Frame header, Payload, Frame end marker.

```bash
# Types of AMQP Frames
- Method Frame: Carries AMQP commands (e.g., basic.publish, queue.declare, basic.ack).
- Header Frame: Contains message properties (content-type, delivery-mode, etc.) and body size.
- Body Frame: Carries the actual message payload (can be split into multiple body frames).
- Heartbeat Frame: Lightweight frame used to keep the connection alive and detect dead peers.
- Protocol Header: Sent at the very beginning to establish AMQP version compatibility.
```


## AMQP website

url: https://www.amqp.org/about/what


## AMQP resources

docs: [AMQP specification](../resources/amqp0-9-1.pdf)