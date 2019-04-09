from pprint import pprint


class UserClass:

    def user_method(self, *args, **kwargs):
        pass


def user_func(*args, **kwargs):
    pass


pprint(set(dir(UserClass.user_method)) - set(dir(user_func)))  # set()
