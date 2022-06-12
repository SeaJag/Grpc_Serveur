# gRPC server

Create a gRPC server that implements the x --> x+1 method

"An RPC method that takes a HelloRequest parameter from the client and returns a HelloReply from the server"

## Steps

### Prerequisites

Need ``pip`` and ``python3`` for this project

### Installation

``pip install -r requirements.txt``

### Generate protobuf

``python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. templateGRPC.proto``

### Run Server
``python3 server.py``

### Run Client
``python3 client.py``


# Ressources

https://grpc.github.io/grpc/python/grpc.html#create-client-credentials

https://grpc.io/blog/wireshark/

