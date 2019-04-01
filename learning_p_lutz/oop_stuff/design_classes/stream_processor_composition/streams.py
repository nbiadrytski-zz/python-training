class Processor:
    """reader and writer objects are embedded within the class instance (composition),
    and we supply the conversion logic in a subclass rather than passing in a converter function (inheritance)
    """

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):  # defines a converter method that it expects subclasses to fill in
        assert False, 'converter must be defined'

