import grpc

# Generated Classes
import calculator_pb2, calculator_pb2_grpc

# Open gRPC Channel
print('Opening channel')
channel = grpc.insecure_channel('127.0.0.1:50051')

# Create Stub (aka Client) using channel
print('Creating Stub')
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Create valid request message
print('Creating Request')
number = calculator_pb2.Number(value=16)

# Make Call
print('Making Square Root Call')
response = stub.SquareRoot(number)
print("Response: ", response.value)

print('Making Squared Call')
response = stub.Squared(number)
print("Response: ", response.value)
