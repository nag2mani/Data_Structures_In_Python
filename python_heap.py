from heapq import *

count = 0

class StackByQueue:
    def __init__(self):
        self.heap = []
        heapify(self.heap)
    def push(self, v):
        global count
        count += 1
        heappush(self.heap, (-1 * count, v))
    def pop(self):
        return heappop(self.heap)

Stk = StackByQueue()
Stk.push(23)
Stk.push(34)
Stk.push(20)

