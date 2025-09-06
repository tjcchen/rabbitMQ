import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# exchange type: ExchangeType.direct, ExchangeType.topic
channel.exchange_declare(exchange="mytopicexchange", exchange_type=ExchangeType.topic)

user_payments_message = "A european user paid for the product"

# routing key: user.payments, user.europe.log, user.europe.payments, business.europe.order
channel.basic_publish(
    exchange="mytopicexchange",
    routing_key="user.europe.payments",
    body=user_payments_message
)

business_order_message = "A european business ordered goods"

channel.basic_publish(
    exchange="mytopicexchange",
    routing_key="business.europe.order",
    body=business_order_message
)

print(f"sent message: {user_payments_message}")
print(f"sent message: {business_order_message}")
connection.close()
