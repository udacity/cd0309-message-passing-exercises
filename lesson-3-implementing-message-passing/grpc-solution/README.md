## Generating gRPC files
### Create a new virtual environment
`python3 -m venv venv`

### Activate the environment
`source venv/bin/activate`

`pip install grpcio-tools`

`python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ order.proto`