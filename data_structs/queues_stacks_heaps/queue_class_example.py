from collections import deque


class CustomQueue:
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue_(self, item):
        self.queue.append(item)

    def dequeue_(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    def get_size(self):
        self.size = len(self.queue)
        return self.size

    def __repr__(self):
        return str(self.queue)


if __name__ == '__main__':
    my_queue = CustomQueue()
    my_queue.enqueue_(5)
    my_queue.enqueue_(10)
    my_queue.enqueue_(15)
    print(my_queue)  # deque([5, 10, 15])

    print(my_queue.dequeue_())  # 5
    print(my_queue.get_size())  # 2
