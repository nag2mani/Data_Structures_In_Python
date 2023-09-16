"""
Author : Nagmani Kumar
Email : nag2mani@gmail.com
Date : 16th sep 2023
"""


class Empty(Exception):
    # through Error during attempting to access an element from an empty container.
    pass


# class ArrayStack:
# # This is old style of writing class without specifying the base class but in python > 3.0 both is treated as same.

class ArrayStack(object):

    """ LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        # Create an empty stack.
        self._data = []
    
    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)
    
    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack.
        return self._data.append(e)

    def top(self):
        # Return the element at the top of the stack and Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]
    
    def pop(self):
        # Remove and return the element from the top of the stack (end element).Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise 'stack is empty'
        return self._data.pop()


"""
Analysis:
For top(), is_empty(), and len() use constant time in the worst case but The O(1) time for push and pop are amortized bounds.
The space usage is O(n), where n is the current number of elements in the stack.


Amortisation:
the amortized cost per append operation is O(1), meaning that, on average, each append operation takes constant time, even though individual appends may take longer due to resizing operations.
This analysis shows that despite occasional expensive resizing operations, the overall performance of dynamic arrays (like Python lists) is efficient and suitable for real-world applications.
 So, amortized time for each append is independent of n. (see page 201 of DSA in Python by Goodrich, Tamassia and  Goldwasser)
 """


if __name__ == "__main__":
    # This code will only execute when the module is run directly.

    s=ArrayStack()
    s.push(8)
    s.push(9)
    d = s._data
    print(d)
    d.append('nagmani')
    print(d)
    print(s.top())
    print(len(s))
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())

