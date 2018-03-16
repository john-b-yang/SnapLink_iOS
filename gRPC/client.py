import grpc

# Generated Classes
import calculator_pb2, calculator_pb2_grpc

# Open gRPC Channel
print('Opening channel')
channel = grpc.insecure_channel('localhost:50051')

# Create Stub (aka Client) using channel
print('Creating Stub')
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Create valid request message
print('Creating Request')
number = calculator_pb2.Number(value=16)

# Make Call
print('Making Call')
response = stub.SquareRoot(number)
print('Hello')

print(response.value)
