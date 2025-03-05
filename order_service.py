import os
import threading
import time
from google.cloud import pubsub_v1

credentials_path = '/PATH/TO/YOU/PRIVATE/JSON/FILE/HERE/myFile.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

order_subscription_path = 'SUBSCRIPTION_NAME_HERE'
packaging_topic_path = 'TOPIC_NAME_HERE'

def callback(message):
    order_data = message.data.decode('utf-8')
    print(f"Received order: {order_data}")
    message.ack()
    print("Forwarding order to Packaging Service...")
    future = publisher.publish(packaging_topic_path, order_data.encode('utf-8'))
    future.result()
    print("Order forwarded successfully.")

def subscribe():
    future = subscriber.subscribe(order_subscription_path, callback=callback)
    try:
        future.result()
    except Exception as e:
        future.cancel()
        print("Error in order subscription:", e)

thread = threading.Thread(target=subscribe, daemon=True)
thread.start()

print("Order Service is running and listening for orders...")
thread.join()