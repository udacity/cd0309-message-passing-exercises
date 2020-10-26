import json
from .app import g
from .enums import Status


def create_order(order_data):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(order_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("items", kafka_data)


def retrieve_orders():
    """
    This is a stubbed method of retrieving multiple resources. It doesn't actually do anything.
    """
    return [
        {
            "id": "1",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:31:10.969696",
            "created_by": "USER14",
            "equipment": [
                "KEYBOARD", "MOUSE"
            ]
        },
        {
            "id": "2",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:29:10.969696",
            "created_by": "USER15",
            "equipment": [
                "KEYBOARD", "WEBCAM"
            ]
        }
    ]
