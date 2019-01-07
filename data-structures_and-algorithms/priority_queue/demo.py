from priority_queue import PriorityQueue
from item import Item

q = PriorityQueue()

q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

q.pop()
q.pop()

print(q.__repr__())
