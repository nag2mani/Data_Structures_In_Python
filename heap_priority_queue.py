"""
Author : Nagmani Kumar
Date : oct 2023
"""

from priorityqueue import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase): # base class defines Item
    """A min-oriented priority queue implemented with a binary heap."""

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond the end of the list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond the end of the list?

    def swap(self, i, j):
        """Swap the elements at indices i and j of the array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self.swap(j, parent)
            self._upheap(parent)  # recur at the position of the parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self.swap(j, small_child)
                self._downheap(small_child)  # recur at the position of the small child

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)  # _upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with the minimum key.

        Raise an Empty exception if empty.
        """
        if self.is_empty():
            raise "Priority queue is empty."
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with the minimum key.

        Raise an Empty exception if empty.
        """
        if self.is_empty():
            raise "Priority queue is empty."
        self.swap(0, len(self._data) - 1)  # put the minimum item at the end
        item = self._data.pop()  # and remove it from the list;
        self._downheap(0)  # then fix the new root
        return (item._key, item._value)


if __name__ == "__main__":
    H = HeapPriorityQueue()
    H.add(2, "j")
    H.add(8, "j8")
    H.add(90, "j8")
    H.add(1, "j1")
    H.add(12, "j1")
    H.add(0, "j1")

    print(len(H))
    print(H.remove_min())
    print(H.remove_min())
    print(len(H))
    print(H.min())



class BottomUpHeapConstruction(HeapPriorityQueue):

    def __init__(self, contents = ()):
        """Create a new priority queue.By default, queue will be empty. If contents is given, it should be as an iterable sequence of (k,v) tuples specifying the initial contents."""
        self._data = [self._Item(k,v) for k , v in contents]
        if len(self._data) > 1:
            self._heapify()
    
    def _heapify(self):
        start = self._parent(len(self) - 1)
        for i in range(start, -1, -1):
            self._downheap(i)


if __name__ == "__main__":
    print("BottomUpHeapConstruction Start: ")
    B = BottomUpHeapConstruction()
    B.add(2, "j")
    B.add(8, "j8")
    B.add(90, "j8")
    B.add(1, "j1")
    B.add(12, "j1")
    B.add(0, "j1")

    print(B.remove_min())
    print(B.remove_min())
    print(B.remove_min())
    print(B.remove_min())
    print(B.remove_min())
    print(B.remove_min())