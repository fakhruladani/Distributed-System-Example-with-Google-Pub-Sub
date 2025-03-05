import os
import threading
from google.cloud import pubsub_v1

# Setup Google Cloud Credentials
credentials_path = '/PATH/TO/YOU/PRIVATE/JSON/FILE/HERE/myFile.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# Inisialisasi Subscriber
subscriber = pubsub_v1.SubscriberClient()
shipping_subscription_path = 'SUBSCRIPTION_NAME_HERE'

def callback(message):
    shipping_data = message.data.decode('utf-8')
    print(f"[NOTIFICATION] Shipment Delivered: {shipping_data}")
    message.ack()

def subscribe():
    future = subscriber.subscribe(shipping_subscription_path, callback=callback)
    try:
        future.result()
    except Exception as e:
        future.cancel()
        print("Error in notification subscription:", e)

thread = threading.Thread(target=subscribe, daemon=True)
thread.start()

print("Notification Service is running and tracking shipments...")
thread.join()