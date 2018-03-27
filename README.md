# SnapLink_iOS
SnapLink : Visual Appliance Identification and Control in Smart Buildings

Todo:
- Import gRPC w/ cocoapods
- Establish connection between gRPC server and iOS application
- Run dummy function from gRPC on iOS app

In Process:
- Run through gRPC online tutorial
- Write .proto file defining server functionality
- Creating server.py with dummy functions

Completed:

Tips:
- Protobuf Compilation: protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/test.proto
- For concurrent library, please use python 2.7
- Encode/Decode Images into Base64 Format: https://bit.ly/2pLAd1l
