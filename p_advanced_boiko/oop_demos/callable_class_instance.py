class UserClass:

    def __init__(self, name):
        self.name = name

    def __call__(self, times):
        print(f'{self.name} called {times} times!')


u_cls = UserClass('Class instance')
u_cls(1)  # Class instance called 1 times!; class instance can be called like a func
