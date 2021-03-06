# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ur_msgs/SetIORequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetIORequest(genpy.Message):
  _md5sum = "8e9d2a7211150d4126b8813c554cb6ed"
  _type = "ur_msgs/SetIORequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Service allows setting digital (DIO) and analog (AIO) IO, as well as flags
# and configuring tool voltage.
#
# This service has three request fields (see below).
#
# When setting DIO or AIO pins to new values:
#
#  fun    The function to perform
#  pin    Numeric ID of the pin to set, see constants definition below
#  state  Desired pin state (signal level for analog or STATE_(ON|OFF) for DIO and flags)
#
# When configuring tool voltage:
#
#  fun    Set to FUN_SET_TOOL_VOLTAGE
#  pin    Ignored
#  state  Desired tool voltage (use STATE_TOOL_VOLTAGE constants)

# constants
# pin mapping
# analog out
int8 PIN_AOUT0 = 0
int8 PIN_AOUT1 = 1

# digital out
int8 PIN_DOUT0 = 0
int8 PIN_DOUT1 = 1
int8 PIN_DOUT2 = 2
int8 PIN_DOUT3 = 3
int8 PIN_DOUT4 = 4
int8 PIN_DOUT5 = 5
int8 PIN_DOUT6 = 6
int8 PIN_DOUT7 = 7

# configurable out
int8 PIN_CONF_OUT0 = 8
int8 PIN_CONF_OUT1 = 9
int8 PIN_CONF_OUT2 = 10
int8 PIN_CONF_OUT3 = 11
int8 PIN_CONF_OUT4 = 12
int8 PIN_CONF_OUT5 = 13
int8 PIN_CONF_OUT6 = 14
int8 PIN_CONF_OUT7 = 15

# digital tool output
int8 PIN_TOOL_DOUT0 = 16
int8 PIN_TOOL_DOUT1 = 17

# valid function values
#
# Note: 'fun' is short for 'function' (ie: the function the service should perform).
int8 FUN_SET_DIGITAL_OUT = 1
int8 FUN_SET_FLAG = 2
int8 FUN_SET_ANALOG_OUT = 3
int8 FUN_SET_TOOL_VOLTAGE = 4

# valid values for 'state' when setting digital IO or flags
int8 STATE_OFF = 0
int8 STATE_ON = 1

# valid 'state' values when setting tool voltage
int8 STATE_TOOL_VOLTAGE_0V = 0
int8 STATE_TOOL_VOLTAGE_12V = 12
int8 STATE_TOOL_VOLTAGE_24V = 24

# request fields
int8 fun
int8 pin
float32 state
"""
  # Pseudo-constants
  PIN_AOUT0 = 0
  PIN_AOUT1 = 1
  PIN_DOUT0 = 0
  PIN_DOUT1 = 1
  PIN_DOUT2 = 2
  PIN_DOUT3 = 3
  PIN_DOUT4 = 4
  PIN_DOUT5 = 5
  PIN_DOUT6 = 6
  PIN_DOUT7 = 7
  PIN_CONF_OUT0 = 8
  PIN_CONF_OUT1 = 9
  PIN_CONF_OUT2 = 10
  PIN_CONF_OUT3 = 11
  PIN_CONF_OUT4 = 12
  PIN_CONF_OUT5 = 13
  PIN_CONF_OUT6 = 14
  PIN_CONF_OUT7 = 15
  PIN_TOOL_DOUT0 = 16
  PIN_TOOL_DOUT1 = 17
  FUN_SET_DIGITAL_OUT = 1
  FUN_SET_FLAG = 2
  FUN_SET_ANALOG_OUT = 3
  FUN_SET_TOOL_VOLTAGE = 4
  STATE_OFF = 0
  STATE_ON = 1
  STATE_TOOL_VOLTAGE_0V = 0
  STATE_TOOL_VOLTAGE_12V = 12
  STATE_TOOL_VOLTAGE_24V = 24

  __slots__ = ['fun','pin','state']
  _slot_types = ['int8','int8','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       fun,pin,state

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetIORequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.fun is None:
        self.fun = 0
      if self.pin is None:
        self.pin = 0
      if self.state is None:
        self.state = 0.
    else:
      self.fun = 0
      self.pin = 0
      self.state = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2bf().pack(_x.fun, _x.pin, _x.state))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.fun, _x.pin, _x.state,) = _get_struct_2bf().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2bf().pack(_x.fun, _x.pin, _x.state))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.fun, _x.pin, _x.state,) = _get_struct_2bf().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2bf = None
def _get_struct_2bf():
    global _struct_2bf
    if _struct_2bf is None:
        _struct_2bf = struct.Struct("<2bf")
    return _struct_2bf
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ur_msgs/SetIOResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetIOResponse(genpy.Message):
  _md5sum = "358e233cde0c8a8bcfea4ce193f8fc15"
  _type = "ur_msgs/SetIOResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool success

"""
  __slots__ = ['success']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetIOResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
    else:
      self.success = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.success
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.success
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SetIO(object):
  _type          = 'ur_msgs/SetIO'
  _md5sum = 'f539fc0b1a42859fb186a5aaba22d4b0'
  _request_class  = SetIORequest
  _response_class = SetIOResponse
