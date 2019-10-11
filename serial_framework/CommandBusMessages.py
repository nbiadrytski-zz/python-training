# -*- coding: utf-8 -*-
"""CommandBusMessages.py: Serializer / Deserializer all relevant command bus messages"""

from enum import Enum, IntEnum
# import abc

from serial_framework.CommandBusCmdSerializerInterface import CommandBusCmdSerializerInterface
from serial_framework.TableDeserialization import TableDeserialization


class MessageRegistry:
    """
    Class provides standard setup of deserialization tables
    """
    _table = TableDeserialization()

    def registerMessage(messageClass):
        MessageRegistry._table.add(messageClass)

    @staticmethod
    def getDeserializationTable():
        return MessageRegistry._table


class RestartTm(CommandBusCmdSerializerInterface):
    CMDID = 0x15
    MESSAGE_IS_REPLY = False

    def __init__(self):
        pass

    def deserialize(self, payload):
        pass

    def serialize(self):
        return None


MessageRegistry.registerMessage(RestartTm)


class StartDaisyChain(CommandBusCmdSerializerInterface):
    CMDID = 0x11
    MESSAGE_IS_REPLY = False

    def __init__(self):
        pass

    def deserialize(self, payload):
        pass

    def serialize(self):
        return None


MessageRegistry.registerMessage(StartDaisyChain)


class AssignAddress(CommandBusCmdSerializerInterface):
    CMDID = 0x12
    MESSAGE_IS_REPLY = False

    def __init__(self, port=0, adr=0):
        self.port = port
        self.adr = adr

    def deserialize(self, payload):
        self.port = payload[0]
        self.adr = payload[2]

    def serialize(self):
        payload = bytearray()
        payload.append(self.port)
        payload.append(1)  # daisyChain from front to back
        payload.append(self.adr)
        return payload


MessageRegistry.registerMessage(AssignAddress)


class StartFirmware(CommandBusCmdSerializerInterface):
    CMDID = 0x16
    MESSAGE_IS_REPLY = False

    class Image(Enum):
        UNDEFINED_IMAGE = 0xFF
        FIRMWARE_IMAGE = 0x01
        FACTORY_IMAGE = 0xA5

    def __init__(self, imageType=Image.UNDEFINED_IMAGE):
        self.imageType = imageType

    def deserialize(self, payload):
        self.imageType = StartFirmware.Image(payload[0])

    def serialize(self):
        payload = bytearray()
        payload.append(self.imageType.value)
        return payload


MessageRegistry.registerMessage(StartFirmware)


class StartFirmwareReply(CommandBusCmdSerializerInterface):
    CMDID = 0x16
    MESSAGE_IS_REPLY = True

    def __init__(self, success=True):
        self.success = success

    def deserialize(self, payload):
        if payload[0] == 0:
            self.success = True
        else:
            self.success = False

    def serialize(self):
        payload = bytearray()
        if self.success:
            payload.append(0)
        else:
            payload.append(1)
        return payload


MessageRegistry.registerMessage(StartFirmwareReply)


class Ping(CommandBusCmdSerializerInterface):
    CMDID = 0x01
    MESSAGE_IS_REPLY = False

    def __init__(self):
        pass

    def deserialize(self, payload):
        pass

    def serialize(self):
        payLoad = bytearray()
        payLoad.append(0)
        return payLoad


MessageRegistry.registerMessage(Ping)


class PingReply(CommandBusCmdSerializerInterface):
    CMDID = 0x01
    MESSAGE_IS_REPLY = True

    def __init__(self):
        pass

    def deserialize(self, payload):
        pass

    def serialize(self):
        return None


MessageRegistry.registerMessage(PingReply)


class SwitchToNextModule(CommandBusCmdSerializerInterface):
    CMDID = 0x13
    MESSAGE_IS_REPLY = False

    def __init__(self):
        pass

    def deserialize(self, payload):
        pass

    def serialize(self):
        payload = bytearray()
        payload.append(1)  # daisyChain from front to back
        return payload


MessageRegistry.registerMessage(SwitchToNextModule)


class SwitchToNextModuleReply(CommandBusCmdSerializerInterface):
    CMDID = 0x13
    MESSAGE_IS_REPLY = True

    def __init__(self, outputActivated=False, finished=False):
        self.outputActivated = outputActivated
        self.finished = finished

    def deserialize(self, payload):
        self.outputActivated = payload[0]
        self.finished = payload[1]

    def serialize(self):
        payload = bytearray()
        if self.outputActivated:
            payload.append(1)
        else:
            payload.append(0)
        if self.finished:
            payload.append(1)
        else:
            payload.append(0)
        return payload


MessageRegistry.registerMessage(SwitchToNextModuleReply)


class GetPlantConfig(CommandBusCmdSerializerInterface):
    CMDID = 0x03
    MESSAGE_IS_REPLY = False

    def __init__(self):
        pass

    def deserialize(self, payload):
        pass

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # index
        return payload


MessageRegistry.registerMessage(GetPlantConfig)


class ModuleConfig(CommandBusCmdSerializerInterface):
    def __init__(self, bridge=0, port=0, adr=0):
        self.port = port
        self.adr = adr
        self.bridge = bridge

    def deserialize(self, payload):
        self.port = payload[0]
        self.adr = payload[1]
        self.bridge = payload[2]

    def serialize(self):
        payload = bytearray()
        payload.append(self.port)
        payload.append(self.adr)
        payload.append(self.bridge)
        return payload


class GetPlantConfigReply(CommandBusCmdSerializerInterface):
    CMDID = 0x03
    MESSAGE_IS_REPLY = True

    def __init__(self, finished=False, bridge=0, northModule=None, eastModule=None, southModule=None, westModule=None):
        self.finished = finished
        self.ownModule = ModuleConfig()
        self.ownModule.bridge = bridge
        if northModule is None:
            northModule = ModuleConfig()
        if eastModule is None:
            eastModule = ModuleConfig()
        if southModule is None:
            southModule = ModuleConfig()
        if westModule is None:
            westModule = ModuleConfig()
        self.neighbours = [northModule, eastModule, southModule, westModule]

    def deserialize(self, payload):
        if payload is not None:
            self.finished = True
            if payload[0] == 255:
                self.finished = False
            if self.finished:
                self.ownModule.bridge = payload[1]
                for i in range(0, 4):
                    self.neighbours[i].deserialize(payload[(2 + 3 * i):(2 + 3 * (i + 1))])

    def serialize(self):
        payload = bytearray()
        if self.finished:
            payload.append(1)
        else:
            payload.append(255)
        payload.append(self.ownModule.bridge)
        for i in range(0, 4):
            payload.extend(self.neighbours[i].serialize())
        return payload


MessageRegistry.registerMessage(GetPlantConfigReply)


class TransparentMessage(CommandBusCmdSerializerInterface):
    CMDID = 0x41
    MESSAGE_IS_REPLY = False

    _table = TableDeserialization()

    def registerCommand(cmdClass):
        TransparentMessage._table.add(cmdClass)

    def __init__(self, cmd=0, data=bytearray()):
        self.cmd = cmd
        self.data = data

    def deserialize(self, payload):
        self.cmd = payload[0]
        _len = len(payload)
        self.data = payload[1:_len]
        self.commandObject = TransparentMessage._table.deserialize(self.cmd, TransparentMessage.MESSAGE_IS_REPLY,
                                                                   self.data)

    def serialize(self):
        payload = bytearray()
        payload.append(self.cmd)
        for x in range(0, len(self.data)):
            payload.append(int(self.data[x]))
        return payload


MessageRegistry.registerMessage(TransparentMessage)


class TransparentMessageReply(CommandBusCmdSerializerInterface):
    CMDID = 0x41
    MESSAGE_IS_REPLY = True

    _table = TableDeserialization()

    def registerCommand(cmdClass):
        TransparentMessageReply._table.add(cmdClass)

    def __init__(self, cmd=0, data=bytearray()):
        self.cmd = cmd
        self.data = data
        self.commandObject = None

    def deserialize(self, payload):
        self.cmd = payload[0]
        _len = len(payload)
        self.data = payload[1:_len]
        self.commandObject = TransparentMessageReply._table.deserialize(self.cmd,
                                                                        TransparentMessageReply.MESSAGE_IS_REPLY,
                                                                        self.data)

    def serialize(self):
        payload = bytearray()
        payload.append(self.cmd)
        for x in range(0, len(self.data)):
            payload.append(int(self.data[x]))
        return payload


MessageRegistry.registerMessage(TransparentMessageReply)


########################################
# DebugData
########################################


class DebugData(CommandBusCmdSerializerInterface):
    CMDID = 0x01  # transparent message sub command
    MESSAGE_IS_REPLY = False

    def __init__(self, dataType=0, dataCmd=0, dataAddr=0):
        self.dataType = dataType
        self.dataCmd = dataCmd
        self.dataAddr = dataAddr

    def deserialize(self, payload):
        self.dataType = payload[0]
        self.dataCmd = payload[1]
        self.dataAddr = 0x0FF & payload[2]
        self.dataAddr = self.dataAddr | (0x0FF00 & (payload[3] << 8))
        self.dataAddr = self.dataAddr | (0x0FF0000 & (payload[4] << 16))
        self.dataAddr = self.dataAddr | (0x0FF000000 & (payload[5] << 24))

    def serialize(self):
        payload = bytearray()
        payload.append(self.dataType)
        payload.append(self.dataCmd)
        payload.append(0x0FF & self.dataAddr)
        payload.append(0x0FF & (self.dataAddr >> 8))
        payload.append(0x0FF & (self.dataAddr >> 16))
        payload.append(0x0FF & (self.dataAddr >> 24))
        return payload


TransparentMessage.registerCommand(DebugData)


class DebugDataReply(CommandBusCmdSerializerInterface):
    CMDID = 0x01  # transparent message sub command
    MESSAGE_IS_REPLY = True

    _table = TableDeserialization()

    def registerCommand(cmdClass):
        DebugDataReply._table.add(cmdClass)

    def __init__(self, dataType=0, dataCmd=0, dataAddr=0, dataStatus=0, data=bytearray()):
        self.dataType = dataType
        self.dataCmd = dataCmd
        self.dataAddr = dataAddr
        self.dataStatus = dataStatus
        self.data = bytearray()
        self.data = data
        self.commandObject = None

    def deserialize(self, payload):
        self.dataType = payload[0]
        self.dataCmd = payload[1]
        self.dataAddr = 0x0FF & payload[2]
        self.dataAddr = self.dataAddr | (0x0FF00 & (payload[3] << 8))
        self.dataAddr = self.dataAddr | (0x0FF0000 & (payload[4] << 16))
        self.dataAddr = self.dataAddr | (0x0FF000000 & (payload[5] << 24))
        self.dataStatus = payload[6]
        _len = len(payload)
        self.data = payload[7:_len]
        if (self.dataCmd == 0x00):  # read
            self.commandObject = DebugDataReply._table.deserialize(self.dataType, DebugDataReply.MESSAGE_IS_REPLY,
                                                                   self.data)

    def serialize(self):
        payload = bytearray()
        payload.append(self.dataType)
        payload.append(self.dataCmd)
        payload.append(0x0FF & self.dataAddr)
        payload.append(0x0FF & (self.dataAddr >> 8))
        payload.append(0x0FF & (self.dataAddr >> 16))
        payload.append(0x0FF & (self.dataAddr >> 24))
        payload.append(self.dataStatus)
        for x in range(0, len(self.data)):
            payload.append(int(self.data[x]))
        return payload


TransparentMessageReply.registerCommand(DebugDataReply)


########################################
# TraceRecord
########################################


class TraceRecord(CommandBusCmdSerializerInterface):
    def __init__(self, trcId=0, v0=0, v1=0, v2=0):
        self.trcId = trcId
        self.val = [0, 0, 0]
        self.val[0] = v0
        self.val[1] = v1
        self.val[2] = v2

    def deserialize(self, payload):
        self.trcId = 0x0FF & payload[0]
        self.trcId = self.trcId | (0x0FF00 & payload[1] << 8)
        dPtr = 2
        for x in range(0, 3):
            self.val[x] = 0x0FF & payload[dPtr]
            self.val[x] = self.val[x] | (0x0FF00 & (payload[dPtr + 1] << 8))
            self.val[x] = self.val[x] | (0x0FF0000 & (payload[dPtr + 2] << 16))
            self.val[x] = self.val[x] | (0x0FF000000 & (payload[dPtr + 3] << 24))
            dPtr = dPtr + 4

    def serialize(self):
        payload = bytearray()
        payload.append(0x0FF & self.trcId)
        payload.append(0x0FF & (self.trcId >> 8))
        for x in range(0, 3):
            payload.append(0x0FF & self.val[x])
            payload.append(0x0FF & (self.val[x] >> 8))
            payload.append(0x0FF & (self.val[x] >> 16))
            payload.append(0x0FF & (self.val[x] >> 24))
        return payload


class TraceRecords(CommandBusCmdSerializerInterface):
    CMDID = 0x01  # debuf data sub command
    MESSAGE_IS_REPLY = True

    def __init__(self, data=None):
        if data is None:
            data = []
        self.records = data

    def clearRecords(self):
        self.records.clear()

    def addRecord(self, trcRecord):
        self.records.append(trcRecord)

    def deserialize(self, payload):
        dataLen = len(payload)
        _len = int(dataLen / 14)
        for x in range(0, _len):
            dataPtr = x * 14
            _rawRecord = payload[dataPtr:(dataPtr + 14)]
            trcRecord = TraceRecord()
            trcRecord.deserialize(_rawRecord)
            self.records.append(trcRecord)

    def serialize(self):
        payload = bytearray()
        for x in range(0, len(self.records)):
            _raw = self.records[x].serialize()
            payload.append(_raw)
        return payload


DebugDataReply.registerCommand(TraceRecords)


class LdcValues(CommandBusCmdSerializerInterface):
    CMDID = 0x03  # debuf data sub command
    MESSAGE_IS_REPLY = True

    FIELD_SIZE_X = 6
    FIELD_SIZE_Y = 6

    def _initialize_fields(self):
        def_val = 0
        init_field = [[def_val for y in range(LdcValues.FIELD_SIZE_Y)] for x in range(LdcValues.FIELD_SIZE_X)]
        return init_field

    def __init__(self, ldcValues=None):
        self.ldcValues = None
        if ldcValues is None:
            ldcValues = LdcValues._initialize_fields()
        self.ldcValues = ldcValues

    def deserialize(self, payload):
        dataLen = len(payload)
        _len = int(dataLen / 2)
        assert (_len == 36)
        for i in range(0, _len):
            ldcValue = int(0x0FF & payload[i * 2]) + int(0x0FF00 & (payload[i * 2 + 1] << 8))
            x = i % 6
            y = i // 6
            self.ldcValues[x][y] = ldcValue

    def serialize(self):
        payload = bytearray()
        for x in range(0, 6):
            for y in range(0, 6):
                ldcValue = self.ldcValues[x][y]
                payload.append(ldcValue & 0xff)
                payload.append((ldcValue >> 8) & 0xff)
        return payload


DebugDataReply.registerCommand(LdcValues)


class MaxLdcValues(LdcValues):
    CMDID = 0x04  # debuf data sub command
    MESSAGE_IS_REPLY = True

    def __init__(self, ldcValues=None):
        super().__init__(ldcValues)


DebugDataReply.registerCommand(MaxLdcValues)


####################################################################


class MicroCommandsBase(CommandBusCmdSerializerInterface):
    _table = TableDeserialization()

    def registerMessage(messageClass):
        MicroCommandsBase._table.add(messageClass)

    def __init__(self, messageIsReply):
        self.microCommands = []
        self.payloadLength = 0
        self.messageIsReply = messageIsReply

    def deserialize(self, payload):
        if payload is not None:
            index = 0
            while index < len(payload):
                cmd = payload[index + 1]
                length = payload[index + 2]
                indexEnd = index + 3 + length
                microCommandPayload = payload[index:indexEnd]
                microCmd = MicroCommandsBase._table.deserialize(cmd, self.messageIsReply, microCommandPayload)
                if (microCmd is not None):
                    self.microCommands.append(microCmd)
                index = indexEnd

    def serialize(self):
        payload = bytearray()
        for microCmd in self.microCommands:
            payload.extend(microCmd.serialize())
        return payload


class MicroCommands(MicroCommandsBase):
    CMDID = 0x10
    MESSAGE_IS_REPLY = False

    def __init__(self):
        super().__init__(MicroCommands.MESSAGE_IS_REPLY)

    def addMicroCommand(self, microCmd):
        newLength = self.payloadLength + 3 + microCmd.LENGTH
        if (newLength <= 240):
            self.microCommands.append(microCmd)
            self.payloadLength = newLength
            return True
        return False


MessageRegistry.registerMessage(MicroCommands)


class MicroCommandsReply(MicroCommandsBase):
    CMDID = 0x10
    MESSAGE_IS_REPLY = True

    def __init__(self):
        super().__init__(MicroCommandsReply.MESSAGE_IS_REPLY)


MessageRegistry.registerMessage(MicroCommandsReply)


#################################################
# MicroCommands
#################################################


# micro commands need the following prefix in the class name: 'MicroCmd'

class MicroCmdFieldStatus(CommandBusCmdSerializerInterface):
    CMDID = 0x01
    MESSAGE_IS_REPLY = False
    LENGTH = 0

    def __init__(self):
        pass

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdFieldStatus.CMDID)
        payload.append(MicroCmdFieldStatus.LENGTH)
        return payload


MicroCommandsBase.registerMessage(MicroCmdFieldStatus)


class LogicalPositionStatus(IntEnum):
    FREE = 0
    OCCUPIED = 1
    PARTIALLY_OCCUPIED = 2
    ERROR_ON_LOGICAL_POSITION = 3


class MicroCmdFieldStatusReply(CommandBusCmdSerializerInterface):
    """
    Field status is accessible through 'fields' attribute.
    In order to access the position use the following semantic:
    reply.fields[x][y] = status
    """
    CMDID = 0x01
    LENGTH = 36
    MESSAGE_IS_REPLY = True

    FIELD_SIZE_X = 6
    FIELD_SIZE_Y = 6

    def _initialize_fields(self):
        # by default whole filed is initialized as ERROR
        def_val = LogicalPositionStatus.ERROR_ON_LOGICAL_POSITION
        init_field = [[def_val for y in range(self.FIELD_SIZE_Y)] for x in range(self.FIELD_SIZE_X)]
        return init_field

    def __init__(self, _fields=None):
        # the command object should be default-constructible,
        # therefore _fields by default None
        # with additional checks

        if _fields is None:
            self.fields = self._initialize_fields()
            return

        assert len(_fields) == self.FIELD_SIZE_X

        def assert_column(field_column): assert len(field_column) == self.FIELD_SIZE_Y

        [assert_column(field_column) for field_column in _fields]

        self.fields = _fields

    def _validate_status(self, field_value):
        valid = (field_value == LogicalPositionStatus.FREE)
        valid = valid or (field_value == LogicalPositionStatus.OCCUPIED)
        valid = valid or (field_value == LogicalPositionStatus.PARTIALLY_OCCUPIED)

        if (not valid):
            return LogicalPositionStatus.ERROR_ON_LOGICAL_POSITION

        return field_value

    def _convert_idx_to_coords(selfself, idx):
        pos_x = idx % 6
        pos_y = idx // 6

        return pos_x, pos_y

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]
        for i in range(0, self.LENGTH):
            field = payload[3 + i]
            (pos_x, pos_y) = self._convert_idx_to_coords(i)
            self.fields[pos_x][pos_y] = self._validate_status(field)

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdFieldStatusReply.CMDID)
        payload.append(MicroCmdFieldStatusReply.LENGTH)
        for i in range(0, MicroCmdFieldStatusReply.LENGTH):
            (pos_x, pos_y) = self._convert_idx_to_coords(i)
            payload.append(self.fields[pos_x][pos_y])

        return payload


MicroCommandsBase.registerMessage(MicroCmdFieldStatusReply)

WEAR_UNDEFINED = 15
DIRECTION_TOP = 0
DIRECTION_RIGHT = 1
DIRECTION_BOTTOM = 2
DIRECTION_LEFT = 3


class MicroCmdMove(CommandBusCmdSerializerInterface):
    CMDID = 0x02
    MESSAGE_IS_REPLY = False
    LENGTH = 5

    def __init__(self, driveId=0, x=0, y=0, direction=0, length=0, wear=WEAR_UNDEFINED, mode=0):
        self.driveId = driveId
        self.x = x
        self.y = y
        self.direction = direction
        self.length = length
        self.wear = wear
        self.mode = mode

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]
        self.driveId = payload[3]
        self.driveId |= payload[4] << 8
        self.x = (payload[5] & 0x07)
        self.y = ((payload[5] >> 3) & 0x07)
        self.direction = ((payload[5] >> 6) & 0x03)
        self.length = payload[6]
        self.wear = (payload[7] >> 4) & 0x0f
        self.mode = payload[7] & 0x0f

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdMove.CMDID)
        payload.append(MicroCmdMove.LENGTH)
        payload.append(self.driveId & 0xff)
        payload.append((self.driveId >> 8) & 0xff)
        payload.append(((self.direction & 0x03) << 6) | ((self.y & 0x07) << 3) | (self.x & 0x07))
        payload.append(self.length)
        payload.append(((self.wear & 0x0f) << 4) | (self.mode & 0x0f))
        return payload


MicroCommandsBase.registerMessage(MicroCmdMove)


class MicroCmdMoveEnd(CommandBusCmdSerializerInterface):
    CMDID = 0x02
    MESSAGE_IS_REPLY = True
    LENGTH = 4

    def __init__(self, driveId=0, x=0, y=0, err=0, wear=WEAR_UNDEFINED):
        self.driveId = driveId
        self.x = x
        self.y = y
        self.err = err
        self.wear = wear

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]
        self.driveId = payload[3]
        self.driveId |= payload[4] << 8
        self.x = (payload[5] & 0x07)
        self.y = ((payload[5] >> 3) & 0x07)
        errorFlag = payload[6]
        self.err = errorFlag & 0x0f
        if (self.err == 0):
            self.wear = (errorFlag >> 4) & 0x0f
        else:
            self.wear = WEAR_UNDEFINED
            self.err = errorFlag

    def serialize(self):
        payload = bytearray()
        errorFlag = 0
        if (self.err == 0):
            errorFlag = (self.wear & 0x0f) << 4
        else:
            errorFlag = self.err

        payload.append(0)  # subadr
        payload.append(MicroCmdMoveEnd.CMDID)
        payload.append(MicroCmdMoveEnd.LENGTH)
        payload.append(self.driveId & 0xff)
        payload.append((self.driveId >> 8) & 0xff)
        payload.append(((self.y & 0x07) << 3) | (self.x & 0x07))
        payload.append(errorFlag)
        return payload


MicroCommandsBase.registerMessage(MicroCmdMoveEnd)


class MicroCmdMoveStatus(CommandBusCmdSerializerInterface):
    CMDID = 0x03
    MESSAGE_IS_REPLY = True
    LENGTH = 3

    def __init__(self, driveId=0, x=0, y=0):
        self.driveId = driveId
        self.x = x
        self.y = y

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]
        self.driveId = payload[3]
        self.driveId |= payload[4] << 8
        self.x = (payload[5] & 0x07)
        self.y = ((payload[5] >> 3) & 0x07)

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdMoveStatus.CMDID)
        payload.append(MicroCmdMoveStatus.LENGTH)
        payload.append(self.driveId & 0xff)
        payload.append((self.driveId >> 8) & 0xff)
        payload.append(((self.y & 0x07) << 3) | (self.x & 0x07))
        return payload


MicroCommandsBase.registerMessage(MicroCmdMoveStatus)


class MicroCmdTshAlignment(CommandBusCmdSerializerInterface):
    CMDID = 0x12
    MESSAGE_IS_REPLY = False
    LENGTH = 0

    def __init__(self):
        pass

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdTshAlignment.CMDID)
        payload.append(MicroCmdTshAlignment.LENGTH)
        return payload


MicroCommandsBase.registerMessage(MicroCmdTshAlignment)


class MicroCmdTshAlignmentReply(CommandBusCmdSerializerInterface):
    CMDID = 0x12
    MESSAGE_IS_REPLY = True
    LENGTH = 2

    def __init__(self, status=0, numberOfTSHs=0):
        self.status = status
        self.numberOfTSHs = numberOfTSHs

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]
        self.status = payload[3]
        self.numberOfTSHs = payload[4]

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdTshAlignmentReply.CMDID)
        payload.append(MicroCmdTshAlignmentReply.LENGTH)
        payload.append(self.status)
        payload.append(self.numberOfTSHs)
        return payload


MicroCommandsBase.registerMessage(MicroCmdTshAlignmentReply)


class MicroCmdSetModuleStatus(CommandBusCmdSerializerInterface):
    CMDID = 0x13
    MESSAGE_IS_REPLY = False
    LENGTH = 1

    def __init__(self, moduleState=0):
        self.moduleState = moduleState

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]
        self.moduleState = payload[3]

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdSetModuleStatus.CMDID)
        payload.append(MicroCmdSetModuleStatus.LENGTH)
        payload.append(self.moduleState)
        return payload


MicroCommandsBase.registerMessage(MicroCmdSetModuleStatus)


class MicroCmdModuleStatusChanged(CommandBusCmdSerializerInterface):
    CMDID = 0x13
    MESSAGE_IS_REPLY = True
    LENGTH = 2

    def __init__(self, currentState=0, stateChangeResult=0):
        self.currentState = currentState
        self.stateChangeResult = stateChangeResult

    def deserialize(self, payload):
        microcmdid = payload[1]
        length = payload[2]
        self.currentState = payload[3]
        self.stateChangeResult = payload[4]

    def serialize(self):
        payload = bytearray()
        payload.append(0)  # subadr
        payload.append(MicroCmdModuleStatusChanged.CMDID)
        payload.append(MicroCmdModuleStatusChanged.LENGTH)
        payload.append(self.currentState)
        payload.append(self.stateChangeResult)
        return payload


MicroCommandsBase.registerMessage(MicroCmdModuleStatusChanged)
