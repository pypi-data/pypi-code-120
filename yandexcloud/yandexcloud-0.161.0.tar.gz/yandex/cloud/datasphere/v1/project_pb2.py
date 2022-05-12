# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v1/project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datasphere/v1/project.proto',
  package='yandex.cloud.datasphere.v1',
  syntax='proto3',
  serialized_options=b'\n\036yandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphere',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(yandex/cloud/datasphere/v1/project.proto\x12\x1ayandex.cloud.datasphere.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xff\x04\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x08settings\x18\x06 \x01(\x0b\x32,.yandex.cloud.datasphere.v1.Project.Settings\x12:\n\x06limits\x18\x07 \x01(\x0b\x32*.yandex.cloud.datasphere.v1.Project.Limits\x1a\x84\x02\n\x08Settings\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12\x1c\n\x14\x64\x61ta_proc_cluster_id\x18\x03 \x01(\t\x12L\n\x0b\x63ommit_mode\x18\x04 \x01(\x0e\x32\x37.yandex.cloud.datasphere.v1.Project.Settings.CommitMode\x12\x1a\n\x12security_group_ids\x18\x05 \x03(\t\"A\n\nCommitMode\x12\x1b\n\x17\x43OMMIT_MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\x1a\x7f\n\x06Limits\x12\x37\n\x12max_units_per_hour\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17max_units_per_execution\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueBk\n\x1eyandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphereb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])



_PROJECT_SETTINGS_COMMITMODE = _descriptor.EnumDescriptor(
  name='CommitMode',
  full_name='yandex.cloud.datasphere.v1.Project.Settings.CommitMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMMIT_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=583,
  serialized_end=648,
)
_sym_db.RegisterEnumDescriptor(_PROJECT_SETTINGS_COMMITMODE)


_PROJECT_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='yandex.cloud.datasphere.v1.Project.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.datasphere.v1.Project.Settings.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.datasphere.v1.Project.Settings.subnet_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_proc_cluster_id', full_name='yandex.cloud.datasphere.v1.Project.Settings.data_proc_cluster_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commit_mode', full_name='yandex.cloud.datasphere.v1.Project.Settings.commit_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_group_ids', full_name='yandex.cloud.datasphere.v1.Project.Settings.security_group_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROJECT_SETTINGS_COMMITMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=648,
)

_PROJECT_LIMITS = _descriptor.Descriptor(
  name='Limits',
  full_name='yandex.cloud.datasphere.v1.Project.Limits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_units_per_hour', full_name='yandex.cloud.datasphere.v1.Project.Limits.max_units_per_hour', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_units_per_execution', full_name='yandex.cloud.datasphere.v1.Project.Limits.max_units_per_execution', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=650,
  serialized_end=777,
)

_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='yandex.cloud.datasphere.v1.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.datasphere.v1.Project.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.datasphere.v1.Project.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.datasphere.v1.Project.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.datasphere.v1.Project.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.datasphere.v1.Project.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='yandex.cloud.datasphere.v1.Project.settings', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limits', full_name='yandex.cloud.datasphere.v1.Project.limits', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PROJECT_SETTINGS, _PROJECT_LIMITS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=777,
)

_PROJECT_SETTINGS.fields_by_name['commit_mode'].enum_type = _PROJECT_SETTINGS_COMMITMODE
_PROJECT_SETTINGS.containing_type = _PROJECT
_PROJECT_SETTINGS_COMMITMODE.containing_type = _PROJECT_SETTINGS
_PROJECT_LIMITS.fields_by_name['max_units_per_hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PROJECT_LIMITS.fields_by_name['max_units_per_execution'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_PROJECT_LIMITS.containing_type = _PROJECT
_PROJECT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PROJECT.fields_by_name['settings'].message_type = _PROJECT_SETTINGS
_PROJECT.fields_by_name['limits'].message_type = _PROJECT_LIMITS
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {

  'Settings' : _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {
    'DESCRIPTOR' : _PROJECT_SETTINGS,
    '__module__' : 'yandex.cloud.datasphere.v1.project_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.Project.Settings)
    })
  ,

  'Limits' : _reflection.GeneratedProtocolMessageType('Limits', (_message.Message,), {
    'DESCRIPTOR' : _PROJECT_LIMITS,
    '__module__' : 'yandex.cloud.datasphere.v1.project_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.Project.Limits)
    })
  ,
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'yandex.cloud.datasphere.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.Project)
  })
_sym_db.RegisterMessage(Project)
_sym_db.RegisterMessage(Project.Settings)
_sym_db.RegisterMessage(Project.Limits)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
