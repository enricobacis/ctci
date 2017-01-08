"""
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure such as an array.
"""

from stack import Stack


def sort_stack(base):
    """time: O() space: O()"""
    temporary = Stack()
    result = Stack()

    while not base.is_empty():

        while not base.is_empty():
            value = base.pop()
            while not result.is_empty() and result.peek() < value:
                temporary.push(result.pop())  # not sorted. result -> temporary
            result.push(value)                # push the value in right position

        # swap base and temporary
        base, temporary = temporary, base

    return result


def test_sort_stack(fn):
    stack = Stack()
    stack.push(4); stack.push(1); stack.push(2); stack.push(3); stack.push(0)

    result = fn(stack)
    assert result.to_list() == list(range(5))
