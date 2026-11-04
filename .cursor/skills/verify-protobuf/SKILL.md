---
name: verify-protobuf
description: Verify protocol_buffers schema compilation and real message roundtrips after changing scalar, repeated, nested or enum fields.
---
# Verify protobuf schemas

## Launch

This repository stores three proto3 schemas, not a network service. Requires Python3 plus grpcio-tools/protobuf. In an isolated environment install the helper's pinned requirements with `python3 -m pip install -r .cursor/skills/verify-protobuf/helpers/requirements.txt`, then run `python3 .cursor/skills/verify-protobuf/helpers/drive.py` from root. No accounts, sockets, data seed or external service. Install only in the environment you own.

## Doctor

The helper invokes `python -m grpc_tools.protoc` against enum.proto, helloworld.proto and nested.proto. Nonzero status is failure and retained. Generated Python modules go only to its own temporary directory. Readiness means actual schema compile succeeds, not just files exist.

## Drive

Import generated modules and serialize/deserialize real messages: SampleMessage scalar/repeated values and proto3defaults; ComplexMessage nested/repeated child messages; EnumMessage enum numeric/name. Assertions compare actual roundtripped fields and message equality. See features/README.md. No mocked serializer or server.

## Evidence

`artifacts/verification/protobuf.json` records source hashes, compile status/output, mapped contract names and pass/failure. This proves current Python message roundtrips, not cross-language interoperability, old-client compatibility, field-evolution safety or deployed transport. Schema evolution needs additional versioned golden-wire tests.

## Cleanup

Compiler child timeout is30seconds. Helper writes evidence then removes only its own generated-module temporary tree. Evidence is checked after cleanup. No repository source or original data is removed.

## Helpers

`python3 .cursor/skills/verify-protobuf/helpers/drive.py` is the complete local check. Run after schema changes and use `/maintain-verification-skill` when adding new message behavior. A compile-only pass is not a roundtrip pass.
