import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = order_pb2.OrderMessage(
    id="2222",
    created_by="USER123",
    status=order_pb2.OrderMessage.Status.QUEUED,
    created_at='2020-03-12',
    equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
)


response = stub.Create(order)
