# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/api_key.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/api_key.proto',
  package='yandex.cloud.iam.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!yandex/cloud/iam/v1/api_key.proto\x12\x13yandex.cloud.iam.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"u\n\x06\x41piKey\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12service_account_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\tBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_APIKEY = _descriptor.Descriptor(
  name='ApiKey',
  full_name='yandex.cloud.iam.v1.ApiKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iam.v1.ApiKey.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.ApiKey.service_account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iam.v1.ApiKey.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iam.v1.ApiKey.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=91,
  serialized_end=208,
)

_APIKEY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['ApiKey'] = _APIKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApiKey = _reflection.GeneratedProtocolMessageType('ApiKey', (_message.Message,), {
  'DESCRIPTOR' : _APIKEY,
  '__module__' : 'yandex.cloud.iam.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ApiKey)
  })
_sym_db.RegisterMessage(ApiKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
