class UserClass:

    _cls_str = 'UserClass.user_method'

    def user_method(self, *args, **kwargs):
        print(UserClass._cls_str)


u_cls = UserClass()

u_cls.user_method()  # UserClass.user_method; using instance

UserClass.user_method(u_cls)  # UserClass.user_method; using class name

user_func = UserClass.user_method  # using function
user_func(None)  # UserClass.user_method
