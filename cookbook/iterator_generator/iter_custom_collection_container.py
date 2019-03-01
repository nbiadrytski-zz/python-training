"""
You have built a custom container object that internally holds a list, tuple, or some other iterable.
You would like to make iteration work with your new container.
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, node):
        self._children.append(node)

    # Python’s iterator protocol requires __iter__() to return a special iterator object
    # that implements a __next__() method to carry out the actual iteration.
    def __iter__(self):
        return iter(self._children)  # forwards the iteration request to the internally held _children attribute


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    for child in root:
        print(child)
