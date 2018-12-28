def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Can't divide by zero"

print(divide(2, 0))
print("End of program")