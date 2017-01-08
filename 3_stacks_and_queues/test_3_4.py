"""
Implement a MyQueue class which implements a queue using two stacks.
"""

from stack import Stack
import pytest


class MyQueue(object):

    def __init__(self):
        self.add_stack = Stack()
        self.rem_stack = Stack()

    def add(self, value):
        # ensure we are using the data as a stack to push
        if self.add_stack.is_empty():
            while not self.rem_stack.is_empty():
                self.add_stack.push(self.rem_stack.pop())
        # then push the value onto the stack
        self.add_stack.push(value)

    def remove(self):
        # ensure we are using the data as a queue to pop
        if self.rem_stack.is_empty():
            while not self.add_stack.is_empty():
                self.rem_stack.push(self.add_stack.pop())
        # then pop the value from the *queue*
        return self.rem_stack.pop()

    def peek(self):
        # the same as remove but we peek the rem_stack
        if self.rem_stack.is_empty():
            while not self.add_stack.is_empty():
                self.rem_stack.push(self.add_stack.pop())
        return self.rem_stack.peek()

    def is_empty(self):
        return self.add_stack.is_empty() and self.rem_stack.is_empty()


def test_my_queue():
    queue = MyQueue()

    assert queue.is_empty()
    with pytest.raises(AttributeError): queue.peek()
    with pytest.raises(AttributeError): queue.remove()

    queue.add(1)
    queue.add(2)
    assert not queue.is_empty()
    assert queue.remove() == 1

    queue.add(3)
    assert queue.peek() == 2

    queue.add(4)
    assert queue.remove() == 2
    assert queue.remove() == 3
    assert queue.remove() == 4
    assert queue.is_empty()
