"""
How would you design a stack which, in addition to push and pop, has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.
"""

from stack import Stack
import pytest


class StackMin(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.minstack = Stack()  # minstack will hold all the minimums

    def push(self, value):
        if self.minstack.is_empty() or value <= self.minstack.peek():
            self.minstack.push(value)      # add it to the minstack
        Stack.push(self, value)            # add it also to the stack

    def pop(self):
        value = Stack.pop(self)
        if value == self.minstack.peek():  # if we removed the minimum
            self.minstack.pop()            # pop it from the minstack
        return value

    def min(self):
        return self.minstack.peek()


def test_stackmin():
    stackmin = StackMin()

    with pytest.raises(AttributeError): stackmin.min()

    stackmin.push(2)
    assert stackmin.min() == 2  # min now returns the element

    stackmin.push(3)
    assert stackmin.min() == 2  # min not changed

    stackmin.push(1)
    assert stackmin.min() == 1  # min changed

    assert stackmin.pop() == 1  # we pop the new min
    assert stackmin.min() == 2  # min is now back to the first min
