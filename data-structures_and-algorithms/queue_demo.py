from collections import deque

# queue1 with unlimited size
queue1 = deque()
queue1.append(1)
queue1.append(2)
queue1.append(3)
print(queue1)  # deque([1, 2, 3])
queue1.appendleft(4)
print(queue1)  # # deque([4, 1, 2, 3])
queue1.pop()
print(queue1)  # deque([4, 1, 2])

# queue1 with fixed size 3
queue2 = deque(maxlen=3)
queue2.append(1)
queue2.append(2)
queue2.append(3)
print("fixed siz queue_demos before reaching limit ", queue2)  # deque([1, 2, 3], maxlen=3)
queue2.append(4)
print("fixed siz queue_demos after reaching limit ", queue2)  # deque([2, 3, 4], maxlen=3)

