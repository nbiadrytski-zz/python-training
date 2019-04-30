class Buffer:  # low-level, not something that clients want to work with
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):  # support indexing
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


# low-level, not something that clients want to work with
class Viewport:  # shows a chunk of the buffer on screen somewhere
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[self.offset + index]

    def append(self, text):
        self.buffer += text


class Console:  # facade
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    # high-level
    def write(self, text):
        self.current_viewport.buffer.write(text)

    # low-level
    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
    c = Console()
    c.write('hello')
    ch = c.get_char_at(0)

