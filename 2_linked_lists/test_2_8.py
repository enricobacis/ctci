"""
Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop.
"""

from linkedlist import Node


def loop_detection(node):
    """time: O(n) space: O(n)"""
    nodes = set()

    while node:
        if node in nodes: return node
        nodes.add(node)
        node = node.next
    return None


def loop_detection_2(node):
    """time: O(n) space: O(1)"""

    slow = fast = node
    steps = 0

    while fast and fast.next:   # fast could reach the end
        slow = slow.next
        fast = fast.next.next
        steps += 1
        if fast is slow: break  # mind blowing
    else: return None           # if we dont't break, we reach the end = no loop

    # slow and fast are steps away (slow: steps, fast: 2*steps)
    # the two pointers intersect in the middle point of the loop
    nodes_before_loop = (steps + 1) // 2

    while nodes_before_loop:
        node = node.next
        nodes_before_loop -= 1

    return node


def test_loop_detection(fn):

    # a - b - c - d - e
    #         |       |
    #          -------

    a = Node.from_iterable('abcde')
    b = a.next; c = b.next; d = c.next; e = d.next
    assert fn(a) == None

    e.next = c   # create the loop
    assert fn(a) == c

def test_self_loop(fn):

    # a -
    # |  |
    #  --

    a = Node('a')
    a.next = a
    assert fn(a) == a

def test_self_loop_after_acyclic(fn):

    # a - b -
    #     |  |
    #      --

    b = Node('b'); b.next = b
    a = Node('a', next=b)
    assert fn(a) == b
