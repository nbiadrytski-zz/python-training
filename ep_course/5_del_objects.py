import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(f'{class_name} DESTROYED !!!')


pt1 = Point(378, 499)
pt2 = pt1
pt3 = pt1

print(sys.getrefcount(pt1))  # 4; getrefcount creates additional local ref link to pt1, that's why 4

print(id(pt1), id(pt2), id(pt3))  # 4505950192 4505950192 4505950192
del pt1, pt2, pt3
