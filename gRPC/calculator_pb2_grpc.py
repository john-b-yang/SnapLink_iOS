# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SquareRoot = channel.unary_unary(
        '/Calculator/SquareRoot',
        request_serializer=calculator__pb2.Number.SerializeToString,
        response_deserializer=calculator__pb2.Number.FromString,
        )
    self.Squared = channel.unary_unary(
        '/Calculator/Squared',
        request_serializer=calculator__pb2.Number.SerializeToString,
        response_deserializer=calculator__pb2.Number.FromString,
        )
    self.Factorial = channel.unary_unary(
        '/Calculator/Factorial',
        request_serializer=calculator__pb2.Number.SerializeToString,
        response_deserializer=calculator__pb2.Number.FromString,
        )
    self.RotateImage = channel.unary_unary(
        '/Calculator/RotateImage',
        request_serializer=calculator__pb2.Image.SerializeToString,
        response_deserializer=calculator__pb2.Image.FromString,
        )


class CalculatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SquareRoot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Squared(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Factorial(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RotateImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SquareRoot': grpc.unary_unary_rpc_method_handler(
          servicer.SquareRoot,
          request_deserializer=calculator__pb2.Number.FromString,
          response_serializer=calculator__pb2.Number.SerializeToString,
      ),
      'Squared': grpc.unary_unary_rpc_method_handler(
          servicer.Squared,
          request_deserializer=calculator__pb2.Number.FromString,
          response_serializer=calculator__pb2.Number.SerializeToString,
      ),
      'Factorial': grpc.unary_unary_rpc_method_handler(
          servicer.Factorial,
          request_deserializer=calculator__pb2.Number.FromString,
          response_serializer=calculator__pb2.Number.SerializeToString,
      ),
      'RotateImage': grpc.unary_unary_rpc_method_handler(
          servicer.RotateImage,
          request_deserializer=calculator__pb2.Image.FromString,
          response_serializer=calculator__pb2.Image.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
