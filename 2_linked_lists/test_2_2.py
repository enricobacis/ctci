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


def kth_to_last2(node, k):
    """time: O(n) space: O(1)"""
    if k < 0: raise IndexError('index out of bound')

    # move the exploration node k nodes above behind
    behind = node
    while k > 0:
        if not node.next: raise IndexError('index out of bound')
        node = node.next
        k -= 1

    # now move node and behind until node reaches the end
    while node.next:
        node = node.next
        behind = behind.next

    return behind.value


def test_kth_to_last(fn):
    lst = list(range(10))
    head = Node.from_iterable(lst)

    for k, element in enumerate(reversed(lst)):
        assert fn(head, k) == element


def test_kth_to_last_failures(fn):
    head = Node.from_iterable(range(10))

    with pytest.raises(IndexError):
        fn(head, -1)

    with pytest.raises(IndexError):
        fn(head, 10)
