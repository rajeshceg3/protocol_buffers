# Enum values

## Sub-features

ARSENAL serializes/reads as numeric2 and resolves back to symbolic ARSENAL.

## How to get to it (user POV)

Compile `enum.proto` with protoc, construct a generated message, serialize and decode its bytes in a consumer.

## Driving it with grpcio-tools and Python

Run the documented helper. It compiles actual schemas into scratch and exercises the generated serializer/deserializer with assertions, retaining compile and contract results.

## Gotchas

Other enum values and unknown numeric-value policy need expanded cases when relevant. No external transport/service or judge is invoked.
