class UserClass:
    def __new__(cls):
        print('__new__')
        return super(UserClass, cls).__new__(cls)

    def __init__(self):
        print('__init__')


u_cls = UserClass()

# __new__
# __init__
