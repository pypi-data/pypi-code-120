# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki_vector/messaging/shared.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anki_vector.messaging import behavior_pb2 as anki__vector_dot_messaging_dot_behavior__pb2
from anki_vector.messaging import cube_pb2 as anki__vector_dot_messaging_dot_cube__pb2
from anki_vector.messaging import alexa_pb2 as anki__vector_dot_messaging_dot_alexa__pb2
from anki_vector.messaging import messages_pb2 as anki__vector_dot_messaging_dot_messages__pb2
from anki_vector.messaging import settings_pb2 as anki__vector_dot_messaging_dot_settings__pb2
from anki_vector.messaging import extensions_pb2 as anki__vector_dot_messaging_dot_extensions__pb2
from anki_vector.messaging import response_status_pb2 as anki__vector_dot_messaging_dot_response__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='anki_vector/messaging/shared.proto',
  package='Anki.Vector.external_interface',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\"anki_vector/messaging/shared.proto\x12\x1e\x41nki.Vector.external_interface\x1a$anki_vector/messaging/behavior.proto\x1a anki_vector/messaging/cube.proto\x1a!anki_vector/messaging/alexa.proto\x1a$anki_vector/messaging/messages.proto\x1a$anki_vector/messaging/settings.proto\x1a&anki_vector/messaging/extensions.proto\x1a+anki_vector/messaging/response_status.proto\"J\n\x16ProtocolVersionRequest\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\x03\x12\x18\n\x10min_host_version\x18\x02 \x01(\x03\"\xa7\x01\n\x17ProtocolVersionResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.Anki.Vector.external_interface.ProtocolVersionResponse.Result\x12\x14\n\x0chost_version\x18\x02 \x01(\x03\"&\n\x06Result\x12\x0f\n\x0bUNSUPPORTED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\"h\n\x12\x43onnectionResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\x12\x12\n\nis_primary\x18\x02 \x01(\x08\"\xd2\x0b\n\x05\x45vent\x12P\n\x13time_stamped_status\x18\x01 \x01(\x0b\x32\x31.Anki.Vector.external_interface.TimeStampedStatusH\x00\x12@\n\nonboarding\x18\x02 \x01(\x0b\x32*.Anki.Vector.external_interface.OnboardingH\x00\x12=\n\twake_word\x18\x03 \x01(\x0b\x32(.Anki.Vector.external_interface.WakeWordH\x00\x12O\n\x12\x61ttention_transfer\x18\x04 \x01(\x0b\x32\x31.Anki.Vector.external_interface.AttentionTransferH\x00\x12P\n\x13robot_observed_face\x18\x05 \x01(\x0b\x32\x31.Anki.Vector.external_interface.RobotObservedFaceH\x00\x12\x64\n\x1erobot_changed_observed_face_id\x18\x06 \x01(\x0b\x32:.Anki.Vector.external_interface.RobotChangedObservedFaceIDH\x00\x12\x43\n\x0cobject_event\x18\x07 \x01(\x0b\x32+.Anki.Vector.external_interface.ObjectEventH\x00\x12K\n\x10stimulation_info\x18\x08 \x01(\x0b\x32/.Anki.Vector.external_interface.StimulationInfoH\x00\x12\x41\n\x0bphoto_taken\x18\t \x01(\x0b\x32*.Anki.Vector.external_interface.PhotoTakenH\x00\x12\x41\n\x0brobot_state\x18\n \x01(\x0b\x32*.Anki.Vector.external_interface.RobotStateH\x00\x12\x43\n\x0c\x63ube_battery\x18\x0b \x01(\x0b\x32+.Anki.Vector.external_interface.CubeBatteryH\x00\x12\x43\n\nkeep_alive\x18\x0c \x01(\x0b\x32-.Anki.Vector.external_interface.KeepAlivePingH\x00\x12Q\n\x13\x63onnection_response\x18\r \x01(\x0b\x32\x32.Anki.Vector.external_interface.ConnectionResponseH\x00\x12\x45\n\rjdocs_changed\x18\x0e \x01(\x0b\x32,.Anki.Vector.external_interface.JdocsChangedH\x00\x12J\n\x10\x61lexa_auth_event\x18\x0f \x01(\x0b\x32..Anki.Vector.external_interface.AlexaAuthEventH\x00\x12R\n\x14mirror_mode_disabled\x18\x10 \x01(\x0b\x32\x32.Anki.Vector.external_interface.MirrorModeDisabledH\x00\x12]\n\x1avision_modes_auto_disabled\x18\x11 \x01(\x0b\x32\x37.Anki.Vector.external_interface.VisionModesAutoDisabledH\x00\x12\x61\n\x1c\x63heck_update_status_response\x18\x12 \x01(\x0b\x32\x39.Anki.Vector.external_interface.CheckUpdateStatusResponseH\x00\x12\x41\n\x0buser_intent\x18\x13 \x01(\x0b\x32*.Anki.Vector.external_interface.UserIntentH\x00\x42\x0c\n\nevent_type\"\x1a\n\nFilterList\x12\x0c\n\x04list\x18\x01 \x03(\t\"\xb6\x01\n\x0c\x45ventRequest\x12@\n\nwhite_list\x18\x01 \x01(\x0b\x32*.Anki.Vector.external_interface.FilterListH\x00\x12@\n\nblack_list\x18\x02 \x01(\x0b\x32*.Anki.Vector.external_interface.FilterListH\x00\x12\x15\n\rconnection_id\x18\x03 \x01(\tB\x0b\n\tlist_type\"\x8b\x01\n\rEventResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\x12\x34\n\x05\x65vent\x18\x02 \x01(\x0b\x32%.Anki.Vector.external_interface.Event:\x04\x80\xa6\x1d\x01\"I\n\x19UserAuthenticationRequest\x12\x17\n\x0fuser_session_id\x18\x01 \x01(\x0c\x12\x13\n\x0b\x63lient_name\x18\x02 \x01(\x0c\"\xf0\x01\n\x1aUserAuthenticationResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\x12M\n\x04\x63ode\x18\x02 \x01(\x0e\x32?.Anki.Vector.external_interface.UserAuthenticationResponse.Code\x12\x19\n\x11\x63lient_token_guid\x18\x03 \x01(\x0c\"(\n\x04\x43ode\x12\x10\n\x0cUNAUTHORIZED\x10\x00\x12\x0e\n\nAUTHORIZED\x10\x01\x62\x06proto3'
  ,
  dependencies=[anki__vector_dot_messaging_dot_behavior__pb2.DESCRIPTOR,anki__vector_dot_messaging_dot_cube__pb2.DESCRIPTOR,anki__vector_dot_messaging_dot_alexa__pb2.DESCRIPTOR,anki__vector_dot_messaging_dot_messages__pb2.DESCRIPTOR,anki__vector_dot_messaging_dot_settings__pb2.DESCRIPTOR,anki__vector_dot_messaging_dot_extensions__pb2.DESCRIPTOR,anki__vector_dot_messaging_dot_response__status__pb2.DESCRIPTOR,])



_PROTOCOLVERSIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='Anki.Vector.external_interface.ProtocolVersionResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=544,
  serialized_end=582,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOLVERSIONRESPONSE_RESULT)

_USERAUTHENTICATIONRESPONSE_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='Anki.Vector.external_interface.UserAuthenticationResponse.Code',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2814,
  serialized_end=2854,
)
_sym_db.RegisterEnumDescriptor(_USERAUTHENTICATIONRESPONSE_CODE)


_PROTOCOLVERSIONREQUEST = _descriptor.Descriptor(
  name='ProtocolVersionRequest',
  full_name='Anki.Vector.external_interface.ProtocolVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_version', full_name='Anki.Vector.external_interface.ProtocolVersionRequest.client_version', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_host_version', full_name='Anki.Vector.external_interface.ProtocolVersionRequest.min_host_version', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=338,
  serialized_end=412,
)


_PROTOCOLVERSIONRESPONSE = _descriptor.Descriptor(
  name='ProtocolVersionResponse',
  full_name='Anki.Vector.external_interface.ProtocolVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='Anki.Vector.external_interface.ProtocolVersionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_version', full_name='Anki.Vector.external_interface.ProtocolVersionResponse.host_version', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROTOCOLVERSIONRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=582,
)


_CONNECTIONRESPONSE = _descriptor.Descriptor(
  name='ConnectionResponse',
  full_name='Anki.Vector.external_interface.ConnectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Anki.Vector.external_interface.ConnectionResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_primary', full_name='Anki.Vector.external_interface.ConnectionResponse.is_primary', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=584,
  serialized_end=688,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='Anki.Vector.external_interface.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_stamped_status', full_name='Anki.Vector.external_interface.Event.time_stamped_status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='onboarding', full_name='Anki.Vector.external_interface.Event.onboarding', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wake_word', full_name='Anki.Vector.external_interface.Event.wake_word', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attention_transfer', full_name='Anki.Vector.external_interface.Event.attention_transfer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robot_observed_face', full_name='Anki.Vector.external_interface.Event.robot_observed_face', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robot_changed_observed_face_id', full_name='Anki.Vector.external_interface.Event.robot_changed_observed_face_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_event', full_name='Anki.Vector.external_interface.Event.object_event', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stimulation_info', full_name='Anki.Vector.external_interface.Event.stimulation_info', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photo_taken', full_name='Anki.Vector.external_interface.Event.photo_taken', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robot_state', full_name='Anki.Vector.external_interface.Event.robot_state', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cube_battery', full_name='Anki.Vector.external_interface.Event.cube_battery', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keep_alive', full_name='Anki.Vector.external_interface.Event.keep_alive', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_response', full_name='Anki.Vector.external_interface.Event.connection_response', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jdocs_changed', full_name='Anki.Vector.external_interface.Event.jdocs_changed', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alexa_auth_event', full_name='Anki.Vector.external_interface.Event.alexa_auth_event', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mirror_mode_disabled', full_name='Anki.Vector.external_interface.Event.mirror_mode_disabled', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vision_modes_auto_disabled', full_name='Anki.Vector.external_interface.Event.vision_modes_auto_disabled', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_update_status_response', full_name='Anki.Vector.external_interface.Event.check_update_status_response', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_intent', full_name='Anki.Vector.external_interface.Event.user_intent', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
      name='event_type', full_name='Anki.Vector.external_interface.Event.event_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=691,
  serialized_end=2181,
)


_FILTERLIST = _descriptor.Descriptor(
  name='FilterList',
  full_name='Anki.Vector.external_interface.FilterList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='Anki.Vector.external_interface.FilterList.list', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=2183,
  serialized_end=2209,
)


_EVENTREQUEST = _descriptor.Descriptor(
  name='EventRequest',
  full_name='Anki.Vector.external_interface.EventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='white_list', full_name='Anki.Vector.external_interface.EventRequest.white_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='black_list', full_name='Anki.Vector.external_interface.EventRequest.black_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='Anki.Vector.external_interface.EventRequest.connection_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
      name='list_type', full_name='Anki.Vector.external_interface.EventRequest.list_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=2212,
  serialized_end=2394,
)


_EVENTRESPONSE = _descriptor.Descriptor(
  name='EventResponse',
  full_name='Anki.Vector.external_interface.EventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Anki.Vector.external_interface.EventResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='Anki.Vector.external_interface.EventResponse.event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\200\246\035\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2397,
  serialized_end=2536,
)


_USERAUTHENTICATIONREQUEST = _descriptor.Descriptor(
  name='UserAuthenticationRequest',
  full_name='Anki.Vector.external_interface.UserAuthenticationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_session_id', full_name='Anki.Vector.external_interface.UserAuthenticationRequest.user_session_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_name', full_name='Anki.Vector.external_interface.UserAuthenticationRequest.client_name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=2538,
  serialized_end=2611,
)


_USERAUTHENTICATIONRESPONSE = _descriptor.Descriptor(
  name='UserAuthenticationResponse',
  full_name='Anki.Vector.external_interface.UserAuthenticationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Anki.Vector.external_interface.UserAuthenticationResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='Anki.Vector.external_interface.UserAuthenticationResponse.code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_token_guid', full_name='Anki.Vector.external_interface.UserAuthenticationResponse.client_token_guid', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERAUTHENTICATIONRESPONSE_CODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2614,
  serialized_end=2854,
)

_PROTOCOLVERSIONRESPONSE.fields_by_name['result'].enum_type = _PROTOCOLVERSIONRESPONSE_RESULT
_PROTOCOLVERSIONRESPONSE_RESULT.containing_type = _PROTOCOLVERSIONRESPONSE
_CONNECTIONRESPONSE.fields_by_name['status'].message_type = anki__vector_dot_messaging_dot_response__status__pb2._RESPONSESTATUS
_EVENT.fields_by_name['time_stamped_status'].message_type = anki__vector_dot_messaging_dot_messages__pb2._TIMESTAMPEDSTATUS
_EVENT.fields_by_name['onboarding'].message_type = anki__vector_dot_messaging_dot_messages__pb2._ONBOARDING
_EVENT.fields_by_name['wake_word'].message_type = anki__vector_dot_messaging_dot_messages__pb2._WAKEWORD
_EVENT.fields_by_name['attention_transfer'].message_type = anki__vector_dot_messaging_dot_messages__pb2._ATTENTIONTRANSFER
_EVENT.fields_by_name['robot_observed_face'].message_type = anki__vector_dot_messaging_dot_messages__pb2._ROBOTOBSERVEDFACE
_EVENT.fields_by_name['robot_changed_observed_face_id'].message_type = anki__vector_dot_messaging_dot_messages__pb2._ROBOTCHANGEDOBSERVEDFACEID
_EVENT.fields_by_name['object_event'].message_type = anki__vector_dot_messaging_dot_cube__pb2._OBJECTEVENT
_EVENT.fields_by_name['stimulation_info'].message_type = anki__vector_dot_messaging_dot_messages__pb2._STIMULATIONINFO
_EVENT.fields_by_name['photo_taken'].message_type = anki__vector_dot_messaging_dot_messages__pb2._PHOTOTAKEN
_EVENT.fields_by_name['robot_state'].message_type = anki__vector_dot_messaging_dot_messages__pb2._ROBOTSTATE
_EVENT.fields_by_name['cube_battery'].message_type = anki__vector_dot_messaging_dot_messages__pb2._CUBEBATTERY
_EVENT.fields_by_name['keep_alive'].message_type = anki__vector_dot_messaging_dot_messages__pb2._KEEPALIVEPING
_EVENT.fields_by_name['connection_response'].message_type = _CONNECTIONRESPONSE
_EVENT.fields_by_name['jdocs_changed'].message_type = anki__vector_dot_messaging_dot_settings__pb2._JDOCSCHANGED
_EVENT.fields_by_name['alexa_auth_event'].message_type = anki__vector_dot_messaging_dot_alexa__pb2._ALEXAAUTHEVENT
_EVENT.fields_by_name['mirror_mode_disabled'].message_type = anki__vector_dot_messaging_dot_messages__pb2._MIRRORMODEDISABLED
_EVENT.fields_by_name['vision_modes_auto_disabled'].message_type = anki__vector_dot_messaging_dot_messages__pb2._VISIONMODESAUTODISABLED
_EVENT.fields_by_name['check_update_status_response'].message_type = anki__vector_dot_messaging_dot_messages__pb2._CHECKUPDATESTATUSRESPONSE
_EVENT.fields_by_name['user_intent'].message_type = anki__vector_dot_messaging_dot_messages__pb2._USERINTENT
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['time_stamped_status'])
_EVENT.fields_by_name['time_stamped_status'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['onboarding'])
_EVENT.fields_by_name['onboarding'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['wake_word'])
_EVENT.fields_by_name['wake_word'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['attention_transfer'])
_EVENT.fields_by_name['attention_transfer'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['robot_observed_face'])
_EVENT.fields_by_name['robot_observed_face'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['robot_changed_observed_face_id'])
_EVENT.fields_by_name['robot_changed_observed_face_id'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['object_event'])
_EVENT.fields_by_name['object_event'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['stimulation_info'])
_EVENT.fields_by_name['stimulation_info'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['photo_taken'])
_EVENT.fields_by_name['photo_taken'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['robot_state'])
_EVENT.fields_by_name['robot_state'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['cube_battery'])
_EVENT.fields_by_name['cube_battery'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['keep_alive'])
_EVENT.fields_by_name['keep_alive'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['connection_response'])
_EVENT.fields_by_name['connection_response'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['jdocs_changed'])
_EVENT.fields_by_name['jdocs_changed'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['alexa_auth_event'])
_EVENT.fields_by_name['alexa_auth_event'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['mirror_mode_disabled'])
_EVENT.fields_by_name['mirror_mode_disabled'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['vision_modes_auto_disabled'])
_EVENT.fields_by_name['vision_modes_auto_disabled'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['check_update_status_response'])
_EVENT.fields_by_name['check_update_status_response'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENT.oneofs_by_name['event_type'].fields.append(
  _EVENT.fields_by_name['user_intent'])
_EVENT.fields_by_name['user_intent'].containing_oneof = _EVENT.oneofs_by_name['event_type']
_EVENTREQUEST.fields_by_name['white_list'].message_type = _FILTERLIST
_EVENTREQUEST.fields_by_name['black_list'].message_type = _FILTERLIST
_EVENTREQUEST.oneofs_by_name['list_type'].fields.append(
  _EVENTREQUEST.fields_by_name['white_list'])
_EVENTREQUEST.fields_by_name['white_list'].containing_oneof = _EVENTREQUEST.oneofs_by_name['list_type']
_EVENTREQUEST.oneofs_by_name['list_type'].fields.append(
  _EVENTREQUEST.fields_by_name['black_list'])
_EVENTREQUEST.fields_by_name['black_list'].containing_oneof = _EVENTREQUEST.oneofs_by_name['list_type']
_EVENTRESPONSE.fields_by_name['status'].message_type = anki__vector_dot_messaging_dot_response__status__pb2._RESPONSESTATUS
_EVENTRESPONSE.fields_by_name['event'].message_type = _EVENT
_USERAUTHENTICATIONRESPONSE.fields_by_name['status'].message_type = anki__vector_dot_messaging_dot_response__status__pb2._RESPONSESTATUS
_USERAUTHENTICATIONRESPONSE.fields_by_name['code'].enum_type = _USERAUTHENTICATIONRESPONSE_CODE
_USERAUTHENTICATIONRESPONSE_CODE.containing_type = _USERAUTHENTICATIONRESPONSE
DESCRIPTOR.message_types_by_name['ProtocolVersionRequest'] = _PROTOCOLVERSIONREQUEST
DESCRIPTOR.message_types_by_name['ProtocolVersionResponse'] = _PROTOCOLVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['ConnectionResponse'] = _CONNECTIONRESPONSE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['FilterList'] = _FILTERLIST
DESCRIPTOR.message_types_by_name['EventRequest'] = _EVENTREQUEST
DESCRIPTOR.message_types_by_name['EventResponse'] = _EVENTRESPONSE
DESCRIPTOR.message_types_by_name['UserAuthenticationRequest'] = _USERAUTHENTICATIONREQUEST
DESCRIPTOR.message_types_by_name['UserAuthenticationResponse'] = _USERAUTHENTICATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtocolVersionRequest = _reflection.GeneratedProtocolMessageType('ProtocolVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLVERSIONREQUEST,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ProtocolVersionRequest)
  })
_sym_db.RegisterMessage(ProtocolVersionRequest)

ProtocolVersionResponse = _reflection.GeneratedProtocolMessageType('ProtocolVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLVERSIONRESPONSE,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ProtocolVersionResponse)
  })
_sym_db.RegisterMessage(ProtocolVersionResponse)

ConnectionResponse = _reflection.GeneratedProtocolMessageType('ConnectionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONRESPONSE,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ConnectionResponse)
  })
_sym_db.RegisterMessage(ConnectionResponse)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.Event)
  })
_sym_db.RegisterMessage(Event)

FilterList = _reflection.GeneratedProtocolMessageType('FilterList', (_message.Message,), {
  'DESCRIPTOR' : _FILTERLIST,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.FilterList)
  })
_sym_db.RegisterMessage(FilterList)

EventRequest = _reflection.GeneratedProtocolMessageType('EventRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREQUEST,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.EventRequest)
  })
_sym_db.RegisterMessage(EventRequest)

EventResponse = _reflection.GeneratedProtocolMessageType('EventResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRESPONSE,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.EventResponse)
  })
_sym_db.RegisterMessage(EventResponse)

UserAuthenticationRequest = _reflection.GeneratedProtocolMessageType('UserAuthenticationRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAUTHENTICATIONREQUEST,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.UserAuthenticationRequest)
  })
_sym_db.RegisterMessage(UserAuthenticationRequest)

UserAuthenticationResponse = _reflection.GeneratedProtocolMessageType('UserAuthenticationResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAUTHENTICATIONRESPONSE,
  '__module__' : 'anki_vector.messaging.shared_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.UserAuthenticationResponse)
  })
_sym_db.RegisterMessage(UserAuthenticationResponse)


_EVENTRESPONSE._options = None
# @@protoc_insertion_point(module_scope)
