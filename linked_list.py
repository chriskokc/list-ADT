# List ADT
# Linked List implementation
from node import Node


class List:
    def __init__(self, head=None):
        self.head = head

    def get_item(self, n):
        current = self.head
        count = 0
        while current is not None:
            if count == n:
                return current.value
            current = current.next
            count += 1
        return f"The linked list has ended and the {n}th element wasn't there."

    def search(self, x):
        current = self.head
        while current is not None:
            if current.value == x:
                return True
            current = current.next
        return False

    def insert_front(self, x):
        new_node = Node(x)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def remove(self, x):
        current = self.head
        prev = None
        # if the head itself is the match
        if current.value == x:
            self.head = current.next
            # finish the whole function
            return
        while current is not None:
            # if we find the value, we stop searching
            if current.value == x:
                break
            prev = current
            current = current.next
        # if the value cannot be found, finish the whole function
        if current is None:
            return "The node cannot be found in the list as there is no matching value."
        # disconnect the matching node from the list
        prev.next = current.next

