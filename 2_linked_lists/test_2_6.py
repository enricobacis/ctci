"""
Given two (singly) linked lists, determine if the two lists intersect. Return
the intersecting node. Note that the intersection is defined based on reference,
not value.
"""

from linkedlist import Node


def intersection(node1, node2):
    """time: O(a+b) space: O(a)"""
    nodes = set()
    while node1:
        nodes.add(node1)
        node1 = node1.next

    while node2:
        if node2 in nodes:
            return node2
        node2 = node2.next

    return None


def intersection_2(node1, node2):
    """time: O(a+b) space: O(1)"""

    def length(node):
        l = 0
        while node:
            node = node.next
            l += 1
        return l

    # two intersecting nodes will reach the tail together
    len1, len2 = length(node1), length(node2)

    # ensure node1 is the longest (using swap)
    if len2 > len1: (node1, node2) = (node2, node1)

    # advance node1 so the two list are equal in length
    steps = abs(len1 - len2)
    while steps:
        node1 = node1.next
        steps -= 1

    # advance both lists together checking for same node
    while node1 and node2:
        if node1 is node2: return node1
        node1 = node1.next
        node2 = node2.next

    return None


def test_intersection(fn):

    # a - b - c - d
    #    /
    # e -
    #
    # g - h - i

    a = Node.from_iterable('abcd')
    b = a.next
    e = Node('e', next=b)
    g = Node.from_iterable('ghi')

    assert fn(a, a) == a
    assert fn(a, b) == b
    assert fn(a, e) == b
    assert fn(b, e) == b
    assert fn(a, g) == None
