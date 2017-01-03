"""Implement an algorithm to find the kth to last element of a singly linked list."""

from linkedlist import Node


def kth_to_last(node, k):
    """time: O(n) space: O(n)"""
    lst = []
    while node:
        lst.append(node.value)
        node = node.next

    return lst[len(lst) - k - 1]


def test_kth_to_last():
    lst = list(range(10))
    head = Node.from_iterable(lst)

    for k, element in enumerate(reversed(lst)):
        assert kth_to_last(head, k) == element
