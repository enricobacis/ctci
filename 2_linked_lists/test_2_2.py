"""Implement an algorithm to find the kth to last element of a singly linked list."""

from linkedlist import Node
import pytest


def kth_to_last(node, k):
    """time: O(n) space: O(n)"""
    lst = []
    while node:
        lst.append(node.value)
        node = node.next

    idx = len(lst) - k - 1
    if idx < 0:
        raise IndexError('index out of bound')
    else:
        return lst[idx]


def test_kth_to_last():
    lst = list(range(10))
    head = Node.from_iterable(lst)

    for k, element in enumerate(reversed(lst)):
        assert kth_to_last(head, k) == element

def test_kth_to_last_failures():
    head = Node.from_iterable(range(10))

    with pytest.raises(IndexError):
        kth_to_last(head, -1)

    with pytest.raises(IndexError):
        kth_to_last(head, 10)
