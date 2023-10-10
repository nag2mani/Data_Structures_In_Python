"""
Author : Nagmani Kumar
Date : sep 2023
"""


# Node Class for Linked List
class Node:
    def __init__(self, element):
        self._element = element
        self._next = None

class LinkedList:

    """A singly linked list for storage."""

    def __init__(self):
        self._head = None
        self._size = 0

    def insert_at_first(self, e):
        # new_node = Node(e)
        # if self._head == None:
        #     self._head = new_node
        #     self._size += 1
        # else:
        #     new_node._next = self._head
        #     self._head = new_node
        #     self._size += 1

        new_node = Node(e)
        new_node._next = self._head
        self._head = new_node
        self._size += 1

    def delete_at_first(self):
        self._head = self._head._next

    def insert_at_last(self, e):
        new_node = Node(e)
        if self._head is None:
            self._head = new_node
            return
        current_node = self._head
        while current_node._next:
            current_node = current_node._next
        current_node._next = new_node

    def delete_at_last(self):
        current_node = self._head
        while current_node._next._next:
            current_node = current_node._next
        current_node._next = None

    # print method for the linked list
    def printLL(self):
        current_node = self._head
        while(current_node):
            print(current_node._element)
            current_node = current_node._next


# create a new linked list
l_list = LinkedList()

# add nodes to the linked list
l_list.insert_at_last('a')
l_list.insert_at_last('b')
l_list.insert_at_first('c')
l_list.insert_at_last('d')

# print the linked list
print("Node Data")
l_list.printLL()




