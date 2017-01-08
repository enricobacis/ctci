class Node(object):

    """A single node of a linked list."""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack(object):

    """Simple Stack implementation with push, pop, peek and is_empty."""

    def __init__(self):
        """Initialize a Stack object."""
        self.top = None

    def peek(self):
        """Return the top value of the stack without popping."""
        return self.top.value

    def push(self, value):
        """Push a value onto the stack."""
        self.top = Node(value, next=self.top)

    def pop(self):
        """Pops a value from the stack."""
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None
