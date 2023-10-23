"""
Author : Nagmani Kumar
Date : oct 2023
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
        
        def excess_element(self):
        # my own method to excess the element
            return (self._key, self._value)

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
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k, v) tuple with the minimum key."""
        p = self.find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with the minimum key."""
        p = self.find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self._data.first()
        while cursor is not None:
            yield cursor.element().excess_element()
            cursor = self._data.after(cursor)


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
        newest = self._Item(key, value)  # Make a new item instance
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
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with the minimum key."""
        if self.is_empty():
            raise "Priority queue is empty."
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self._data.first()
        while cursor is not None:
            yield cursor.element().excess_element()
            cursor = self._data.after(cursor)


if __name__ == "__main__":
    Up = UnsortedPriorityQueue()
    Up.add(10,"nagmani")
    Up.add(100,"Datai")
    Up.add(15,"Useni")
    Up.add(7,"kkkk")
    Up.add(13,"oujhb")
    print(len(Up))
    print(Up.min())
    print(Up.remove_min())


    for i in iter(Up):
        print(i)


    Sp = SortedPriorityQueue()
    Sp.add(10,"nagmani")
    Sp.add(100,"Datai")
    Sp.add(15,"Useni")
    Sp.add(7,"kkkk")
    Sp.add(13,"oujhb")
    print(len(Sp))
    print(Sp.min())
    print(Sp.remove_min())


    for i in iter(Sp):
        print(i)
        