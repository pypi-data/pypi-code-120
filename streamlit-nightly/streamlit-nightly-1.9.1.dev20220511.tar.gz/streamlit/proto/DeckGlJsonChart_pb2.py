# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/DeckGlJsonChart.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/DeckGlJsonChart.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%streamlit/proto/DeckGlJsonChart.proto\"M\n\x0f\x44\x65\x63kGlJsonChart\x12\x0c\n\x04json\x18\x01 \x01(\t\x12\x0f\n\x07tooltip\x18\x02 \x01(\t\x12\x1b\n\x13use_container_width\x18\x04 \x01(\x08\x62\x06proto3'
)




_DECKGLJSONCHART = _descriptor.Descriptor(
  name='DeckGlJsonChart',
  full_name='DeckGlJsonChart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='DeckGlJsonChart.json', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tooltip', full_name='DeckGlJsonChart.tooltip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_container_width', full_name='DeckGlJsonChart.use_container_width', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=41,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['DeckGlJsonChart'] = _DECKGLJSONCHART
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeckGlJsonChart = _reflection.GeneratedProtocolMessageType('DeckGlJsonChart', (_message.Message,), {
  'DESCRIPTOR' : _DECKGLJSONCHART,
  '__module__' : 'streamlit.proto.DeckGlJsonChart_pb2'
  # @@protoc_insertion_point(class_scope:DeckGlJsonChart)
  })
_sym_db.RegisterMessage(DeckGlJsonChart)


# @@protoc_insertion_point(module_scope)
