# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/user_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.oauth import claims_pb2 as yandex_dot_cloud_dot_oauth_dot_claims__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/organizationmanager/v1/user_service.proto',
  package='yandex.cloud.organizationmanager.v1',
  syntax='proto3',
  serialized_options=b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6yandex/cloud/organizationmanager/v1/user_service.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\x1fyandex/cloud/oauth/claims.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"y\n\x12ListMembersRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\xd7\x01\n\x13ListMembersResponse\x12X\n\x05users\x18\x01 \x03(\x0b\x32I.yandex.cloud.organizationmanager.v1.ListMembersResponse.OrganizationUser\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1aM\n\x10OrganizationUser\x12\x39\n\x0esubject_claims\x18\x01 \x01(\x0b\x32!.yandex.cloud.oauth.SubjectClaims\"^\n\x17\x44\x65leteMembershipRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nsubject_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"c\n\x18\x44\x65leteMembershipMetadata\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nsubject_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"c\n\x18\x44\x65leteMembershipResponse\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nsubject_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=502\xdc\x03\n\x0bUserService\x12\xc8\x01\n\x0bListMembers\x12\x37.yandex.cloud.organizationmanager.v1.ListMembersRequest\x1a\x38.yandex.cloud.organizationmanager.v1.ListMembersResponse\"F\x82\xd3\xe4\x93\x02@\x12>/organization-manager/v1/organizations/{organization_id}/users\x12\x81\x02\n\x10\x44\x65leteMembership\x12<.yandex.cloud.organizationmanager.v1.DeleteMembershipRequest\x1a!.yandex.cloud.operation.Operation\"\x8b\x01\x82\xd3\xe4\x93\x02M*K/organization-manager/v1/organizations/{organization_id}/users/{subject_id}\xb2\xd2*4\n\x18\x44\x65leteMembershipMetadata\x12\x18\x44\x65leteMembershipResponseB\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_oauth_dot_claims__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_LISTMEMBERSREQUEST = _descriptor.Descriptor(
  name='ListMembersRequest',
  full_name='yandex.cloud.organizationmanager.v1.ListMembersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.ListMembersRequest.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.organizationmanager.v1.ListMembersRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.organizationmanager.v1.ListMembersRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=263,
  serialized_end=384,
)


_LISTMEMBERSRESPONSE_ORGANIZATIONUSER = _descriptor.Descriptor(
  name='OrganizationUser',
  full_name='yandex.cloud.organizationmanager.v1.ListMembersResponse.OrganizationUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_claims', full_name='yandex.cloud.organizationmanager.v1.ListMembersResponse.OrganizationUser.subject_claims', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=525,
  serialized_end=602,
)

_LISTMEMBERSRESPONSE = _descriptor.Descriptor(
  name='ListMembersResponse',
  full_name='yandex.cloud.organizationmanager.v1.ListMembersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='yandex.cloud.organizationmanager.v1.ListMembersResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.organizationmanager.v1.ListMembersResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LISTMEMBERSRESPONSE_ORGANIZATIONUSER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=602,
)


_DELETEMEMBERSHIPREQUEST = _descriptor.Descriptor(
  name='DeleteMembershipRequest',
  full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipRequest.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject_id', full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipRequest.subject_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=604,
  serialized_end=698,
)


_DELETEMEMBERSHIPMETADATA = _descriptor.Descriptor(
  name='DeleteMembershipMetadata',
  full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipMetadata.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject_id', full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipMetadata.subject_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=700,
  serialized_end=799,
)


_DELETEMEMBERSHIPRESPONSE = _descriptor.Descriptor(
  name='DeleteMembershipResponse',
  full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipResponse.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject_id', full_name='yandex.cloud.organizationmanager.v1.DeleteMembershipResponse.subject_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=801,
  serialized_end=900,
)

_LISTMEMBERSRESPONSE_ORGANIZATIONUSER.fields_by_name['subject_claims'].message_type = yandex_dot_cloud_dot_oauth_dot_claims__pb2._SUBJECTCLAIMS
_LISTMEMBERSRESPONSE_ORGANIZATIONUSER.containing_type = _LISTMEMBERSRESPONSE
_LISTMEMBERSRESPONSE.fields_by_name['users'].message_type = _LISTMEMBERSRESPONSE_ORGANIZATIONUSER
DESCRIPTOR.message_types_by_name['ListMembersRequest'] = _LISTMEMBERSREQUEST
DESCRIPTOR.message_types_by_name['ListMembersResponse'] = _LISTMEMBERSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteMembershipRequest'] = _DELETEMEMBERSHIPREQUEST
DESCRIPTOR.message_types_by_name['DeleteMembershipMetadata'] = _DELETEMEMBERSHIPMETADATA
DESCRIPTOR.message_types_by_name['DeleteMembershipResponse'] = _DELETEMEMBERSHIPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListMembersRequest = _reflection.GeneratedProtocolMessageType('ListMembersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMEMBERSREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListMembersRequest)
  })
_sym_db.RegisterMessage(ListMembersRequest)

ListMembersResponse = _reflection.GeneratedProtocolMessageType('ListMembersResponse', (_message.Message,), {

  'OrganizationUser' : _reflection.GeneratedProtocolMessageType('OrganizationUser', (_message.Message,), {
    'DESCRIPTOR' : _LISTMEMBERSRESPONSE_ORGANIZATIONUSER,
    '__module__' : 'yandex.cloud.organizationmanager.v1.user_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListMembersResponse.OrganizationUser)
    })
  ,
  'DESCRIPTOR' : _LISTMEMBERSRESPONSE,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.ListMembersResponse)
  })
_sym_db.RegisterMessage(ListMembersResponse)
_sym_db.RegisterMessage(ListMembersResponse.OrganizationUser)

DeleteMembershipRequest = _reflection.GeneratedProtocolMessageType('DeleteMembershipRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMEMBERSHIPREQUEST,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.DeleteMembershipRequest)
  })
_sym_db.RegisterMessage(DeleteMembershipRequest)

DeleteMembershipMetadata = _reflection.GeneratedProtocolMessageType('DeleteMembershipMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMEMBERSHIPMETADATA,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.DeleteMembershipMetadata)
  })
_sym_db.RegisterMessage(DeleteMembershipMetadata)

DeleteMembershipResponse = _reflection.GeneratedProtocolMessageType('DeleteMembershipResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMEMBERSHIPRESPONSE,
  '__module__' : 'yandex.cloud.organizationmanager.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.DeleteMembershipResponse)
  })
_sym_db.RegisterMessage(DeleteMembershipResponse)


DESCRIPTOR._options = None
_LISTMEMBERSREQUEST.fields_by_name['organization_id']._options = None
_LISTMEMBERSREQUEST.fields_by_name['page_size']._options = None
_LISTMEMBERSREQUEST.fields_by_name['page_token']._options = None
_DELETEMEMBERSHIPREQUEST.fields_by_name['organization_id']._options = None
_DELETEMEMBERSHIPREQUEST.fields_by_name['subject_id']._options = None
_DELETEMEMBERSHIPMETADATA.fields_by_name['organization_id']._options = None
_DELETEMEMBERSHIPMETADATA.fields_by_name['subject_id']._options = None
_DELETEMEMBERSHIPRESPONSE.fields_by_name['organization_id']._options = None
_DELETEMEMBERSHIPRESPONSE.fields_by_name['subject_id']._options = None

_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='yandex.cloud.organizationmanager.v1.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=903,
  serialized_end=1379,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListMembers',
    full_name='yandex.cloud.organizationmanager.v1.UserService.ListMembers',
    index=0,
    containing_service=None,
    input_type=_LISTMEMBERSREQUEST,
    output_type=_LISTMEMBERSRESPONSE,
    serialized_options=b'\202\323\344\223\002@\022>/organization-manager/v1/organizations/{organization_id}/users',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteMembership',
    full_name='yandex.cloud.organizationmanager.v1.UserService.DeleteMembership',
    index=1,
    containing_service=None,
    input_type=_DELETEMEMBERSHIPREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002M*K/organization-manager/v1/organizations/{organization_id}/users/{subject_id}\262\322*4\n\030DeleteMembershipMetadata\022\030DeleteMembershipResponse',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)
