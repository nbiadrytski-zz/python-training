def singleton(class_):  # decorator
    instances = {}  # keep class instances in dictionary

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)  # add that class to instances dict
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':  # Initialiser is now called just once
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

# Loading database
# True
