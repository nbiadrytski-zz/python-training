class Manager:
    def __init__(self, name):
        self.name = name

    def view_records(self):
        print('{} is able to view records'.format(self.name))
