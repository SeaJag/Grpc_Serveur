Generate protobuf

python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. server.proto

#generation du certificat ssl mettre le domaine sur le quel on travail pour la
connection entre le client et le server

# Install

pip install -r requirements.txt

# Server

python3 server.py

# Client

python3 client.py
