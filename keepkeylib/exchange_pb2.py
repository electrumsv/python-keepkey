# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exchange.proto',
  package='',
<<<<<<< HEAD
  serialized_pb='\n\x0e\x65xchange.proto\"[\n\x0f\x45xchangeAddress\x12\x11\n\tcoin_type\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65st_tag\x18\x03 \x01(\t\x12\x12\n\nrs_address\x18\x04 \x01(\t\"\xa7\x02\n\x10\x45xchangeResponse\x12)\n\x0f\x64\x65posit_address\x18\x01 \x01(\x0b\x32\x10.ExchangeAddress\x12\x16\n\x0e\x64\x65posit_amount\x18\x02 \x01(\x04\x12\x12\n\nexpiration\x18\x03 \x01(\r\x12\x13\n\x0bquoted_rate\x18\x04 \x01(\x04\x12,\n\x12withdrawal_address\x18\x05 \x01(\x0b\x32\x10.ExchangeAddress\x12\x19\n\x11withdrawal_amount\x18\x06 \x01(\x04\x12(\n\x0ereturn_address\x18\x07 \x01(\x0b\x32\x10.ExchangeAddress\x12\x0f\n\x07\x61pi_key\x18\x08 \x01(\x0c\x12\x11\n\tminer_fee\x18\t \x01(\x04\x12\x10\n\x08order_id\x18\n \x01(\x0c\"P\n\x16SignedExchangeResponse\x12#\n\x08response\x18\x01 \x01(\x0b\x32\x11.ExchangeResponse\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x42.\n\x1b\x63om.keepkey.device-protocolB\x0fKeepKeyExchange')
=======
  serialized_pb='\n\x0e\x65xchange.proto\"H\n\x0f\x45xchangeAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65st_tag\x18\x02 \x01(\t\x12\x12\n\nrs_address\x18\x03 \x01(\t\"\xce\x01\n\x0f\x45xchangeRequest\x12\x19\n\x11withdrawal_amount\x18\x01 \x01(\x04\x12,\n\x12withdrawal_address\x18\x02 \x01(\x0b\x32\x10.ExchangeAddress\x12\x1c\n\x14withdrawal_coin_type\x18\x03 \x01(\t\x12\x19\n\x11\x64\x65posit_coin_type\x18\x04 \x01(\t\x12(\n\x0ereturn_address\x18\x05 \x01(\x0b\x32\x10.ExchangeAddress\x12\x0f\n\x07\x61pi_key\x18\x06 \x01(\x0c\"\xb4\x01\n\x10\x45xchangeResponse\x12!\n\x07request\x18\x01 \x01(\x0b\x32\x10.ExchangeRequest\x12)\n\x0f\x64\x65posit_address\x18\x02 \x01(\x0b\x32\x10.ExchangeAddress\x12\x16\n\x0e\x64\x65posit_amount\x18\x03 \x01(\x04\x12\x12\n\nexpiration\x18\x04 \x01(\r\x12\x13\n\x0bquoted_rate\x18\x05 \x01(\r\x12\x11\n\tsignature\x18\x06 \x01(\x0c\x42.\n\x1b\x63om.keepkey.device-protocolB\x0fKeepKeyExchange')
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c




_EXCHANGEADDRESS = _descriptor.Descriptor(
  name='ExchangeAddress',
  full_name='ExchangeAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='coin_type', full_name='ExchangeAddress.coin_type', index=0,
=======
      name='address', full_name='ExchangeAddress.address', index=0,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='address', full_name='ExchangeAddress.address', index=1,
=======
      name='dest_tag', full_name='ExchangeAddress.dest_tag', index=1,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='dest_tag', full_name='ExchangeAddress.dest_tag', index=2,
=======
      name='rs_address', full_name='ExchangeAddress.rs_address', index=2,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
<<<<<<< HEAD
    _descriptor.FieldDescriptor(
      name='rs_address', full_name='ExchangeAddress.rs_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
=======
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=18,
<<<<<<< HEAD
  serialized_end=109,
)


_EXCHANGERESPONSE = _descriptor.Descriptor(
  name='ExchangeResponse',
  full_name='ExchangeResponse',
=======
  serialized_end=90,
)


_EXCHANGEREQUEST = _descriptor.Descriptor(
  name='ExchangeRequest',
  full_name='ExchangeRequest',
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='deposit_address', full_name='ExchangeResponse.deposit_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deposit_amount', full_name='ExchangeResponse.deposit_amount', index=1,
      number=2, type=4, cpp_type=4, label=1,
=======
      name='withdrawal_amount', full_name='ExchangeRequest.withdrawal_amount', index=0,
      number=1, type=4, cpp_type=4, label=1,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='expiration', full_name='ExchangeResponse.expiration', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quoted_rate', full_name='ExchangeResponse.quoted_rate', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='withdrawal_address', full_name='ExchangeResponse.withdrawal_address', index=4,
      number=5, type=11, cpp_type=10, label=1,
=======
      name='withdrawal_address', full_name='ExchangeRequest.withdrawal_address', index=1,
      number=2, type=11, cpp_type=10, label=1,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='withdrawal_amount', full_name='ExchangeResponse.withdrawal_amount', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_address', full_name='ExchangeResponse.return_address', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
=======
      name='withdrawal_coin_type', full_name='ExchangeRequest.withdrawal_coin_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='api_key', full_name='ExchangeResponse.api_key', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
=======
      name='deposit_coin_type', full_name='ExchangeRequest.deposit_coin_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='miner_fee', full_name='ExchangeResponse.miner_fee', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
=======
      name='return_address', full_name='ExchangeRequest.return_address', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='order_id', full_name='ExchangeResponse.order_id', index=9,
      number=10, type=12, cpp_type=9, label=1,
=======
      name='api_key', full_name='ExchangeRequest.api_key', index=5,
      number=6, type=12, cpp_type=9, label=1,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
<<<<<<< HEAD
  serialized_start=112,
  serialized_end=407,
)


_SIGNEDEXCHANGERESPONSE = _descriptor.Descriptor(
  name='SignedExchangeResponse',
  full_name='SignedExchangeResponse',
=======
  serialized_start=93,
  serialized_end=299,
)


_EXCHANGERESPONSE = _descriptor.Descriptor(
  name='ExchangeResponse',
  full_name='ExchangeResponse',
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='response', full_name='SignedExchangeResponse.response', index=0,
=======
      name='request', full_name='ExchangeResponse.request', index=0,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
<<<<<<< HEAD
      name='signature', full_name='SignedExchangeResponse.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
=======
      name='deposit_address', full_name='ExchangeResponse.deposit_address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deposit_amount', full_name='ExchangeResponse.deposit_amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='ExchangeResponse.expiration', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quoted_rate', full_name='ExchangeResponse.quoted_rate', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ExchangeResponse.signature', index=5,
      number=6, type=12, cpp_type=9, label=1,
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
<<<<<<< HEAD
  serialized_start=409,
  serialized_end=489,
)

_EXCHANGERESPONSE.fields_by_name['deposit_address'].message_type = _EXCHANGEADDRESS
_EXCHANGERESPONSE.fields_by_name['withdrawal_address'].message_type = _EXCHANGEADDRESS
_EXCHANGERESPONSE.fields_by_name['return_address'].message_type = _EXCHANGEADDRESS
_SIGNEDEXCHANGERESPONSE.fields_by_name['response'].message_type = _EXCHANGERESPONSE
DESCRIPTOR.message_types_by_name['ExchangeAddress'] = _EXCHANGEADDRESS
DESCRIPTOR.message_types_by_name['ExchangeResponse'] = _EXCHANGERESPONSE
DESCRIPTOR.message_types_by_name['SignedExchangeResponse'] = _SIGNEDEXCHANGERESPONSE
=======
  serialized_start=302,
  serialized_end=482,
)

_EXCHANGEREQUEST.fields_by_name['withdrawal_address'].message_type = _EXCHANGEADDRESS
_EXCHANGEREQUEST.fields_by_name['return_address'].message_type = _EXCHANGEADDRESS
_EXCHANGERESPONSE.fields_by_name['request'].message_type = _EXCHANGEREQUEST
_EXCHANGERESPONSE.fields_by_name['deposit_address'].message_type = _EXCHANGEADDRESS
DESCRIPTOR.message_types_by_name['ExchangeAddress'] = _EXCHANGEADDRESS
DESCRIPTOR.message_types_by_name['ExchangeRequest'] = _EXCHANGEREQUEST
DESCRIPTOR.message_types_by_name['ExchangeResponse'] = _EXCHANGERESPONSE
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c

class ExchangeAddress(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXCHANGEADDRESS

  # @@protoc_insertion_point(class_scope:ExchangeAddress)

<<<<<<< HEAD
class ExchangeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXCHANGERESPONSE

  # @@protoc_insertion_point(class_scope:ExchangeResponse)

class SignedExchangeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIGNEDEXCHANGERESPONSE

  # @@protoc_insertion_point(class_scope:SignedExchangeResponse)
=======
class ExchangeRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXCHANGEREQUEST

  # @@protoc_insertion_point(class_scope:ExchangeRequest)

class ExchangeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXCHANGERESPONSE

  # @@protoc_insertion_point(class_scope:ExchangeResponse)
>>>>>>> daa296fe2a18805a376e34ab6189bb301cdcac9c


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\033com.keepkey.device-protocolB\017KeepKeyExchange')
# @@protoc_insertion_point(module_scope)