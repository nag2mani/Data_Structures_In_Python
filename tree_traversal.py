"""
Author : Nagmani Kumar
Date : september 2023
Subject : These Algorithms designed for tree, For more datails open "tree.py".
"""


from tree import LinkedBinaryTree
T = LinkedBinaryTree()

def preorder_traversal(T, p):
    visited = []
    if p.element() not in visited:
        print(p.element())
        visited.append(p.element())
        for c in T.children(p):
            preorder_traversal(T, c)
# preorder_traversal(T, T.root())


def postorder_traversal(T, p):
    visited = []
    for c in T.children(p):
        postorder_traversal(T, c)
    if p.element() not in visited:
        print(p.element())
        visited.append(p.element())
# postorder_traversal(T, T.root())


def breadthfirst(T):
    queue = [T.root()]
    visited = []
    while len(queue) != 0:
        x = queue.pop(0)
        visited.append(x)
        print(x.element())
        for c in T.children(x):
            queue.append(c)
# breadthfirst(T)

# inorder
def inorder(p):
    visited = []
    if T.left(p) is not None:
        inorder(T, T.left(p))
    visited.append(p.element())
    if T.right(p) is not None:
        inorder(T, T.right(p))




















