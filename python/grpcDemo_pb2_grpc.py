# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpcDemo_pb2 as grpcDemo__pb2


class grpcBackendStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.returnValue = channel.unary_unary(
        '/grpcBackend/returnValue',
        request_serializer=grpcDemo__pb2.grpcMessage.SerializeToString,
        response_deserializer=grpcDemo__pb2.grpcMessage.FromString,
        )


class grpcBackendServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def returnValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_grpcBackendServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'returnValue': grpc.unary_unary_rpc_method_handler(
          servicer.returnValue,
          request_deserializer=grpcDemo__pb2.grpcMessage.FromString,
          response_serializer=grpcDemo__pb2.grpcMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpcBackend', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))