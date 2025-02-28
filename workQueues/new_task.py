import pika
import sys
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

# message = " ".join(sys.argv[1:]) or "Hello World" # with argv
print("Enter the message (type 'exit' to quit):")

while True:  # with constant input from the user
    try:
        message = input("> ")
        if message.lower() == "exit":
            print("You chose to exit")
            break
        channel.basic_publish(
            exchange="",
            routing_key="task_queue",
            body=message,
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        print(f" [x] Sent '{message}'")
    except KeyboardInterrupt:
        print("\nInterrupeted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

connection.close()
