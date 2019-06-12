# stack: LIFO - last in first out

my_stack = list()  # new stack which is an empty list
my_stack.append(4)  # push an item onto the stack
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack)  # [4, 7, 12, 19]

print(my_stack.pop())  # 19, remove item from stack
print(my_stack.pop())  # 12
print(my_stack)  # [4, 7]
