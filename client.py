import grpc
import templateGRPC_pb2_grpc
import templateGRPC_pb2
import time


def main():
    request = templateGRPC_pb2.ApiRequest(
        number=4)

    response = stub.ApiEndpoint(request)
    print(response)


if __name__ == '__main__':
    with open('ssl/server.crt', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
    channel = grpc.secure_channel('localhost:5000', creds)
    stub = templateGRPC_pb2_grpc.ApiStub(channel)
    while True:
        main()
        time.sleep(2)
