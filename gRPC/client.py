import grpc, base64

# Generated Classes
import calculator_pb2, calculator_pb2_grpc

# Open gRPC Channel
print('Opening channel')
channel = grpc.insecure_channel('127.0.0.1:50051')

# Create Stub (aka Client) using channel
print('Creating Stub')
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Create Number request message
print('Creating Request')
number = calculator_pb2.Number(value=16)

# Make Call
print('Making Square Root Call')
response = stub.SquareRoot(number)
print("Response: ", response.value)

print('Making Squared Call')
response = stub.Squared(number)
print("Response: ", response.value)

print('Making Factorial Call')
response = stub.Factorial(number)
print("Response: ", response.value)

print('Making Rotate Image Call')
# Encode Image as Base64 String
with open("test.png", "rb") as image_file:
    encode_string = base64.b64encode(image_file.read())
# Create Image request message
image = calculator_pb2.Image(hash=encode_string)
# Function Call
response = stub.RotateImage(image)
# Decode base64 into image and save
with open("test.png", "wb") as file:
    file.write(response.hash.decode('base64'))
