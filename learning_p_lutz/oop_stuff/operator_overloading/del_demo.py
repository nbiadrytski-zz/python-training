class Life:

    def __init__(self, name='unknown'):
        print(f'Hello {name}')
        self.name = name

    def live(self):
        print(self.name)

    def __del__(self):
        print(f'Bye {self.name}')


brian = Life('Brian')
brian.live()
brian = 'loretta'  # when brian is assigned a string, we lose the last reference to Life inst and trigger its destructor method
# Hello Brian
# Brian
# Bye Brian