# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera_6dof.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63\x61mera_6dof.proto\"O\n\x0bTranslation\x12\x0e\n\x01x\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x0e\n\x01y\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x0e\n\x01z\x18\x03 \x01(\x02H\x02\x88\x01\x01\x42\x04\n\x02_xB\x04\n\x02_yB\x04\n\x02_z\"d\n\nQuaternion\x12\x0e\n\x01w\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x0e\n\x01x\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x0e\n\x01y\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x0e\n\x01z\x18\x04 \x01(\x02H\x03\x88\x01\x01\x42\x04\n\x02_wB\x04\n\x02_xB\x04\n\x02_yB\x04\n\x02_z\"\xa2\x01\n\rAttitudeFrame\x12\x16\n\ttimestamp\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12&\n\x0btranslation\x18\x02 \x01(\x0b\x32\x0c.TranslationH\x01\x88\x01\x01\x12$\n\nquaternion\x18\x03 \x01(\x0b\x32\x0b.QuaternionH\x02\x88\x01\x01\x42\x0c\n\n_timestampB\x0e\n\x0c_translationB\r\n\x0b_quaternion\"\xe2\x01\n\nCameraData\x12\x12\n\x05width\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06height\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x19\n\x0c\x66ocal_length\x18\x03 \x01(\x01H\x02\x88\x01\x01\x12\x1e\n\x11principal_point_x\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x1e\n\x11principal_point_y\x18\x05 \x01(\x02H\x04\x88\x01\x01\x42\x08\n\x06_widthB\t\n\x07_heightB\x0f\n\r_focal_lengthB\x14\n\x12_principal_point_xB\x14\n\x12_principal_point_y\"\x8c\x01\n\x06SixDof\x12%\n\rattitude_data\x18\x01 \x03(\x0b\x32\x0e.AttitudeFrame\x12%\n\x0b\x63\x61mera_data\x18\x02 \x01(\x0b\x32\x0b.CameraDataH\x00\x88\x01\x01\x12\x16\n\tvideo_fps\x18\x03 \x01(\x02H\x01\x88\x01\x01\x42\x0e\n\x0c_camera_dataB\x0c\n\n_video_fpsb\x06proto3')



_TRANSLATION = DESCRIPTOR.message_types_by_name['Translation']
_QUATERNION = DESCRIPTOR.message_types_by_name['Quaternion']
_ATTITUDEFRAME = DESCRIPTOR.message_types_by_name['AttitudeFrame']
_CAMERADATA = DESCRIPTOR.message_types_by_name['CameraData']
_SIXDOF = DESCRIPTOR.message_types_by_name['SixDof']
Translation = _reflection.GeneratedProtocolMessageType('Translation', (_message.Message,), {
  'DESCRIPTOR' : _TRANSLATION,
  '__module__' : 'camera_6dof_pb2'
  # @@protoc_insertion_point(class_scope:Translation)
  })
_sym_db.RegisterMessage(Translation)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), {
  'DESCRIPTOR' : _QUATERNION,
  '__module__' : 'camera_6dof_pb2'
  # @@protoc_insertion_point(class_scope:Quaternion)
  })
_sym_db.RegisterMessage(Quaternion)

AttitudeFrame = _reflection.GeneratedProtocolMessageType('AttitudeFrame', (_message.Message,), {
  'DESCRIPTOR' : _ATTITUDEFRAME,
  '__module__' : 'camera_6dof_pb2'
  # @@protoc_insertion_point(class_scope:AttitudeFrame)
  })
_sym_db.RegisterMessage(AttitudeFrame)

CameraData = _reflection.GeneratedProtocolMessageType('CameraData', (_message.Message,), {
  'DESCRIPTOR' : _CAMERADATA,
  '__module__' : 'camera_6dof_pb2'
  # @@protoc_insertion_point(class_scope:CameraData)
  })
_sym_db.RegisterMessage(CameraData)

SixDof = _reflection.GeneratedProtocolMessageType('SixDof', (_message.Message,), {
  'DESCRIPTOR' : _SIXDOF,
  '__module__' : 'camera_6dof_pb2'
  # @@protoc_insertion_point(class_scope:SixDof)
  })
_sym_db.RegisterMessage(SixDof)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRANSLATION._serialized_start=21
  _TRANSLATION._serialized_end=100
  _QUATERNION._serialized_start=102
  _QUATERNION._serialized_end=202
  _ATTITUDEFRAME._serialized_start=205
  _ATTITUDEFRAME._serialized_end=367
  _CAMERADATA._serialized_start=370
  _CAMERADATA._serialized_end=596
  _SIXDOF._serialized_start=599
  _SIXDOF._serialized_end=739
# @@protoc_insertion_point(module_scope)