X = 99  # global


def f1():
    X = 88  # local

    def f2():  # f2 is a local variable within f1’s local scope
        print(X)  # reference made in nested def
    return f2


action = f1()  # action is a func; f1 returned f2
action()
