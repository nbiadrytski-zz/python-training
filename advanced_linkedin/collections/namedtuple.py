import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("MyPoint", "x y")

    print(collections.namedtuple.__doc__)

    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(p1)  # MyPoint(x=10, y=20)
    print(p2)  # MyPoint(x=30, y=40)
    print(p1.x, p1.y)  # 10 20

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)  # MyPoint(x=100, y=20)


if __name__ == "__main__":
    main()