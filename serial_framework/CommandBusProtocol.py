from serial_framework.CommandBusHeader import CommandBusHeader

from twisted.internet.task import LoopingCall


class CommandBusMessage:
    """
    Container for single command bus protocol messages consisting of:
     * Address
     * CMDId
     * object reference of CmdBus Message
     * cmdBus message as byte stream
    """

    def __init__(self, adr, obj, bridgeId=0, portId=0):
        self.connectionId = ''
        self.bridgeId = bridgeId
        self.portId = portId
        self.adr = adr
        self.cmd = obj.__class__.CMDID
        self.obj = obj
        self.header = None
        self.message = None
        self.retries = 0


class CommandBusProtocol:
    """
    CommandBusProtocol class is the glue between CmdBus Header and messages.
    It contains the instance of (de)serialization table
    It also keeps track of mapping between send/received messages and its corresponding timeout.
    Concrete: it rejects sending of new message as long as it waits for an reply of a former message
    """

    TIMOUT_REPLY = 10  # 100ms

    def __init__(self, tableDeserialization, roleMaster):
        """

        :param commandBusProtocolHeader: must implement interface: tsCmdBusDevLib::CommandBusHeaderInterface
        :param tableDeserialization:
        """
        self.roleMaster = roleMaster
        self.timeoutCounter = -1
        self.tableDeserialization = tableDeserialization
        self.toggleBit = []
        for i in range(0, 256):
            self.toggleBit.append(False)
        self.receiveBuffer = []
        self.loopingCall = LoopingCall(self._timerInterval)
        self.loopingCall.start(0.010)

    def _timerInterval(self):
        if self.timeoutCounter >= 0:
            self.timeoutCounter += 1
            if self.timeoutCounter >= CommandBusProtocol.TIMOUT_REPLY:
                self.stopTimerInterval()
                self.receiveBuffer.clear()
                print('CommandBusProtocol: receive timeout')

    def startTimerInterval(self):
        self.timeoutCounter = 0

    def stopTimerInterval(self):
        self.timeoutCounter = -1

    def deserializeData(self, data):
        if self.timeoutCounter == -1:
            self.startTimerInterval()
        self.receiveBuffer.extend(data)
        header = CommandBusHeader()
        messageComplete = header.deserialize(self.receiveBuffer)
        if (messageComplete):
            if header.crcOk:
                self.receiveBuffer.clear()
                self.stopTimerInterval()
                obj = self.tableDeserialization.deserialize(header.cmdid, header.messageIsReply, header.payload)
                if obj is not None:
                    messageObject = CommandBusMessage(header.adr, obj)
                    messageObject.connectionId = self.connectionId
                    messageObject.bridgeId = self.bridgeId
                    messageObject.portId = self.portId
                    messageObject.header = header
                    return messageObject
                else:
                    #print('Deserialization of cmd/reply ' + str(messageObject.cmd) + ' not found!')
                    return None
            else:
                self.stopTimerInterval()
                self.receiveBuffer.clear()
                print('wrong crc received ' + self.connectionId)

    def serializeMessage(self, messageObject):
        if (messageObject.message is None):
            buffer = CommandBusHeader.serialize(messageObject.adr, self.toggleBit[messageObject.adr], not self.roleMaster, messageObject.cmd, messageObject.obj.serialize())
            messageObject.message = buffer
            if self.toggleBit[messageObject.adr]:
                self.toggleBit[messageObject.adr] = False
            else:
                self.toggleBit[messageObject.adr] = True
        return messageObject.message