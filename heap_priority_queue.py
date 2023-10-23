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
        return self._left(j) < len(self.data)  # index beyond the end of the list?

    def _has_right(self, j):
        return self._right(j) < len(self.data)  # index beyond the end of the list?

    def swap(self, i, j):
        """Swap the elements at indices i and j of the array."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self._upheap(parent)  # recur at the position of the parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self._downheap(small_child)  # recur at the position of the small child

    def __init__(self):
        """Create a new empty Priority Queue."""
        self.data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self.data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self.data.append(self._Item(key, value))
        self._upheap(len(self.data) - 1)  # _upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with the minimum key.

        Raise an Empty exception if empty.
        """
        if self.is_empty():
            raise "Priority queue is empty."
        item = self.data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with the minimum key.

        Raise an Empty exception if empty.
        """
        if self.is_empty():
            raise "Priority queue is empty."
        self.swap(0, len(self.data) - 1)  # put the minimum item at the end
        item = self.data.pop()  # and remove it from the list;
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


