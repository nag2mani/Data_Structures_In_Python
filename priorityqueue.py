"""
Author : Nagmani Kumar
Date : sep 2023
"""

from my_positional_list import PositionalList

class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

    def is_empty(self):  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0



class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def find_min(self):  # nonpublic utility
        """Return Position of item with the minimum key."""
        if self.is_empty():  # is_empty is inherited from the base class
            raise "Priority queue is empty"
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self.Item(key, value))

    def min(self):
        """Return but do not remove (k, v) tuple with the minimum key."""
        p = self.find_min()
        item = p.element()
        return (item.key, item.value)

    def remove_min(self):
        """Remove and return (k, v) tuple with the minimum key."""
        p = self.find_min()
        item = self._data.delete(p)
        return (item.key, item.value)



class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list."""
    
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self.Item(key, value)  # Make a new item instance
        walk = self._data.last()  # Walk backward looking for a smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)  # The new key is the smallest
        else:
            self._data.add_after(walk, newest)  # Newest goes after walk

    def min(self):
        """Return but do not remove (k, v) tuple with the minimum key."""
        if self.is_empty():
            raise "Priority queue is empty."
        p = self._data.first()
        item = p.element()
        return (item.key, item.value)

    def remove_min(self):
        """Remove and return (k, v) tuple with the minimum key."""
        if self.is_empty():
            raise "Priority queue is empty."
        item = self._data.delete(self._data.first())
        return (item.key, item.value)





