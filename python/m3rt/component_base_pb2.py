# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: component_base.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='component_base.proto',
  package='',
  serialized_pb='\n\x14\x63omponent_base.proto\"*\n\x0bM3StatusAll\x12\x0c\n\x04name\x18\x01 \x03(\t\x12\r\n\x05\x64\x61tum\x18\x02 \x03(\x0c\"\\\n\x0cM3CommandAll\x12\x10\n\x08name_cmd\x18\x01 \x03(\t\x12\x12\n\nname_param\x18\x02 \x03(\t\x12\x11\n\tdatum_cmd\x18\x03 \x03(\x0c\x12\x13\n\x0b\x64\x61tum_param\x18\x04 \x03(\x0c\".\n\x0fM3StatusLogPage\x12\x1b\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x0c.M3StatusAll\"\x85\x01\n\x0cM3BaseStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x05state\x18\x02 \x01(\x0e\x32\r.M3COMP_STATE:\x11M3COMP_STATE_INIT\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x12\n\x04rate\x18\x04 \x01(\t:\x04\x66\x61st\x12\x0f\n\x07version\x18\x05 \x01(\t\"\xbb\x01\n\x10M3EtherCATStatus\x12\x16\n\nnetwork_id\x18\x01 \x01(\x05:\x02-1\x12\x19\n\rserial_number\x18\x02 \x01(\x05:\x02-1\x12\x18\n\x0cproduct_code\x18\x03 \x01(\x05:\x02-1\x12\x0e\n\x06\x61\x63tive\x18\x04 \x01(\x05\x12\x0e\n\x06online\x18\x05 \x01(\x05\x12\x13\n\x0boperational\x18\x06 \x01(\x05\x12\x10\n\x08\x61l_state\x18\x07 \x01(\x05\x12\x13\n\x0bpdo_version\x18\x14 \x01(\t\"}\n\x12M3MonitorComponent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x05state\x18\x02 \x01(\x0e\x32\r.M3COMP_STATE\x12\x1c\n\x14\x63ycle_time_status_us\x18\x03 \x01(\x01\x12\x1d\n\x15\x63ycle_time_command_us\x18\x04 \x01(\x01\"\x12\n\x10M3MonitorCommand\"\x10\n\x0eM3MonitorParam\"\xe0\x03\n\x0fM3MonitorStatus\x12\x1b\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\r.M3BaseStatus\x12\x19\n\x11num_components_rt\x18\x02 \x01(\x05\x12\x19\n\x11num_components_ec\x18\x03 \x01(\x05\x12\x16\n\x0enum_components\x18\x04 \x01(\x05\x12\x1d\n\x15num_components_safeop\x18\x05 \x01(\x05\x12\x19\n\x11num_components_op\x18\x06 \x01(\x05\x12\x1a\n\x12num_components_err\x18\x07 \x01(\x05\x12\x13\n\x0boperational\x18\x08 \x01(\x08\x12\x1c\n\x14\x63ycle_time_status_us\x18\t \x01(\x01\x12\x1d\n\x15\x63ycle_time_command_us\x18\n \x01(\x01\x12\x15\n\rcycle_time_us\x18\x0b \x01(\x01\x12\x1a\n\x12\x63ycle_frequency_hz\x18\x0c \x01(\x01\x12\'\n\ncomponents\x18\r \x03(\x0b\x32\x13.M3MonitorComponent\x12\x1b\n\x13num_ethercat_cycles\x18\x0e \x01(\x05\x12\x19\n\x11\x63ycle_time_max_us\x18\x0f \x01(\x01\x12&\n\nec_domains\x18\x10 \x03(\x0b\x32\x12.M3MonitorEcDomain\"\x96\x01\n\x11M3MonitorEcDomain\x12\x16\n\x0et_ecat_wait_rx\x18\x01 \x01(\x03\x12\x11\n\tt_ecat_rx\x18\x02 \x01(\x03\x12\x17\n\x0ft_ecat_wait_shm\x18\x03 \x01(\x03\x12\x12\n\nt_ecat_shm\x18\x04 \x01(\x03\x12\x16\n\x0et_ecat_wait_tx\x18\x05 \x01(\x03\x12\x11\n\tt_ecat_tx\x18\x06 \x01(\x03*i\n\x0cM3COMP_STATE\x12\x15\n\x11M3COMP_STATE_INIT\x10\x00\x12\x14\n\x10M3COMP_STATE_ERR\x10\x01\x12\x17\n\x13M3COMP_STATE_SAFEOP\x10\x02\x12\x13\n\x0fM3COMP_STATE_OP\x10\x03\x42\x02H\x01')

_M3COMP_STATE = _descriptor.EnumDescriptor(
  name='M3COMP_STATE',
  full_name='M3COMP_STATE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='M3COMP_STATE_INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M3COMP_STATE_ERR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M3COMP_STATE_SAFEOP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M3COMP_STATE_OP', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1337,
  serialized_end=1442,
)

M3COMP_STATE = enum_type_wrapper.EnumTypeWrapper(_M3COMP_STATE)
M3COMP_STATE_INIT = 0
M3COMP_STATE_ERR = 1
M3COMP_STATE_SAFEOP = 2
M3COMP_STATE_OP = 3



_M3STATUSALL = _descriptor.Descriptor(
  name='M3StatusAll',
  full_name='M3StatusAll',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='M3StatusAll.name', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datum', full_name='M3StatusAll.datum', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=24,
  serialized_end=66,
)


_M3COMMANDALL = _descriptor.Descriptor(
  name='M3CommandAll',
  full_name='M3CommandAll',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name_cmd', full_name='M3CommandAll.name_cmd', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name_param', full_name='M3CommandAll.name_param', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datum_cmd', full_name='M3CommandAll.datum_cmd', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datum_param', full_name='M3CommandAll.datum_param', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=68,
  serialized_end=160,
)


_M3STATUSLOGPAGE = _descriptor.Descriptor(
  name='M3StatusLogPage',
  full_name='M3StatusLogPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='M3StatusLogPage.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=162,
  serialized_end=208,
)


_M3BASESTATUS = _descriptor.Descriptor(
  name='M3BaseStatus',
  full_name='M3BaseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='M3BaseStatus.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='M3BaseStatus.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='M3BaseStatus.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rate', full_name='M3BaseStatus.rate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("fast", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='M3BaseStatus.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=211,
  serialized_end=344,
)


_M3ETHERCATSTATUS = _descriptor.Descriptor(
  name='M3EtherCATStatus',
  full_name='M3EtherCATStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_id', full_name='M3EtherCATStatus.network_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='M3EtherCATStatus.serial_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_code', full_name='M3EtherCATStatus.product_code', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active', full_name='M3EtherCATStatus.active', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online', full_name='M3EtherCATStatus.online', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operational', full_name='M3EtherCATStatus.operational', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='al_state', full_name='M3EtherCATStatus.al_state', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pdo_version', full_name='M3EtherCATStatus.pdo_version', index=7,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=347,
  serialized_end=534,
)


_M3MONITORCOMPONENT = _descriptor.Descriptor(
  name='M3MonitorComponent',
  full_name='M3MonitorComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='M3MonitorComponent.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='M3MonitorComponent.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycle_time_status_us', full_name='M3MonitorComponent.cycle_time_status_us', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycle_time_command_us', full_name='M3MonitorComponent.cycle_time_command_us', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=536,
  serialized_end=661,
)


_M3MONITORCOMMAND = _descriptor.Descriptor(
  name='M3MonitorCommand',
  full_name='M3MonitorCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=663,
  serialized_end=681,
)


_M3MONITORPARAM = _descriptor.Descriptor(
  name='M3MonitorParam',
  full_name='M3MonitorParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=683,
  serialized_end=699,
)


_M3MONITORSTATUS = _descriptor.Descriptor(
  name='M3MonitorStatus',
  full_name='M3MonitorStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='M3MonitorStatus.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_components_rt', full_name='M3MonitorStatus.num_components_rt', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_components_ec', full_name='M3MonitorStatus.num_components_ec', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_components', full_name='M3MonitorStatus.num_components', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_components_safeop', full_name='M3MonitorStatus.num_components_safeop', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_components_op', full_name='M3MonitorStatus.num_components_op', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_components_err', full_name='M3MonitorStatus.num_components_err', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operational', full_name='M3MonitorStatus.operational', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycle_time_status_us', full_name='M3MonitorStatus.cycle_time_status_us', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycle_time_command_us', full_name='M3MonitorStatus.cycle_time_command_us', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycle_time_us', full_name='M3MonitorStatus.cycle_time_us', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycle_frequency_hz', full_name='M3MonitorStatus.cycle_frequency_hz', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='components', full_name='M3MonitorStatus.components', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_ethercat_cycles', full_name='M3MonitorStatus.num_ethercat_cycles', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycle_time_max_us', full_name='M3MonitorStatus.cycle_time_max_us', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ec_domains', full_name='M3MonitorStatus.ec_domains', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=702,
  serialized_end=1182,
)


_M3MONITORECDOMAIN = _descriptor.Descriptor(
  name='M3MonitorEcDomain',
  full_name='M3MonitorEcDomain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='t_ecat_wait_rx', full_name='M3MonitorEcDomain.t_ecat_wait_rx', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_ecat_rx', full_name='M3MonitorEcDomain.t_ecat_rx', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_ecat_wait_shm', full_name='M3MonitorEcDomain.t_ecat_wait_shm', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_ecat_shm', full_name='M3MonitorEcDomain.t_ecat_shm', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_ecat_wait_tx', full_name='M3MonitorEcDomain.t_ecat_wait_tx', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_ecat_tx', full_name='M3MonitorEcDomain.t_ecat_tx', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1185,
  serialized_end=1335,
)

_M3STATUSLOGPAGE.fields_by_name['entry'].message_type = _M3STATUSALL
_M3BASESTATUS.fields_by_name['state'].enum_type = _M3COMP_STATE
_M3MONITORCOMPONENT.fields_by_name['state'].enum_type = _M3COMP_STATE
_M3MONITORSTATUS.fields_by_name['base'].message_type = _M3BASESTATUS
_M3MONITORSTATUS.fields_by_name['components'].message_type = _M3MONITORCOMPONENT
_M3MONITORSTATUS.fields_by_name['ec_domains'].message_type = _M3MONITORECDOMAIN
DESCRIPTOR.message_types_by_name['M3StatusAll'] = _M3STATUSALL
DESCRIPTOR.message_types_by_name['M3CommandAll'] = _M3COMMANDALL
DESCRIPTOR.message_types_by_name['M3StatusLogPage'] = _M3STATUSLOGPAGE
DESCRIPTOR.message_types_by_name['M3BaseStatus'] = _M3BASESTATUS
DESCRIPTOR.message_types_by_name['M3EtherCATStatus'] = _M3ETHERCATSTATUS
DESCRIPTOR.message_types_by_name['M3MonitorComponent'] = _M3MONITORCOMPONENT
DESCRIPTOR.message_types_by_name['M3MonitorCommand'] = _M3MONITORCOMMAND
DESCRIPTOR.message_types_by_name['M3MonitorParam'] = _M3MONITORPARAM
DESCRIPTOR.message_types_by_name['M3MonitorStatus'] = _M3MONITORSTATUS
DESCRIPTOR.message_types_by_name['M3MonitorEcDomain'] = _M3MONITORECDOMAIN

class M3StatusAll(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3STATUSALL

  # @@protoc_insertion_point(class_scope:M3StatusAll)

class M3CommandAll(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3COMMANDALL

  # @@protoc_insertion_point(class_scope:M3CommandAll)

class M3StatusLogPage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3STATUSLOGPAGE

  # @@protoc_insertion_point(class_scope:M3StatusLogPage)

class M3BaseStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3BASESTATUS

  # @@protoc_insertion_point(class_scope:M3BaseStatus)

class M3EtherCATStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3ETHERCATSTATUS

  # @@protoc_insertion_point(class_scope:M3EtherCATStatus)

class M3MonitorComponent(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3MONITORCOMPONENT

  # @@protoc_insertion_point(class_scope:M3MonitorComponent)

class M3MonitorCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3MONITORCOMMAND

  # @@protoc_insertion_point(class_scope:M3MonitorCommand)

class M3MonitorParam(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3MONITORPARAM

  # @@protoc_insertion_point(class_scope:M3MonitorParam)

class M3MonitorStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3MONITORSTATUS

  # @@protoc_insertion_point(class_scope:M3MonitorStatus)

class M3MonitorEcDomain(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M3MONITORECDOMAIN

  # @@protoc_insertion_point(class_scope:M3MonitorEcDomain)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\001')
# @@protoc_insertion_point(module_scope)
