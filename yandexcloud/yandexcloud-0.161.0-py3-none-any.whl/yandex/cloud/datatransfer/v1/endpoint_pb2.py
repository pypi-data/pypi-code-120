# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import clickhouse_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_clickhouse__pb2
from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2
from yandex.cloud.datatransfer.v1.endpoint import mongo_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mongo__pb2
from yandex.cloud.datatransfer.v1.endpoint import mysql_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mysql__pb2
from yandex.cloud.datatransfer.v1.endpoint import postgres_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_postgres__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datatransfer/v1/endpoint.proto',
  package='yandex.cloud.datatransfer.v1',
  syntax='proto3',
  serialized_options=b'\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransfer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+yandex/cloud/datatransfer/v1/endpoint.proto\x12\x1cyandex.cloud.datatransfer.v1\x1a\x36yandex/cloud/datatransfer/v1/endpoint/clickhouse.proto\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\x1a\x31yandex/cloud/datatransfer/v1/endpoint/mongo.proto\x1a\x31yandex/cloud/datatransfer/v1/endpoint/mysql.proto\x1a\x34yandex/cloud/datatransfer/v1/endpoint/postgres.proto\"\x81\x02\n\x08\x45ndpoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x42\n\x06labels\x18\x06 \x03(\x0b\x32\x32.yandex.cloud.datatransfer.v1.Endpoint.LabelsEntry\x12@\n\x08settings\x18\x34 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.EndpointSettings\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9e\x05\n\x10\x45ndpointSettings\x12J\n\x0cmysql_source\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.datatransfer.v1.endpoint.MysqlSourceH\x00\x12P\n\x0fpostgres_source\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.datatransfer.v1.endpoint.PostgresSourceH\x00\x12J\n\x0cmongo_source\x18\t \x01(\x0b\x32\x32.yandex.cloud.datatransfer.v1.endpoint.MongoSourceH\x00\x12T\n\x11\x63lickhouse_source\x18\x10 \x01(\x0b\x32\x37.yandex.cloud.datatransfer.v1.endpoint.ClickhouseSourceH\x00\x12J\n\x0cmysql_target\x18\x65 \x01(\x0b\x32\x32.yandex.cloud.datatransfer.v1.endpoint.MysqlTargetH\x00\x12P\n\x0fpostgres_target\x18\x66 \x01(\x0b\x32\x35.yandex.cloud.datatransfer.v1.endpoint.PostgresTargetH\x00\x12T\n\x11\x63lickhouse_target\x18h \x01(\x0b\x32\x37.yandex.cloud.datatransfer.v1.endpoint.ClickhouseTargetH\x00\x12J\n\x0cmongo_target\x18o \x01(\x0b\x32\x32.yandex.cloud.datatransfer.v1.endpoint.MongoTargetH\x00\x42\n\n\x08settingsBq\n yandex.cloud.api.datatransfer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1;datatransferb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_clickhouse__pb2.DESCRIPTOR,yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2.DESCRIPTOR,yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mongo__pb2.DESCRIPTOR,yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mysql__pb2.DESCRIPTOR,yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_postgres__pb2.DESCRIPTOR,])




_ENDPOINT_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.datatransfer.v1.Endpoint.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.datatransfer.v1.Endpoint.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.datatransfer.v1.Endpoint.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=599,
)

_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='yandex.cloud.datatransfer.v1.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.datatransfer.v1.Endpoint.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.datatransfer.v1.Endpoint.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.datatransfer.v1.Endpoint.name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.datatransfer.v1.Endpoint.description', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.datatransfer.v1.Endpoint.labels', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='yandex.cloud.datatransfer.v1.Endpoint.settings', index=5,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENDPOINT_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=599,
)


_ENDPOINTSETTINGS = _descriptor.Descriptor(
  name='EndpointSettings',
  full_name='yandex.cloud.datatransfer.v1.EndpointSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mysql_source', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.mysql_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postgres_source', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.postgres_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mongo_source', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.mongo_source', index=2,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clickhouse_source', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.clickhouse_source', index=3,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mysql_target', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.mysql_target', index=4,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postgres_target', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.postgres_target', index=5,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clickhouse_target', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.clickhouse_target', index=6,
      number=104, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mongo_target', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.mongo_target', index=7,
      number=111, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='settings', full_name='yandex.cloud.datatransfer.v1.EndpointSettings.settings',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=602,
  serialized_end=1272,
)

_ENDPOINT_LABELSENTRY.containing_type = _ENDPOINT
_ENDPOINT.fields_by_name['labels'].message_type = _ENDPOINT_LABELSENTRY
_ENDPOINT.fields_by_name['settings'].message_type = _ENDPOINTSETTINGS
_ENDPOINTSETTINGS.fields_by_name['mysql_source'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mysql__pb2._MYSQLSOURCE
_ENDPOINTSETTINGS.fields_by_name['postgres_source'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_postgres__pb2._POSTGRESSOURCE
_ENDPOINTSETTINGS.fields_by_name['mongo_source'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mongo__pb2._MONGOSOURCE
_ENDPOINTSETTINGS.fields_by_name['clickhouse_source'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_clickhouse__pb2._CLICKHOUSESOURCE
_ENDPOINTSETTINGS.fields_by_name['mysql_target'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mysql__pb2._MYSQLTARGET
_ENDPOINTSETTINGS.fields_by_name['postgres_target'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_postgres__pb2._POSTGRESTARGET
_ENDPOINTSETTINGS.fields_by_name['clickhouse_target'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_clickhouse__pb2._CLICKHOUSETARGET
_ENDPOINTSETTINGS.fields_by_name['mongo_target'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_mongo__pb2._MONGOTARGET
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['mysql_source'])
_ENDPOINTSETTINGS.fields_by_name['mysql_source'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['postgres_source'])
_ENDPOINTSETTINGS.fields_by_name['postgres_source'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['mongo_source'])
_ENDPOINTSETTINGS.fields_by_name['mongo_source'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['clickhouse_source'])
_ENDPOINTSETTINGS.fields_by_name['clickhouse_source'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['mysql_target'])
_ENDPOINTSETTINGS.fields_by_name['mysql_target'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['postgres_target'])
_ENDPOINTSETTINGS.fields_by_name['postgres_target'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['clickhouse_target'])
_ENDPOINTSETTINGS.fields_by_name['clickhouse_target'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
_ENDPOINTSETTINGS.oneofs_by_name['settings'].fields.append(
  _ENDPOINTSETTINGS.fields_by_name['mongo_target'])
_ENDPOINTSETTINGS.fields_by_name['mongo_target'].containing_oneof = _ENDPOINTSETTINGS.oneofs_by_name['settings']
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['EndpointSettings'] = _ENDPOINTSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENDPOINT_LABELSENTRY,
    '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.Endpoint.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)
_sym_db.RegisterMessage(Endpoint.LabelsEntry)

EndpointSettings = _reflection.GeneratedProtocolMessageType('EndpointSettings', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTSETTINGS,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.EndpointSettings)
  })
_sym_db.RegisterMessage(EndpointSettings)


DESCRIPTOR._options = None
_ENDPOINT_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
