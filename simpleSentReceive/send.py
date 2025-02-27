import pika
import os
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")

print("Enter the message (type 'exit' to quit): ")

while True:
    try:
        message = input("> ")
        if message.lower() == "exit":
            print("You chose to exit")
            break

        channel.basic_publish(exchange="", routing_key="hello", body=message)
        print(f" [x] Sent  '{message}' ")
    except KeyboardInterrupt:
        print("\nInterrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

connection.close()
