"""
Author : Nagmani Kumar
Date : sep 2023
"""


class Stacks:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek into an empty stack.")

    def size(self):
        return len(self.stack)


# Example usage
stack = Stacks()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.stack)  # Output: Stack: [10, 20, 30]

print("Top:", stack.top())  # Output: Pop: 30
print("Stack:", stack.stack)  # Output: Stack: [10, 20]

print("Top:", stack.top())  # Output: Peek: 20

print("Is empty:", stack.is_empty())  # Output: Is empty: False

print("Stack size:", stack.size())  # Output: Stack size: 2
