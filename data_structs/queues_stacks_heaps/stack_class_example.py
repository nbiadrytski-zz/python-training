class ListBasedStack:
    def __init__(self):
        self.stack = list()

    def push_(self, item):
        """push an item onto the stack"""
        self.stack.append(item)

    def pop_(self):
        """remove item from stack"""
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek_(self):
        """return top item from the list without removing the item"""
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __repr__(self):
        return str(self.stack)


if __name__ == '__main__':
    my_stack = ListBasedStack()
    my_stack.push_(1)
    my_stack.push_(3)
    my_stack.push_(5)
    print(my_stack)  # [1, 3, 5]

    print(my_stack.pop_())  # 5
    print(my_stack.peek_())  # 3
    print(my_stack.pop_())  # 3
    print(my_stack.pop_())  # 1

    print(my_stack)  # []
    print(my_stack.pop_())  # None

