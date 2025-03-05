# Distributed System Example with Google Pub/Sub

This project demonstrates the implementation of a distributed system using Google Cloud Pub/Sub to simulate an online shopping process. The system consists of multiple services that communicate asynchronously using Pub/Sub messaging.

## Architecture
The system includes the following microservices:

1. **End User Service** (`end_user.py`): Simulates a customer placing an order.
2. **Order Service** (`order_service.py`): Receives orders and forwards them to the Packaging Service.
3. **Packaging Service** (`packaging_service.py`): Processes packaging and sends the order to the Shipping Service.
4. **Shipping Service** (`shipping_service.py`): Handles shipping and sends a delivery notification.
5. **Notification Service** (`notification.py`): Notifies the end user when the order is delivered.

Each service operates independently and communicates using Google Cloud Pub/Sub.

## Prerequisites

1. A Google Cloud account with Pub/Sub enabled.
2. A service account with Pub/Sub permissions.
3. Python 3 installed on your system.
4. Google Cloud SDK installed and configured.

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/Distributed-System-Example-with-Google-Pub-Sub.git
   cd Distributed-System-Example-with-Google-Pub-Sub
   ```

2. **Install Dependencies**
   ```bash
   pip install google-cloud-pubsub
   ```

3. **Set Up Google Cloud Credentials**
   - Download the service account JSON key file.
   - Update the following line in each script to the correct path:
     ```python
     credentials_path = '/PATH/TO/YOUR/PRIVATE/JSON/FILE/myFile.privateKey.json'
     ```

4. **Create Topics and Subscriptions in Google Cloud Pub/Sub**
   ```bash
   gcloud pubsub topics create order-topic
   gcloud pubsub topics create packaging-topic
   gcloud pubsub topics create shipping-topic
   gcloud pubsub topics create notification-topic

   gcloud pubsub subscriptions create order-subscription --topic=order-topic
   gcloud pubsub subscriptions create packaging-subscription --topic=packaging-topic
   gcloud pubsub subscriptions create shipping-subscription --topic=shipping-topic
   gcloud pubsub subscriptions create notification-subscription --topic=notification-topic
   ```

5. **Update Pub/Sub Topic and Subscription Names**
   Replace `'TOPIC_NAME_HERE'` and `'SUBSCRIPTION_NAME_HERE'` in each script with the actual topic and subscription names you created.

## Running the Services

Each service should be run in a separate terminal window:

1. **Start the Notification Service**
   ```bash
   python notification.py
   ```
2. **Start the Shipping Service**
   ```bash
   python shipping_service.py
   ```
3. **Start the Packaging Service**
   ```bash
   python packaging_service.py
   ```
4. **Start the Order Service**
   ```bash
   python order_service.py
   ```
5. **Simulate an End User Placing an Order**
   ```bash
   python end_user.py
   ```

## Workflow
1. The **End User** places an order, which is published to `order-topic`.
2. The **Order Service** receives the order and forwards it to the `packaging-topic`.
3. The **Packaging Service** processes the packaging and sends it to `shipping-topic`.
4. The **Shipping Service** handles the shipping and notifies the **Notification Service**.
5. The **Notification Service** receives the shipping status and prints a delivery message.

## Example Output

```bash
End-user placed an order. Message ID: 12345
Received order: Order ID: 10202, Item: Drawing Book, Quantity: 1
Forwarding order to Packaging Service...
Received package order: Order ID: 10202, Item: Drawing Book, Quantity: 1
Processing packaging...
Forwarding package to Shipping Service...
Received package for shipping: Order ID: 10202, Item: Drawing Book, Quantity: 1
Processing shipping...
Forwarding shipping status to Notification Service...
[NOTIFICATION] Shipment Delivered: Order ID: 10202, Item: Drawing Book, Quantity: 1
```

## Conclusion
This example demonstrates how to implement a distributed system using Google Pub/Sub for event-driven communication. Each service runs independently, ensuring scalability and decoupling of processes.

## License
This project is open-source and free to use.

