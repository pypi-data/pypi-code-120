# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/cache_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/cdn/v1/cache_service.proto',
  package='yandex.cloud.cdn.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'yandex/cloud/cdn/v1/cache_service.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"E\n\x11PurgeCacheRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\r\n\x05paths\x18\x02 \x03(\t\"7\n\x12PurgeCacheMetadata\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"H\n\x14PrefetchCacheRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\r\n\x05paths\x18\x02 \x03(\t\":\n\x15PrefetchCacheMetadata\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=502\xfe\x02\n\x0c\x43\x61\x63heService\x12\xaf\x01\n\x05Purge\x12&.yandex.cloud.cdn.v1.PurgeCacheRequest\x1a!.yandex.cloud.operation.Operation\"[\x82\xd3\xe4\x93\x02&\"!/cdn/v1/cache/{resource_id}:purge:\x01*\xb2\xd2*+\n\x12PurgeCacheMetadata\x12\x15google.protobuf.Empty\x12\xbb\x01\n\x08Prefetch\x12).yandex.cloud.cdn.v1.PrefetchCacheRequest\x1a!.yandex.cloud.operation.Operation\"a\x82\xd3\xe4\x93\x02)\"$/cdn/v1/cache/{resource_id}:prefetch:\x01*\xb2\xd2*.\n\x15PrefetchCacheMetadata\x12\x15google.protobuf.EmptyBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_PURGECACHEREQUEST = _descriptor.Descriptor(
  name='PurgeCacheRequest',
  full_name='yandex.cloud.cdn.v1.PurgeCacheRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.cdn.v1.PurgeCacheRequest.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='yandex.cloud.cdn.v1.PurgeCacheRequest.paths', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=199,
  serialized_end=268,
)


_PURGECACHEMETADATA = _descriptor.Descriptor(
  name='PurgeCacheMetadata',
  full_name='yandex.cloud.cdn.v1.PurgeCacheMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.cdn.v1.PurgeCacheMetadata.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=270,
  serialized_end=325,
)


_PREFETCHCACHEREQUEST = _descriptor.Descriptor(
  name='PrefetchCacheRequest',
  full_name='yandex.cloud.cdn.v1.PrefetchCacheRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.cdn.v1.PrefetchCacheRequest.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='yandex.cloud.cdn.v1.PrefetchCacheRequest.paths', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=327,
  serialized_end=399,
)


_PREFETCHCACHEMETADATA = _descriptor.Descriptor(
  name='PrefetchCacheMetadata',
  full_name='yandex.cloud.cdn.v1.PrefetchCacheMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.cdn.v1.PrefetchCacheMetadata.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=401,
  serialized_end=459,
)

DESCRIPTOR.message_types_by_name['PurgeCacheRequest'] = _PURGECACHEREQUEST
DESCRIPTOR.message_types_by_name['PurgeCacheMetadata'] = _PURGECACHEMETADATA
DESCRIPTOR.message_types_by_name['PrefetchCacheRequest'] = _PREFETCHCACHEREQUEST
DESCRIPTOR.message_types_by_name['PrefetchCacheMetadata'] = _PREFETCHCACHEMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PurgeCacheRequest = _reflection.GeneratedProtocolMessageType('PurgeCacheRequest', (_message.Message,), {
  'DESCRIPTOR' : _PURGECACHEREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.cache_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.PurgeCacheRequest)
  })
_sym_db.RegisterMessage(PurgeCacheRequest)

PurgeCacheMetadata = _reflection.GeneratedProtocolMessageType('PurgeCacheMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PURGECACHEMETADATA,
  '__module__' : 'yandex.cloud.cdn.v1.cache_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.PurgeCacheMetadata)
  })
_sym_db.RegisterMessage(PurgeCacheMetadata)

PrefetchCacheRequest = _reflection.GeneratedProtocolMessageType('PrefetchCacheRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREFETCHCACHEREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.cache_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.PrefetchCacheRequest)
  })
_sym_db.RegisterMessage(PrefetchCacheRequest)

PrefetchCacheMetadata = _reflection.GeneratedProtocolMessageType('PrefetchCacheMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PREFETCHCACHEMETADATA,
  '__module__' : 'yandex.cloud.cdn.v1.cache_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.PrefetchCacheMetadata)
  })
_sym_db.RegisterMessage(PrefetchCacheMetadata)


DESCRIPTOR._options = None
_PURGECACHEREQUEST.fields_by_name['resource_id']._options = None
_PURGECACHEMETADATA.fields_by_name['resource_id']._options = None
_PREFETCHCACHEREQUEST.fields_by_name['resource_id']._options = None
_PREFETCHCACHEMETADATA.fields_by_name['resource_id']._options = None

_CACHESERVICE = _descriptor.ServiceDescriptor(
  name='CacheService',
  full_name='yandex.cloud.cdn.v1.CacheService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=462,
  serialized_end=844,
  methods=[
  _descriptor.MethodDescriptor(
    name='Purge',
    full_name='yandex.cloud.cdn.v1.CacheService.Purge',
    index=0,
    containing_service=None,
    input_type=_PURGECACHEREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002&\"!/cdn/v1/cache/{resource_id}:purge:\001*\262\322*+\n\022PurgeCacheMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Prefetch',
    full_name='yandex.cloud.cdn.v1.CacheService.Prefetch',
    index=1,
    containing_service=None,
    input_type=_PREFETCHCACHEREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002)\"$/cdn/v1/cache/{resource_id}:prefetch:\001*\262\322*.\n\025PrefetchCacheMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CACHESERVICE)

DESCRIPTOR.services_by_name['CacheService'] = _CACHESERVICE

# @@protoc_insertion_point(module_scope)
