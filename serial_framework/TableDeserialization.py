class TableDeserialization:
    """
    Container for commandbus messages.
    Key: CommandId
    Value: CommandBus Message
    """
    def __init__(self):
        self.table = []

    def add(self, commandBusMessageClass):
        """
        Adds commandBusMessage to table

        Note: commandBusMessage must implement CommandBusCmdSerializerInterface
        :param commandBusMessageClass: Command
        """
        self.table.append(commandBusMessageClass)

    def getEntry(self, cmd, messageIsReply):
        for entry in self.table:
            if (entry.CMDID == cmd) and (entry.MESSAGE_IS_REPLY == messageIsReply):
                return entry
        return None

    def deserialize(self, cmdId, messageIsReply, payload):
        """
        Function tries to find a suitable CmdBUs message for cmdId.
        If CmdBus message is found, deserialize() is called and the object returned.
        In case no suitable cmdbus message is found, NONE is returned
        :param cmdId: commandId that fits to payload
        :param payload: byteArray that contains complete payload of CommandBus Message
        :return: if CmdBus Message for cmdId found: cmdBus message with deserialized payload | None, else
        """
        entry = self.getEntry(cmdId, messageIsReply)
        if entry is not None:
            command = entry()
            command.deserialize(payload)
            return command
        return None
