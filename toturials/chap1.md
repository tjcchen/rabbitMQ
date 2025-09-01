# RabbitMQ 

## What is RabbitMQ?

RabbitMQ is a distrubted message broker, which implements the Advanced Message Queuing Protocol (AMQP). It is used to decouple applications and services by enabling asynchronous communication through message passing.

## The size of RabbitMQ

RabbitMQ is a software that runs on a server, and it can be installed on a single machine or on multiple machines to form a cluster. Single application size is less than 4MB. RabbitMQ has rich features and plugin systems.


## Local Installation and Development

Debug host: http://localhost:15672


## Why use RabbitMQ?

1. In a distributed system, services often depend on each other. If Service A calls Service B directly and B is slow or down, A gets stuck or fails. A and B no longer need to be online at the same time.

- A publishes a message to RabbitMQ.

- RabbitMQ stores it safely.

- B consumes it whenever it’s ready.


2. RabbitMQ works as an Asynchronous Communication. Synchronous API calls (REST, gRPC) make the caller wait for a response, causing latency and wasted resources.

- RabbitMQ allows fire-and-forget messaging:

- A sends a task (e.g., "resize image") to a queue.

- B processes it in the background.

- System feels faster for users, and workloads can be processed in parallel.


3. RabbitMQ support Reliable Message Delivery - Messages can be lost if the network or consumer crashes.

- Durable queues & persistent messages (survive broker restarts).

- Acknowledgments (ACK/NACK) — messages are only removed after successful processing.

4. Load Balancing / Work Distribution

- Multiple consumers need to process jobs without duplicating work.

- RabbitMQ can distribute tasks evenly across multiple workers.


## RabbitMQ website

url: https://www.rabbitmq.com/