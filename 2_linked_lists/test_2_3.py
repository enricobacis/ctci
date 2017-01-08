"""
Implement an algorithm to delete a node in the middle of a singly linked
list, given only access to that node.
"""

from linkedlist import Node


def delete_middle_node(node):
    """time: O(1) space: O(1)"""
    # we actually clone node.next into node
    node.value = node.next.value
    node.next = node.next.next


def test_delete_middle_node(fn):
    head = Node.from_iterable('abcdef')
    c = head.next.next
    fn(c)
    assert head.to_list() == list('abdef')
