class Node:
    """
    You are building custom objects on which you would like to support iteration,
    but would like an easy way to implement the iterator protocol.
    Implement an iterator that traverses nodes in a depth-first pattern
    """
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

    def depth_first(self):
        """
        First yields itself and then
        iterates over each child
        yielding the items produced by the child’s depth_first() method (using yield from).
        """
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    # Node0
    #     Node1
    #         Node3
    #         Node4
    #     Node2
    #         Node5

    for ch in root.depth_first():
        print(ch)

    # Node(0)
    # Node(1)
    # Node(3)
    # Node(4)
    # Node(2)
    # Node(5)

    print("--------------------")

    for ch in root:
        print(ch)

    # Node(1)
    # Node(2)
