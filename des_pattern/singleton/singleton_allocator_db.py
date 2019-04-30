import random


class Database:
    _instance = None

    def __init__(self):
        self.id = random.randint(1,101)
        print('Generated an id of ', self.id)
        print('Loading database from file')
        pass

    def __new__(cls, *args, **kwargs):  # allocator; check whether or not static instance has been created
        if not cls._instance:  # means instance hasn't been initialised yet
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)  # set hte instance
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1 == d2)  # True

# Initialiser is still being called twice:
# Generated an id of  82
# Loading database from file
# Generated an id of  20
# Loading database from file
# True
