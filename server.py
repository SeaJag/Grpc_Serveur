import grpc
from concurrent import futures
import time
import templateGRPC_pb2
import templateGRPC_pb2_grpc
import os


class TheBestTinder(templateGRPC_pb2_grpc.ApiServicer):

    def ApiEndpoint(self, request, context):
        response = templateGRPC_pb2.ApiResponse()
        response.reply = request.number + 1
        return response


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    with open('ssl/server.key', 'rb') as f:
        private_key = f.read()
    with open('ssl/server.crt', 'rb') as f:
        certificate_chain = f.read()

    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain), ))

    templateGRPC_pb2_grpc.add_ApiServicer_to_server(TheBestTinder(), server)

    # listen on port 50051
    print('Starting server. Listening on port 5000.')
    server.add_secure_port('[::]:5000', server_credentials)
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
