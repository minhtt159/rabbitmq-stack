import pika
from pika import spec

RMQ_HOST = "IP_ADDRESS"
RMQ_PORT = 5672

RMQ_USER = "guest"
RMQ_PASS = "guest"

EXCHANGE = "test-exchange"
ROUTING  = "test"
QUEUE    = "test-queue"

MSG = "Hello World!"

# channel: BlockingChannel
# method: spec.Basic.Deliver
# properties: spec.BasicProperties
# body: bytes
# def consumer_callback(ch: any,
#                     method: spec.Basic.Deliver,
#                     properies: spec.BasicProperties,
#                     body: bytes):
#     print(f"[+] Received {body}")

if __name__ == "__main__":
    # Create connection to RabbitMQ
    conn_creds = pika.PlainCredentials(username = RMQ_USER,
                                    password = RMQ_PASS)
    conn_params = pika.ConnectionParameters(host = RMQ_HOST,
                                            port = RMQ_PORT,
                                            credentials = conn_creds)
    connection = pika.BlockingConnection(parameters = conn_params)
    channel = connection.channel()
    channel.queue_declare(queue = QUEUE, durable = True)

    # Send message to the queue
    channel.basic_publish(exchange = EXCHANGE, routing_key = ROUTING, body = MSG)
    print(f"[-] Sent {MSG} to {EXCHANGE} with key {ROUTING}")

    # Consume message from queue
    method_frame, header_frame, body = channel.basic_get(queue = QUEUE, auto_ack = True)
    if method_frame == None:
        print(f"[+] Channel {QUEUE} is empty")
    else:
        print(f"[+] Received: {body}")