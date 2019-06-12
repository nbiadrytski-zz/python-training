from collections import deque


# queue: FIFO


my_queue = deque()  # double-ended queue
my_queue.append(5)  # add to the queue
my_queue.append(10)  # remove from queue
my_queue.append(15)  # remove from queue
print(my_queue)  # deque([5, 10, 15])
print(my_queue.popleft())  # 5
print(my_queue)  # deque([10, 15])
