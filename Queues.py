"""
Author : Nagmani Kumar
Date : sep 2023
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


# Example usage
if __name__ == "__main__":
    # Create a queue
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Display the queue
    print("Queue:", q.items)  # Output: Queue: [10, 20, 30]

    # Dequeue an element
    dequeued_item = q.dequeue()
    print("Dequeued item:", dequeued_item)  # Output: Dequeued item: 10

    # Peek at the front element
    front_item = q.peek()
    print("Front item:", front_item)  # Output: Front item: 20

    # Check if the queue is empty
    print("Is queue empty?", q.is_empty())  # Output: Is queue empty? False

    # Get the size of the queue
    print("Queue size:", q.size())  # Output: Queue size: 2


