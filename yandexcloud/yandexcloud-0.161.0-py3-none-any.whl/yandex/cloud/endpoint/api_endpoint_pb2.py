# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/endpoint/api_endpoint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/endpoint/api_endpoint.proto',
  package='yandex.cloud.endpoint',
  syntax='proto3',
  serialized_options=b'\n\031yandex.cloud.api.endpointZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/endpoint;endpoint',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(yandex/cloud/endpoint/api_endpoint.proto\x12\x15yandex.cloud.endpoint\"*\n\x0b\x41piEndpoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB_\n\x19yandex.cloud.api.endpointZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/endpoint;endpointb\x06proto3'
)




_APIENDPOINT = _descriptor.Descriptor(
  name='ApiEndpoint',
  full_name='yandex.cloud.endpoint.ApiEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.endpoint.ApiEndpoint.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='yandex.cloud.endpoint.ApiEndpoint.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['ApiEndpoint'] = _APIENDPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApiEndpoint = _reflection.GeneratedProtocolMessageType('ApiEndpoint', (_message.Message,), {
  'DESCRIPTOR' : _APIENDPOINT,
  '__module__' : 'yandex.cloud.endpoint.api_endpoint_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.endpoint.ApiEndpoint)
  })
_sym_db.RegisterMessage(ApiEndpoint)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
