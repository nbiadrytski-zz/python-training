import sys

number = 1
print(sys.getrefcount(number))  # 791

# python caches int objects from -5 to 255

number2 = 3000
print(sys.getrefcount(number2))
