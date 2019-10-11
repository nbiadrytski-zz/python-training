from serial_framework.CommandBusProtocol import *
from serial_framework.helpers import debug_dump_hex

from twisted.internet import reactor, protocol, serialport


class CommandBusSlaveProtocol(CommandBusProtocol, protocol.Protocol):
    """
    Represents CommandBus slave implementation.
    Is responsible for receiving requests and sending replies
    A slave specific thing is implemented:
      - CommandBusSlave detects a repeated request from master (information kept in self.last_headers)
      - and CommandBusSlave repeats the last reply in case of a repeated request (information kept in self.last_sent_messages).
    """

    def __init__(self, connectionId, tableDeserialization, callback):
        self.connectionId = connectionId
        super().__init__(tableDeserialization, False)  # False = Slave
        self.callback = callback
        self.last_headers = []
        for i in range(0, 256):
            self.last_headers.append(None)
        self.last_sent_messages = []
        for i in range(0, 256):
            self.last_sent_messages.append(None)

    def sendMessage(self, messageObject):
        self.last_sent_messages[messageObject.adr] = messageObject
        reactor.callFromThread(self.sendMessageInternal, messageObject)

    def sendMessageInternal(self, messageObject):
        if messageObject.adr != 0xff:
            msgToSend = self.serializeMessage(messageObject)
            debug_dump_hex('=== SEND s: ', msgToSend, '\n')
            self.transport.write(msgToSend)

    def dataReceived(self, data):
        # waiting for: CommandBusProtocolMessage
        messageObject =  self.deserializeData(data)
        if messageObject != None:
            debug_dump_hex('=== RECV: ', data, '\n')
            lastHeader = self.last_headers[messageObject.adr]
            lastSentMessage = self.last_sent_messages[messageObject.adr]
            if lastHeader and lastSentMessage and (lastHeader.crc == messageObject.header.crc) and (lastHeader.cmd == messageObject.header.cmd):
                # retry: resend last message
                self.sendMessage(lastSentMessage)
            else:
                # no retry: store new header and remove last message
                self.last_headers[messageObject.adr] = messageObject.header
                self.last_sent_messages[messageObject.adr] = None
                if self.callback:
                    self.callback.messageReceived(self, messageObject)
        else:
            # Message not fully received yet
            pass

    def connectionMade(self):
        if self.callback:
            self.callback.connectionMade(self)

    def connectionLost(self, reason):
        if self.callback:
            self.callback.connectionLost(self, reason)


class CommandBusSlave:
    """
    Represents service provider that acts with twisted framework
    """

    def __init__(self, tableDeserialization, protocolClass=CommandBusSlaveProtocol):
        """
        :param tableDeserialization:
        :param protocolClass:
        """
        self._services = []
        self._connections = {}
        self._tableDeserialization = tableDeserialization
        self._protocolClass = protocolClass

    def registerService(self, service):
        self._services.append(service)

    def getConnection(self, connectionId):
        if connectionId in self._connections:
            return self._connections[connectionId]
        else:
            return None

    def getConnectionByIds(self, bridgeId, portId):
        for connectionId in self._connections:
            connection = self._connections[connectionId]
            if (connection.bridgeId == bridgeId and
                connection.portId == portId):
                return connection
        return None

    def connect(self, connectionId, port, baudrate):
        protocol = self._protocolClass(connectionId, self._tableDeserialization, self)
        sp = serialport.SerialPort(protocol, port, reactor, baudrate)
        self._connections[connectionId] = protocol
        return protocol

    def sendMessage(self, connectionId, messageObject):
        connection = self.getConnection(connectionId)
        if connection != None:
            connection.sendMessage(messageObject)
        else:
            print('connection ' + connectionId + ' not found.')

    def messageReceived(self, connection, messageObject):
        for service in self._services:
            funcName = messageObject.obj.__class__.__name__
            func = getattr(service, funcName, None)
            if not func:
                func = getattr(service, 'all', None)
            if callable(func):
                func(connection, messageObject)
                found = True
            else:
                print('Function not found: ' + funcName)

    def connectionMade(self, connection):
        for service in self._services:
            service.connectionMade(connection, None)

    def connectionLost(self, connection, reason):
        for service in self._services:
            service.connectionLost(connection, reason)

    def start(self):
        pass

    def stop(self):
        pass


if __name__ == '__main__':

    from serial_framework.CommandBusMessages import *

    tableDeserialization = MessageRegistry.getDeserializationTable()


    class MyService:
        def __init__(self):
            pass

        def connectionMade(self, connection, dummy):
            print('connectionMade')

        def connectionLost(self, connection, reason):
            print('connectionLost')

        def all(self, connection, params):
            obj = params.obj
            objClass = obj.__class__
            print('MyService receive adr: ' + str(params.adr) + ' obj: ' + objClass.__name__)

        def Ping(self, connection, params):
            print('MyService receive adr: ' + str(params.adr) + ' PingReply')
            connection.sendMessage(CommandBusMessage(params.adr, PingReply()))


    myService = MyService()
    commandbus = CommandBusSlave(tableDeserialization)
    commandbus.registerService(myService)
    commandbus.connect('myconn1', '/dev/master', 921600)
    #    commandbus.sendMessage('myconn1', CommandBusMessage(1, SwitchToNextModule()))
    #    commandbus.sendMessage('myconn1', CommandBusMessage(1, Ping()))

    commandbus.start()
    reactor.run()