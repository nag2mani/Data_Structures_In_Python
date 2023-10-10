"""
Author : Nagmani Kumar
Date : sep 2023
"""

class Empty(Exception):
    # through Error during attempting to access an element from an empty container.
    pass

class CircularArrayQueue(object):

    """We can implement the deque ADT in much the same way as the ArrayQueue class"""

    DEFAULT_CAPACITY = 8

    def __init__(self):
        self._data = [None] * CircularArrayQueue.DEFAULT_CAPACITY
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
    
    def last(self):
        # Return the element at the front of the queue.Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise Empty("Queue is empty")
        last_index_of_element = (self._front + self._size - 1) % len(self._data)  
        return self._data[last_index_of_element]    # Think why not return self._data[-1]

    def add_first(self, e):
        # add e in the first place of the circular array.
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def delete_first(self):
        #It is same as dequeue() of array_queue.
        # delete and return the first element of circular array.
        if self.is_empty():
            raise Empty("Queue is empty")

        answer = self._data[self._front]
        self._data[self._front] = None   #help in garbage collection.
        self._front = (self._front + 1) % len(self._data) #now front will be another element.
        self._size -= 1
        return answer

    def add_last(self, e):
        # It is same as enqueue() of array_queue.
        # add the element e to the end of the circular array.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        last_index_to_insert = (self._front + self._size) % len(self._data)
        self._data[last_index_to_insert] = e
        self._size += 1

    def delete_last(self):
        # delete and return the last element of the circular array.
        last_index_of_element = (self._front + self._size - 1) % len(self._data)
        answer = self._data[last_index_of_element]
        self._data[last_index_of_element] = None
        self._size -= 1
        return answer


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
The efficiency of an ArrayDeque is similar to that of an ArrayQueue,
with all operations having O(1) running time,
but with that bound being amortized for operations that may change the size of the underlying list.
"""


if __name__ == "__main__":
    # This code will only execute when the module is run directly.
    D = CircularArrayQueue()
    D.add_last(5)
    D.add_first(3)
    D.add_first(7)
    D.first()
    D.delete_last()
    D.delete_last()
    print(D.last())
    D.delete_last()
    print(D._data)
    print(D.is_empty())
    print(len(D))

