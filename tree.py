"""
Author : Nagmani Kumar
Date : september 2023
Subject : It contains Tree ADT and their traversal algorithm.
"""

from my_linked_queue import LinkedQueue

class Tree:
    """Abstract base class representing a tree structure."""

#------------------------------- nested Position class -------------------------------

    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("Must be implemented by subclass")

        def eq(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("Must be implemented by subclass")

        def ne(self, other):
            """Return True if other does not represent the same location."""
            return not(self == other)  # opposite of eq


# ---------- abstract methods that concrete subclass must support ----------


    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("Must be implemented by subclass")


# ---------- concrete methods implemented in this class ----------


    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree. Its time complexity is N^2."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of the subtree rooted at position p. Its time complexity is N."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at the position p.
        If p is none then return the height of the entire tree
        """
        if p is None:
            p = self.root()
            return self._height2(p)

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    #Helper method of preorder
    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    ## Preorder without helper and you can do on any node.
    def preorder2(self, p):
        yield p
        for c in self.children(p):
            for i in self.preorder2(c):
                yield i

    def postorder(self):
        """Generate a postorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    #Helper method of postorder
    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p"""
        for c in p.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree"""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def positions(self):
        """Generate an iteration of the tree's positions.It relies on a preorder traversal to generate the results"""
        return self.preorder()

    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        for p in self.positions():
            yield p.element()



class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------

    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    # ---------- concrete methods implemented in this class ----------

    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p"""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        """Generate an iteration of the tree's positions.It relies on a inorder traversal to generate the results"""
        return self.inorder()



class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:  
        # Lightweight, nonpublic class for storing a node.
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node if the position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for a given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # -------------------------- binary tree constructor --------------------------

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # -------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if the tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is the root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def add_root(self, e):
        """Place element e at the root of an empty tree and return a new Position.
        Raise ValueError if the tree is nonempty.
        """
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        Return the Position of the new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)  # node is its parent
        return self._make_position(node._left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of the new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)  # node is its parent
        return self._make_position(node._right)

    def replace(self, p, e):
        """Replace the element at Position p with e, and return the old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old


    def delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element


    def attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external position p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("Position must be a leaf")
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be the same type
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attach t1 as the left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to empty.
            t1._size = 0
        if not t2.is_empty():  # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None   # set t2 instance to empty
            t2._size = 0




if __name__ == "__main__":

    """This is the T1 tree for experiments."""
    #       90
    #      / \
    #     /   \
    #    50    40
    #   / \     \
    #  30 20    10

    T1 = LinkedBinaryTree()
    root_position = T1.add_root(90)
    # print(T1.root().element())
    root_left = T1.add_left(root_position, 50)
    root_right = T1.add_right(root_position, 40)
    left_of_50 = T1.add_left(root_left, 30)
    right_of_50 = T1.add_right(root_left, 20)
    right_of_40 = T1.add_right(root_right, 12)
    # print("Number of children of Root Node of T1 :", T1.num_children(root_position))
    # print("Number of children of right child of Root Node of T1 :",T1.num_children(root_right))
    print("Length of tree T1:",len(T1))

    # print("Before Replacement :", T.right(root_position).element())
    # T.replace(root_right, 70)
    # print("After Replacement :",T.right(root_position).element())

    # print("Before Delete :", T.right(root_position).element())
    # T.delete(root_right)
    # print("After Delete :",T.right(root_position).element())

    #Creating another tree "T2".
    """This is the T2 tree for experiments."""
    #      180
    #      / \
    #     /   \
    #   100    80
    #   / \     \
    #  60 40    20

    T2 = LinkedBinaryTree()
    root_position = T2.add_root(180)
    # print(T2.root().element())
    root_left = T2.add_left(root_position, 100)
    root_right = T2.add_right(root_position, 80)
    left_of_100 = T2.add_left(root_left, 60)
    right_of_100 = T2.add_right(root_left, 40)
    right_of_80 = T2.add_right(root_right, 30)
    # print("Number of children of Root Node of T2 :", T2.num_children(root_position))
    # print("Number of children of right child of Root Node of T2 :",T2.num_children(root_right))
    print("Length of tree T2:",len(T2))

    #Attaching T1 and T2 at a node T
    T = LinkedBinaryTree()
    root_position = T.add_root(1000)

    # print("Length before attaching :", len(T))
    T.attach(root_position, T1, T2)
    print("Length of tree T after attaching T1 and T2 with a unique root:", len(T))

    # Final Tree Structure
    #          1000
    #         /     \
    #        /       \
    #       /         \
    #      /           \
    #     90            180
    #    /  \          /   \
    #   /    \        /     \
    #  50     40     100     80
    # /  \     \    / \       \
   # 30  20     10  60 40      20

    # print("Preorder Traversal of Tree :")
    # for i in iter(T.preorder()):
    #     print(i.element(), end=", ")

    # print("\nPreorder2 Traversal of Tree :")
    # for i in iter(T.preorder2(T.root())):
    #     print(i.element(), end=", ")

    # # print("Postorder Traversal of Tree :")
    # # for i in iter(T.postorder()):
    # #     print(i.element(), end=", ")

    # print("\nInorder Traversal of Tree :")
    # for i in iter(T.inorder()):
    #     print(i.element(), end=", ")

    # print("\nTree Traversal of Tree :")
    # for i in iter(T):
    #     print(i, end=" ")




#Application:

for p in T.preorder():
    print(p.element(), end= ", ")

def preorder_indent(T, p, d):
    """Print preorder representation of subtree of T rooted at p at depth d"""
    print(2*d*' ', str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d+1)

# preorder_indent(T, T.root(), len(T))


def preorder_level(T, p, d, path):
    """Print labeled representation of subtree of T rooted at p at depth d"""
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)

    for c in T.children(p):
        preorder_level(T, c, d+1, path)
        path[-1] += 1
    path.pop()

preorder_level(T, T.root(), len(T), [])


def parenthesize(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end="")
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = " (" if first_time else ", "
            print(sep, end="")
            first_time = False
            parenthesize(T, c)
        print(")", end="")

parenthesize(T, T.root())


def disk_space(T, p):
    """Return total disk space for subtree of T rooted at p"""
    subtotal = p.element().space()
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal

print(disk_space(T, T.root()))

# Finished
#Issue: _make_position and _validate should be function of class binary tree but in book and pdf diffrent implimentation is given, which is correct?