# Nested messages

## Sub-features

one_msg id4/name single and one multiple_msg id5/name list roundtrip unchanged.

## How to get to it (user POV)

Compile `nested.proto` with protoc, construct a generated message, serialize and decode its bytes in a consumer.

## Driving it with grpcio-tools and Python

Run the documented helper. It compiles actual schemas into scratch and exercises the generated serializer/deserializer with assertions, retaining compile and contract results.

## Gotchas

Presence, large repeated lists and cross-version changes are not fully covered. No external transport/service or judge is invoked.
