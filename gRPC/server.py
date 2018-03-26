import grpc, time
from concurrent import futures

# Generated Classes
import calculator_pb2, calculator_pb2_grpc

# Original Calculator
import calculator

# Class for defining server functions, from CalculatorServicer class
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    # Expose Square Root Function
    # Params: request, response (Number data type)
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

    # Expose Squared Function
    # Params: request, response (Number data type)
    def Squared(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.squared(request.value)
        return response

    def Factorial(self, request, context):
        print('Factorial Called')
        response = calculator_pb2.Number()
        response.value = calculator.factorial(request.value)
        return response

# Create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Use generated function to add defined class to server
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

print("Start server, listening on port 50051")
server.add_insecure_port('0.0.0.0:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
