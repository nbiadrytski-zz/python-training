class MaxHeap:
    """MaxHeap always bubbles the highest value to the top, so it can be removed instantly"""
    def __init__(self, items=[]):  # pass list of items we want to add to the heap
        super().__init__()
        self.heap = [0]  # we do not use 0 element, we start from 1
        for item in items:
            self.heap.append(item)  # add items to the end of the list
            self.__floatUp(len(self.heap) - 1)  # float up to its proper position

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):  # returns top item on the heap
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            # max item is at index 1, swap it with the last item
            self.__swap(1, len(self.heap) - 1)
            # remove last item and assign it to max
            max = self.heap.pop()
            # bubble down the first item that we moved to top position
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        

