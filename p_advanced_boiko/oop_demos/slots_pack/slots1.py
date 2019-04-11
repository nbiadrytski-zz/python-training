class Point:
    # each object has a__dict__ where keys are attributes names and values are attributes values
    # BUT Point object has no __dict__ here
    __slots__ = ['x', 'y']


point = Point()
# print(point.__dict__)  # AttributeError: 'Point' object has no attribute '__dict__'
print(dir(Point))

point.x = 10  # descriptor is created for x. and then called __get__()
point.y = 20
print(point)

# Since there is no dict, new attributes cannot be added
# point.z = 30  # AttributeError: 'Point' object has no attribute 'z'


