# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='calculator',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"2\n\x08\x43\x61lcInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10upSinceInSeconds\x18\x02 \x01(\x02\"\x12\n\x05\x46loat\x12\t\n\x01n\x18\x01 \x01(\x02\"*\n\tTwoFloats\x12\r\n\x05\x66irst\x18\x01 \x01(\x02\x12\x0e\n\x06second\x18\x02 \x01(\x02\"\x14\n\x07Integer\x12\t\n\x01n\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty2\xdd\x01\n\nCalculator\x12\x31\n\x03\x61\x64\x64\x12\x15.calculator.TwoFloats\x1a\x11.calculator.Float\"\x00\x12\x31\n\x03sub\x12\x15.calculator.TwoFloats\x1a\x11.calculator.Float\"\x00\x12\x36\n\x04rand\x12\x15.calculator.TwoFloats\x1a\x13.calculator.Integer\"\x00\x30\x01\x12\x31\n\x04info\x12\x11.calculator.Empty\x1a\x14.calculator.CalcInfo\"\x00\x62\x06proto3'
)




_CALCINFO = _descriptor.Descriptor(
  name='CalcInfo',
  full_name='calculator.CalcInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='calculator.CalcInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upSinceInSeconds', full_name='calculator.CalcInfo.upSinceInSeconds', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=32,
  serialized_end=82,
)


_FLOAT = _descriptor.Descriptor(
  name='Float',
  full_name='calculator.Float',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='calculator.Float.n', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=84,
  serialized_end=102,
)


_TWOFLOATS = _descriptor.Descriptor(
  name='TwoFloats',
  full_name='calculator.TwoFloats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='calculator.TwoFloats.first', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second', full_name='calculator.TwoFloats.second', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=104,
  serialized_end=146,
)


_INTEGER = _descriptor.Descriptor(
  name='Integer',
  full_name='calculator.Integer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='calculator.Integer.n', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=148,
  serialized_end=168,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='calculator.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=170,
  serialized_end=177,
)

DESCRIPTOR.message_types_by_name['CalcInfo'] = _CALCINFO
DESCRIPTOR.message_types_by_name['Float'] = _FLOAT
DESCRIPTOR.message_types_by_name['TwoFloats'] = _TWOFLOATS
DESCRIPTOR.message_types_by_name['Integer'] = _INTEGER
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalcInfo = _reflection.GeneratedProtocolMessageType('CalcInfo', (_message.Message,), {
  'DESCRIPTOR' : _CALCINFO,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.CalcInfo)
  })
_sym_db.RegisterMessage(CalcInfo)

Float = _reflection.GeneratedProtocolMessageType('Float', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.Float)
  })
_sym_db.RegisterMessage(Float)

TwoFloats = _reflection.GeneratedProtocolMessageType('TwoFloats', (_message.Message,), {
  'DESCRIPTOR' : _TWOFLOATS,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.TwoFloats)
  })
_sym_db.RegisterMessage(TwoFloats)

Integer = _reflection.GeneratedProtocolMessageType('Integer', (_message.Message,), {
  'DESCRIPTOR' : _INTEGER,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.Integer)
  })
_sym_db.RegisterMessage(Integer)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.Empty)
  })
_sym_db.RegisterMessage(Empty)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='calculator.Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=180,
  serialized_end=401,
  methods=[
  _descriptor.MethodDescriptor(
    name='add',
    full_name='calculator.Calculator.add',
    index=0,
    containing_service=None,
    input_type=_TWOFLOATS,
    output_type=_FLOAT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sub',
    full_name='calculator.Calculator.sub',
    index=1,
    containing_service=None,
    input_type=_TWOFLOATS,
    output_type=_FLOAT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rand',
    full_name='calculator.Calculator.rand',
    index=2,
    containing_service=None,
    input_type=_TWOFLOATS,
    output_type=_INTEGER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='info',
    full_name='calculator.Calculator.info',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CALCINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
