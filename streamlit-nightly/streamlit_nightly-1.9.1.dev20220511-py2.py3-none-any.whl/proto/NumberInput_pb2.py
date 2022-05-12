# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/NumberInput.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/NumberInput.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!streamlit/proto/NumberInput.proto\"\xd4\x02\n\x0bNumberInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0f\n\x07\x66orm_id\x18\x03 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x08 \x01(\t\x12\x0f\n\x07has_min\x18\x0b \x01(\x08\x12\x0f\n\x07has_max\x18\x0c \x01(\x08\x12(\n\tdata_type\x18\r \x01(\x0e\x32\x15.NumberInput.DataType\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x0e \x01(\x01\x12\x0c\n\x04step\x18\x0f \x01(\x01\x12\x0b\n\x03min\x18\x10 \x01(\x01\x12\x0b\n\x03max\x18\x11 \x01(\x01\x12\x0c\n\x04help\x18\x12 \x01(\t\x12\r\n\x05value\x18\x13 \x01(\x01\x12\x11\n\tset_value\x18\x14 \x01(\x08\x12\x10\n\x08\x64isabled\x18\x15 \x01(\x08\"\x1e\n\x08\x44\x61taType\x12\x07\n\x03INT\x10\x00\x12\t\n\x05\x46LOAT\x10\x01J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\t\x10\nJ\x04\x08\n\x10\x0b\x62\x06proto3'
)



_NUMBERINPUT_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='NumberInput.DataType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=312,
  serialized_end=342,
)
_sym_db.RegisterEnumDescriptor(_NUMBERINPUT_DATATYPE)


_NUMBERINPUT = _descriptor.Descriptor(
  name='NumberInput',
  full_name='NumberInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='NumberInput.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='NumberInput.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='form_id', full_name='NumberInput.form_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='NumberInput.format', index=3,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_min', full_name='NumberInput.has_min', index=4,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_max', full_name='NumberInput.has_max', index=5,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='NumberInput.data_type', index=6,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default', full_name='NumberInput.default', index=7,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='step', full_name='NumberInput.step', index=8,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min', full_name='NumberInput.min', index=9,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max', full_name='NumberInput.max', index=10,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='help', full_name='NumberInput.help', index=11,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='NumberInput.value', index=12,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_value', full_name='NumberInput.set_value', index=13,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='NumberInput.disabled', index=14,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NUMBERINPUT_DATATYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=378,
)

_NUMBERINPUT.fields_by_name['data_type'].enum_type = _NUMBERINPUT_DATATYPE
_NUMBERINPUT_DATATYPE.containing_type = _NUMBERINPUT
DESCRIPTOR.message_types_by_name['NumberInput'] = _NUMBERINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NumberInput = _reflection.GeneratedProtocolMessageType('NumberInput', (_message.Message,), {
  'DESCRIPTOR' : _NUMBERINPUT,
  '__module__' : 'streamlit.proto.NumberInput_pb2'
  # @@protoc_insertion_point(class_scope:NumberInput)
  })
_sym_db.RegisterMessage(NumberInput)


# @@protoc_insertion_point(module_scope)
