import os
import threading
import time
from google.cloud import pubsub_v1

credentials_path = '/PATH/TO/YOU/PRIVATE/JSON/FILE/HERE/myFile.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

shipping_subscription_path = 'SUBSCRIPTION_NAME_HERE'
notification_topic_path = 'TOPIC_NAME_HERE'

def callback(message):
    shipping_data = message.data.decode('utf-8')
    print(f"Received package for shipping: {shipping_data}")
    message.ack() 
    
    print("Processing shipping...")
    time.sleep(3)
    
    print("Forwarding shipping status to Notification Service...")
    future = publisher.publish(notification_topic_path, shipping_data.encode('utf-8'))
    future.result()
    print("Shipping status forwarded successfully.")

def subscribe():
    future = subscriber.subscribe(shipping_subscription_path, callback=callback)
    try:
        future.result()
    except Exception as e:
        future.cancel()
        print("Error in shipping subscription:", e)

thread = threading.Thread(target=subscribe, daemon=True)
thread.start()

print("Shipping Service is running and listening for shipments...")
thread.join()