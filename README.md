# SnapLink_iOS
SnapLink : Visual Appliance Identification and Control in Smart Buildings

Todo:
- Establish connection between gRPC server and iOS application
- Run dummy function from gRPC on iOS app

In Process:
- Write Swift client code

Completed:
- Run through gRPC online tutorial
- Write .proto file defining server functionality
- Creating server.py with dummy functions
- Import gRPC, Swift Protobuf w/ cocoapods
- Create Swift Client proto file w/ protobuf

Tips:
- Protobuf Compilation: protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/test.proto
- For concurrent library, please use python 2.7
- Encode/Decode Images into Base64 Format: https://bit.ly/2pLAd1l
- Nice Gentle Tutorial: https://bit.ly/2DWorqf
- Swift Protocol Buffer: https://github.com/apple/swift-protobuf
