"""
Author : Nagmani Kumar
Email : nag2mani@gmail.com
Date : 16th sep 2023
"""

class Empty(Exception):
    # through Error during attempting to access an element from an empty container.
    pass

class ArrayQueue(object):

    """FIFO queue implementation using a Python list as underlying storage."""

    DEFAULT_CAPACITY = 8

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
    # Return the number of elements in the queue.
        return self._size
    
    def is_empty(self):
        # return True if the queue is empty.
        return self._size == 0
    
    def first(self):
    # Return the element at the front of the queue.Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise Empty("Queue is empty")

        return self._data[self._front]
    
    def dequeue(self):
        # Remove and return the first element of the queue (i.e., FIFO).Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise Empty("Queue is empty")
        
        answer = self._data[self._front]
        self._data[self._front] = None   #help in garbage collection.
        self._front = (self._front + 1) % len(self._data)  #now front will be another element.
        self._size -= 1

        # A robust approach is to reduce the array to half of its current size, whenever the number of elements stored in it falls below one fourth of its capacity.
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer
    
    def enqueue(self, e):
        #Adding an element to the back of the queue.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        last_index_to_insert = (self._front + self._size) % len(self._data)
        self._data[last_index_to_insert] = e
        self._size += 1


    def _resize(self, cap):
        # Resize to a new list of capacity.
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(len(self._size)):
            self._data[k] = old[walk]
            walk = (1+ walk) % len(old)
        self._front = 0


"""
Analysis:
For first(), is_empty(), and len() use constant time in the worst case but The O(1) time for enqueue and dequeue are amortized bounds.
The space usage is O(n), where n is the current number of elements in the stack.
"""


if __name__ == "__main__":
    # This code will only execute when the module is run directly.
    q = ArrayQueue()
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue('a')
    q.enqueue(22.7)
    print(q._data)
    q.dequeue()
    print(q._data)
    print(q.first())
    print(q._size)
    print(q.len())







