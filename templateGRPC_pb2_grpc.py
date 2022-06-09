# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import templateGRPC_pb2 as templateGRPC__pb2


class TemplateGRPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TemplateGRPCEndpoint = channel.unary_unary(
                '/TemplateGRPC/TemplateGRPCEndpoint',
                request_serializer=templateGRPC__pb2.TemplateGRPCRequest.SerializeToString,
                response_deserializer=templateGRPC__pb2.TemplateGRPCResponse.FromString,
                )


class TemplateGRPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TemplateGRPCEndpoint(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TemplateGRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TemplateGRPCEndpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.TemplateGRPCEndpoint,
                    request_deserializer=templateGRPC__pb2.TemplateGRPCRequest.FromString,
                    response_serializer=templateGRPC__pb2.TemplateGRPCResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TemplateGRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TemplateGRPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TemplateGRPCEndpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TemplateGRPC/TemplateGRPCEndpoint',
            templateGRPC__pb2.TemplateGRPCRequest.SerializeToString,
            templateGRPC__pb2.TemplateGRPCResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
