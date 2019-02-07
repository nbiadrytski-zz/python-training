class Employee:
    def __init__(self, first_name):
        self.name = first_name

    @property
    def fullname(self):
        return "{} {}".format(self.name, self.name[::-1].capitalize())

    #def fire(self):
    #   print('You are fired!!!')


