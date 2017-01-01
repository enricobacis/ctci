"""Common Linked List module to be used with other exercises."""


class Node(object):
    """Single node of a linked list."""

    def __init__(self, value, next=None):
        """Initialize the node with a value and optionally a next pointer."""
        self.value = value
        self.next = next

    def to_list(self):
        """Return a list with the elements contained in the linked list."""
        lst = []
        node = self
        while node:
            lst.append(node.value)
            node = node.next
        return lst

    def __str__(self):
        return str(self.to_list())

    @staticmethod
    def from_iterable(elements):
        """Create a linked list from the given iterable."""
        if not elements: return None
        iterator = iter(elements)
        head = tail = Node(next(iterator))
        for element in iterator:
            tail.next = Node(element)
            tail = tail.next
        return head
