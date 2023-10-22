"""
Author : Nagmani Kumar
Date : sep 2023
"""

class Empty(Exception):
    # through Error during attempting to access an element from an empty container.
    pass

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""

    #--------------------------Nested _Node class--------------------------
    class _Node:

        """Lightweight, nonpublic class for storing a singly linked node"""

        __slots__ = '_element', '_prev', '_next'    # streamline memory usage

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev  #previous node reference.
            self._next = next  #next node reference.

    #--------------------------Base Class Methods--------------------------

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header  # header is before trailer
        self._size = 0

    def __len__(self):
        # Return the number of elements in the list.
        return self._size
    
    def is_empty(self):
        # Return True if list is empty otherwise false.
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # linked to neighbors.
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self.size -= 1
        element = node._element  # record deleted element.
        node._prev = node._next = node._element = None  # deprecate node.
        return element


"""Implementing Positional List"""



class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

#-------------------------- nested Position class --------------------------

    # Nested Position class
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def eq(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def ne(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # Opposite of eq


# ------------------------------- utility method -------------------------------


    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:  # Convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for the given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None  # Boundary violation
        else:
            return self.Position(self, node)  # Legitimate position


 #------------------------------- accessors -------------------------------


    def first(self):
        """Return the first Position in the list (or None if the list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if the list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self.make_position(node.prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)


#------------------------------- mutators -------------------------------


    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return a new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return a new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into the list before Position p and return a new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into the list after Position p and return a new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # Inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e. Return the element formerly at Position p."""
        original = self._validate(p)
        old_value = original._element  # Temporarily store old element
        original._element = e  # Replace with new element
        return old_value  # Return the old element value



if __name__ == "__main__":
    P = PositionalList()
    # print(type(P))
    P.add_first(20)
    P.add_last(21)
    # print(len(P))
    P.add_after(P.last(), "kumar")
    P.replace(P.last(), "Mahto")
    P.add_before(P.last(), "Nagmani")
    # print(P.first().element())
    for i in iter(P):
        print(i)














