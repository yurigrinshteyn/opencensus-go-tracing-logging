# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpcDemo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpcDemo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0egrpcDemo.proto\"\x1e\n\x0bgrpcMessage\x12\x0f\n\x07payload\x18\x01 \x01(\t2:\n\x0bgrpcBackend\x12+\n\x0breturnValue\x12\x0c.grpcMessage\x1a\x0c.grpcMessage\"\x00\x62\x06proto3')
)




_GRPCMESSAGE = _descriptor.Descriptor(
  name='grpcMessage',
  full_name='grpcMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='grpcMessage.payload', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=18,
  serialized_end=48,
)

DESCRIPTOR.message_types_by_name['grpcMessage'] = _GRPCMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

grpcMessage = _reflection.GeneratedProtocolMessageType('grpcMessage', (_message.Message,), dict(
  DESCRIPTOR = _GRPCMESSAGE,
  __module__ = 'grpcDemo_pb2'
  # @@protoc_insertion_point(class_scope:grpcMessage)
  ))
_sym_db.RegisterMessage(grpcMessage)



_GRPCBACKEND = _descriptor.ServiceDescriptor(
  name='grpcBackend',
  full_name='grpcBackend',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=50,
  serialized_end=108,
  methods=[
  _descriptor.MethodDescriptor(
    name='returnValue',
    full_name='grpcBackend.returnValue',
    index=0,
    containing_service=None,
    input_type=_GRPCMESSAGE,
    output_type=_GRPCMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCBACKEND)

DESCRIPTOR.services_by_name['grpcBackend'] = _GRPCBACKEND

# @@protoc_insertion_point(module_scope)