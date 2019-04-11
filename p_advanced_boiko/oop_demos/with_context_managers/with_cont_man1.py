from contextlib import contextmanager, closing


@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')


with tag('h1'):
    print('foo')
# <h1>
# foo
# </h1>


class DbConnection:  # e.g. db connection: open and close.
    def open(self):
        print(f'Opened {self.__class__.__name__}')
        return self

    def close(self):
        print('Ufff... Closed db connection.')


# As my DbConnection class has close method, it will be called anyway
# Even if test() method does not exist
with closing(DbConnection().open()) as db_operation:
    db_operation.test()

# Opened PandoraBox
# AttributeError: 'PandoraBox' object has no attribute 'test'
# Ufff... Closed.

