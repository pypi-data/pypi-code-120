# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/service/dataset/dataset_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api import ids_pb2 as api_dot_ids__pb2
from layer.api.value import ticket_pb2 as api_dot_value_dot_ticket__pb2
from layer.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/service/dataset/dataset_api.proto\x12\x0b\x61pi.dataset\x1a\rapi/ids.proto\x1a\x16\x61pi/value/ticket.proto\x1a\x17validate/validate.proto\"\xc3\x01\n\x07\x43ommand\x12\x32\n\rdataset_query\x18\x01 \x01(\x0b\x32\x19.api.dataset.DatasetQueryH\x00\x12?\n\x14static_dataset_query\x18\x02 \x01(\x0b\x32\x1f.api.dataset.StaticDatasetQueryH\x00\x12\x38\n\x10\x64\x61taset_snapshot\x18\x03 \x01(\x0b\x32\x1c.api.dataset.DatasetSnapshotH\x00\x42\t\n\x07\x63ommand\"9\n\x0c\x44\x61tasetQuery\x12)\n\x06ticket\x18\x01 \x01(\x0b\x32\x0f.api.DataTicketB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"/\n\x12StaticDatasetQuery\x12\x19\n\x08num_rows\x18\x01 \x01(\x03\x42\x07\xfa\x42\x04\"\x02(\x00\"B\n\x0f\x44\x61tasetSnapshot\x12/\n\x08\x62uild_id\x18\x01 \x01(\x0b\x32\x13.api.DatasetBuildIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x42*\n\x15\x63om.layer.api.datasetB\x0f\x44\x61tasetApiProtoP\x01\x62\x06proto3')



_COMMAND = DESCRIPTOR.message_types_by_name['Command']
_DATASETQUERY = DESCRIPTOR.message_types_by_name['DatasetQuery']
_STATICDATASETQUERY = DESCRIPTOR.message_types_by_name['StaticDatasetQuery']
_DATASETSNAPSHOT = DESCRIPTOR.message_types_by_name['DatasetSnapshot']
Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'api.service.dataset.dataset_api_pb2'
  # @@protoc_insertion_point(class_scope:api.dataset.Command)
  })
_sym_db.RegisterMessage(Command)

DatasetQuery = _reflection.GeneratedProtocolMessageType('DatasetQuery', (_message.Message,), {
  'DESCRIPTOR' : _DATASETQUERY,
  '__module__' : 'api.service.dataset.dataset_api_pb2'
  # @@protoc_insertion_point(class_scope:api.dataset.DatasetQuery)
  })
_sym_db.RegisterMessage(DatasetQuery)

StaticDatasetQuery = _reflection.GeneratedProtocolMessageType('StaticDatasetQuery', (_message.Message,), {
  'DESCRIPTOR' : _STATICDATASETQUERY,
  '__module__' : 'api.service.dataset.dataset_api_pb2'
  # @@protoc_insertion_point(class_scope:api.dataset.StaticDatasetQuery)
  })
_sym_db.RegisterMessage(StaticDatasetQuery)

DatasetSnapshot = _reflection.GeneratedProtocolMessageType('DatasetSnapshot', (_message.Message,), {
  'DESCRIPTOR' : _DATASETSNAPSHOT,
  '__module__' : 'api.service.dataset.dataset_api_pb2'
  # @@protoc_insertion_point(class_scope:api.dataset.DatasetSnapshot)
  })
_sym_db.RegisterMessage(DatasetSnapshot)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.layer.api.datasetB\017DatasetApiProtoP\001'
  _DATASETQUERY.fields_by_name['ticket']._options = None
  _DATASETQUERY.fields_by_name['ticket']._serialized_options = b'\372B\005\212\001\002\020\001'
  _STATICDATASETQUERY.fields_by_name['num_rows']._options = None
  _STATICDATASETQUERY.fields_by_name['num_rows']._serialized_options = b'\372B\004\"\002(\000'
  _DATASETSNAPSHOT.fields_by_name['build_id']._options = None
  _DATASETSNAPSHOT.fields_by_name['build_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _COMMAND._serialized_start=119
  _COMMAND._serialized_end=314
  _DATASETQUERY._serialized_start=316
  _DATASETQUERY._serialized_end=373
  _STATICDATASETQUERY._serialized_start=375
  _STATICDATASETQUERY._serialized_end=422
  _DATASETSNAPSHOT._serialized_start=424
  _DATASETSNAPSHOT._serialized_end=490
# @@protoc_insertion_point(module_scope)
