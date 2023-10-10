"""
Author : Nagmani Kumar
Date : sep 2023
"""

class Empty(Exception):
    # through Error during attempting to access an element from an empty container.
    pass

class LinkedStack:

    """LIFO Stack implementation using a singly linked list for storage."""

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
        self._size = 0


    def __len__(self):
        return self._size


    def is_empty(self):
        return self._size == 0
    

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._head._element
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

"""
Analysis:
We see that all of the methods complete in worst-case constant time. This is in contrast to the amortized bounds for the ArrayStack
"""


if __name__ == "__main__":
    S = LinkedStack()
    S.push(3)
    S.push(6)
    S.push(9)
    print(S.pop())
    print(S.top())
    print(len(S))
    print(S.is_empty())


