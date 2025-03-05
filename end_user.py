import os
from google.cloud import pubsub_v1

# Setup Google Cloud Credentials
credentials_path = '/PATH/TO/YOU/PRIVATE/JSON/FILE/HERE/myFile.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# Initialize Publisher
publisher = pubsub_v1.PublisherClient()
topic_path = 'TOPIC_NAME_HERE'

# Simulate Order Placement
order_data = "Order ID: 10202, Item: Drawing Book, Quantity: 1"
data = order_data.encode('utf-8')

# Publish Order to Order Service
future = publisher.publish(topic_path, data)
print(f"End-user placed an order. Message ID: {future.result()}")
