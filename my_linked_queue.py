"""
Author : Nagmani Kumar
Date : sep 2023
"""

class Empty(Exception):
    # through Error during attempting to access an element from an empty container.
    pass

class LinkedQueue:

    """FIFO queue implementation using a singly linked list for storage."""

    #................Nested _Node class.................
    class _Node:

        """Lightweight, nonpublic class for storing a singly linked node"""

        _slot__ = '_element', '_next'    # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next


    #................Stack Methods.................

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        return self._size


    def is_empty(self):
        return self._size == 0


    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._head._element


    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer


    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


"""
Analysis:
The LinkedQueue is similar to the LinkedStack in that all operations run in worst-case constant time,
and the space usage is linear in the current number of elements.
"""





