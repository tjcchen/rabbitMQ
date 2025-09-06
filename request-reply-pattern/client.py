# reconstruct from basic producer code
import pika
import uuid

# callback function
def on_reply_message_received(ch, method, properties, body):
    print(f"Reply received: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# declare a temporary queue for replies
reply_queue = channel.queue_declare(queue="", exclusive=True)
channel.basic_consume(
    queue=reply_queue.method.queue,
    auto_ack=True,
    on_message_callback=on_reply_message_received
)

cor_id = str(uuid.uuid4())
print(f"Sending request: {cor_id}")

# send a request message
message = "Can I request a reply?"
channel.queue_declare(queue="request-queue")
channel.basic_publish(
    exchange="",
    routing_key="request-queue",
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ),
    body=message
)

print(f"Starting Client")
channel.start_consuming()
