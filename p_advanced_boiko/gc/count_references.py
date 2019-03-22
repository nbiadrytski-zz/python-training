import sys

foo = []
print(sys.getrefcount(foo))  # 2: 1 from foo var and 2 from getrefcount


def bar(a):
    print(sys.getrefcount(a))  # 4: 1 - global foo var, 2 - func arg, 3 - getrefcount, 4 - Python's function stack


bar(foo)
print(sys.getrefcount(foo))  # 2: 1 - global foo var, 2 - getrefcount; func bar() scope is destroyed
