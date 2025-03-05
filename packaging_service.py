import os
import threading
import time
from google.cloud import pubsub_v1

credentials_path = '/PATH/TO/YOU/PRIVATE/JSON/FILE/HERE/myFile.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

packaging_subscription_path = 'SUBSCRIPTION_NAME_HERE'
shipping_topic_path = 'TOPIC_NAME_HERE'

def callback(message):
    package_data = message.data.decode('utf-8')
    print(f"Received package order: {package_data}")
    message.ack() 
    
    print("Processing packaging...")
    time.sleep(2) 
    
    print("Forwarding package to Shipping Service...")
    future = publisher.publish(shipping_topic_path, package_data.encode('utf-8'))
    future.result()
    print("Package forwarded successfully.")

def subscribe():
    future = subscriber.subscribe(packaging_subscription_path, callback=callback)
    try:
        future.result()
    except Exception as e:
        future.cancel()
        print("Error in packaging subscription:", e)

thread = threading.Thread(target=subscribe, daemon=True)
thread.start()

print("Packaging Service is running and listening for packages...")
thread.join()
