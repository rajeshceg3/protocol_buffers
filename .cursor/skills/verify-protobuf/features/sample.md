# Scalar and repeated values

## Sub-features

id7, is_sample true, name sample, repeated1/3/5 roundtrip; empty message defaults id0/false.

## How to get to it (user POV)

Compile `helloworld.proto` with protoc, construct a generated message, serialize and decode its bytes in a consumer.

## Driving it with grpcio-tools and Python

Run the documented helper. It compiles actual schemas into scratch and exercises the generated serializer/deserializer with assertions, retaining compile and contract results.

## Gotchas

This does not test unknown fields or historical wire formats. No external transport/service or judge is invoked.
