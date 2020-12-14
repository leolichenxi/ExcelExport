# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/DailyTasksTemplate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/DailyTasksTemplate.proto',
  package='Config',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fprotos/DailyTasksTemplate.proto\x12\x06\x43onfig\"\xcc\x04\n\x12\x44\x61ilyTasksTemplate\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04Kind\x18\x02 \x01(\x05\x12:\n\nLevelRange\x18\x03 \x01(\x0b\x32&.Config.DailyTasksTemplate.Levelrange_\x12\x0f\n\x07Quality\x18\x04 \x01(\x05\x12\r\n\x05Level\x18\x05 \x01(\x05\x12\x14\n\x0cShowProgress\x18\x06 \x01(\x05\x12\x10\n\x08\x41\x63\x63\x65ssId\x18\x07 \x01(\x05\x12\x36\n\x08TaskInfo\x18\x08 \x01(\x0b\x32$.Config.DailyTasksTemplate.Taskinfo_\x12\x33\n\x07Rewards\x18\t \x03(\x0b\x32\".Config.DailyTasksTemplate.Reward_\x12;\n\x0bShowRewards\x18\n \x03(\x0b\x32&.Config.DailyTasksTemplate.Showreward_\x1a\'\n\x0bLevelrange_\x12\x0b\n\x03Min\x18\x01 \x01(\x05\x12\x0b\n\x03Max\x18\x02 \x01(\x05\x1aI\n\tTaskinfo_\x12\x0c\n\x04Type\x18\x01 \x01(\x05\x12\x0e\n\x06Param1\x18\x02 \x01(\x05\x12\x0e\n\x06Param2\x18\x03 \x01(\x05\x12\x0e\n\x06Param3\x18\x04 \x01(\x05\x1a\x42\n\x07Reward_\x12\x0c\n\x04Type\x18\x01 \x01(\x05\x12\n\n\x02Id\x18\x02 \x01(\x05\x12\r\n\x05\x43ount\x18\x03 \x01(\x05\x12\x0e\n\x06Param1\x18\x04 \x01(\x05\x1a\x36\n\x0bShowreward_\x12\x0c\n\x04Type\x18\x01 \x01(\x05\x12\n\n\x02Id\x18\x02 \x01(\x05\x12\r\n\x05\x43ount\x18\x03 \x01(\x05\"I\n\x16\x44\x61ilyTasksTemplateList\x12/\n\x0b\x44\x61ilyTaskss\x18\x01 \x03(\x0b\x32\x1a.Config.DailyTasksTemplateb\x06proto3'
)




_DAILYTASKSTEMPLATE_LEVELRANGE_ = _descriptor.Descriptor(
  name='Levelrange_',
  full_name='Config.DailyTasksTemplate.Levelrange_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Min', full_name='Config.DailyTasksTemplate.Levelrange_.Min', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Max', full_name='Config.DailyTasksTemplate.Levelrange_.Max', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=394,
  serialized_end=433,
)

_DAILYTASKSTEMPLATE_TASKINFO_ = _descriptor.Descriptor(
  name='Taskinfo_',
  full_name='Config.DailyTasksTemplate.Taskinfo_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='Config.DailyTasksTemplate.Taskinfo_.Type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Param1', full_name='Config.DailyTasksTemplate.Taskinfo_.Param1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Param2', full_name='Config.DailyTasksTemplate.Taskinfo_.Param2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Param3', full_name='Config.DailyTasksTemplate.Taskinfo_.Param3', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=435,
  serialized_end=508,
)

_DAILYTASKSTEMPLATE_REWARD_ = _descriptor.Descriptor(
  name='Reward_',
  full_name='Config.DailyTasksTemplate.Reward_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='Config.DailyTasksTemplate.Reward_.Type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Id', full_name='Config.DailyTasksTemplate.Reward_.Id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Count', full_name='Config.DailyTasksTemplate.Reward_.Count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Param1', full_name='Config.DailyTasksTemplate.Reward_.Param1', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=510,
  serialized_end=576,
)

_DAILYTASKSTEMPLATE_SHOWREWARD_ = _descriptor.Descriptor(
  name='Showreward_',
  full_name='Config.DailyTasksTemplate.Showreward_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='Config.DailyTasksTemplate.Showreward_.Type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Id', full_name='Config.DailyTasksTemplate.Showreward_.Id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Count', full_name='Config.DailyTasksTemplate.Showreward_.Count', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=578,
  serialized_end=632,
)

_DAILYTASKSTEMPLATE = _descriptor.Descriptor(
  name='DailyTasksTemplate',
  full_name='Config.DailyTasksTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='Config.DailyTasksTemplate.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Kind', full_name='Config.DailyTasksTemplate.Kind', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LevelRange', full_name='Config.DailyTasksTemplate.LevelRange', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Quality', full_name='Config.DailyTasksTemplate.Quality', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Level', full_name='Config.DailyTasksTemplate.Level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ShowProgress', full_name='Config.DailyTasksTemplate.ShowProgress', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AccessId', full_name='Config.DailyTasksTemplate.AccessId', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TaskInfo', full_name='Config.DailyTasksTemplate.TaskInfo', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Rewards', full_name='Config.DailyTasksTemplate.Rewards', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ShowRewards', full_name='Config.DailyTasksTemplate.ShowRewards', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DAILYTASKSTEMPLATE_LEVELRANGE_, _DAILYTASKSTEMPLATE_TASKINFO_, _DAILYTASKSTEMPLATE_REWARD_, _DAILYTASKSTEMPLATE_SHOWREWARD_, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=632,
)


_DAILYTASKSTEMPLATELIST = _descriptor.Descriptor(
  name='DailyTasksTemplateList',
  full_name='Config.DailyTasksTemplateList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DailyTaskss', full_name='Config.DailyTasksTemplateList.DailyTaskss', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=634,
  serialized_end=707,
)

_DAILYTASKSTEMPLATE_LEVELRANGE_.containing_type = _DAILYTASKSTEMPLATE
_DAILYTASKSTEMPLATE_TASKINFO_.containing_type = _DAILYTASKSTEMPLATE
_DAILYTASKSTEMPLATE_REWARD_.containing_type = _DAILYTASKSTEMPLATE
_DAILYTASKSTEMPLATE_SHOWREWARD_.containing_type = _DAILYTASKSTEMPLATE
_DAILYTASKSTEMPLATE.fields_by_name['LevelRange'].message_type = _DAILYTASKSTEMPLATE_LEVELRANGE_
_DAILYTASKSTEMPLATE.fields_by_name['TaskInfo'].message_type = _DAILYTASKSTEMPLATE_TASKINFO_
_DAILYTASKSTEMPLATE.fields_by_name['Rewards'].message_type = _DAILYTASKSTEMPLATE_REWARD_
_DAILYTASKSTEMPLATE.fields_by_name['ShowRewards'].message_type = _DAILYTASKSTEMPLATE_SHOWREWARD_
_DAILYTASKSTEMPLATELIST.fields_by_name['DailyTaskss'].message_type = _DAILYTASKSTEMPLATE
DESCRIPTOR.message_types_by_name['DailyTasksTemplate'] = _DAILYTASKSTEMPLATE
DESCRIPTOR.message_types_by_name['DailyTasksTemplateList'] = _DAILYTASKSTEMPLATELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyTasksTemplate = _reflection.GeneratedProtocolMessageType('DailyTasksTemplate', (_message.Message,), {

  'Levelrange_' : _reflection.GeneratedProtocolMessageType('Levelrange_', (_message.Message,), {
    'DESCRIPTOR' : _DAILYTASKSTEMPLATE_LEVELRANGE_,
    '__module__' : 'protos.DailyTasksTemplate_pb2'
    # @@protoc_insertion_point(class_scope:Config.DailyTasksTemplate.Levelrange_)
    })
  ,

  'Taskinfo_' : _reflection.GeneratedProtocolMessageType('Taskinfo_', (_message.Message,), {
    'DESCRIPTOR' : _DAILYTASKSTEMPLATE_TASKINFO_,
    '__module__' : 'protos.DailyTasksTemplate_pb2'
    # @@protoc_insertion_point(class_scope:Config.DailyTasksTemplate.Taskinfo_)
    })
  ,

  'Reward_' : _reflection.GeneratedProtocolMessageType('Reward_', (_message.Message,), {
    'DESCRIPTOR' : _DAILYTASKSTEMPLATE_REWARD_,
    '__module__' : 'protos.DailyTasksTemplate_pb2'
    # @@protoc_insertion_point(class_scope:Config.DailyTasksTemplate.Reward_)
    })
  ,

  'Showreward_' : _reflection.GeneratedProtocolMessageType('Showreward_', (_message.Message,), {
    'DESCRIPTOR' : _DAILYTASKSTEMPLATE_SHOWREWARD_,
    '__module__' : 'protos.DailyTasksTemplate_pb2'
    # @@protoc_insertion_point(class_scope:Config.DailyTasksTemplate.Showreward_)
    })
  ,
  'DESCRIPTOR' : _DAILYTASKSTEMPLATE,
  '__module__' : 'protos.DailyTasksTemplate_pb2'
  # @@protoc_insertion_point(class_scope:Config.DailyTasksTemplate)
  })
_sym_db.RegisterMessage(DailyTasksTemplate)
_sym_db.RegisterMessage(DailyTasksTemplate.Levelrange_)
_sym_db.RegisterMessage(DailyTasksTemplate.Taskinfo_)
_sym_db.RegisterMessage(DailyTasksTemplate.Reward_)
_sym_db.RegisterMessage(DailyTasksTemplate.Showreward_)

DailyTasksTemplateList = _reflection.GeneratedProtocolMessageType('DailyTasksTemplateList', (_message.Message,), {
  'DESCRIPTOR' : _DAILYTASKSTEMPLATELIST,
  '__module__' : 'protos.DailyTasksTemplate_pb2'
  # @@protoc_insertion_point(class_scope:Config.DailyTasksTemplateList)
  })
_sym_db.RegisterMessage(DailyTasksTemplateList)


# @@protoc_insertion_point(module_scope)