import abc


class CommandBusCmdSerializerInterface(abc.ABC):
    """
    Abstract base class for command bus deserialization / serialization.
    All command bus commands must derive from this class to unify the provided interface
    """

    @abc.abstractmethod
    def deserialize(self, payload):
        """
        :param payload: [bytearray] contains payload of command without CRC that must be deserialized
        :return:
        """
        pass

    @abc.abstractmethod
    def serialize(self):
        """
        Serializes command into bytearray
        :return: [bytearray] serialized command content as bytearray
        """
        pass
