## Generating gRPC files
`pip install grpcio-tools`

`python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ order.proto`