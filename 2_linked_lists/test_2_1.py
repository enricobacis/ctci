"""Write code to remove duplicates from an unsorted linked list."""

from linkedlist import Node


def remove_dups(node):
    """time: O(n) space: O(n)"""
    if not node: return

    # the first node can never be a duplicate
    values = set([node.value])
    pred, node = node, node.next

    # we remove duplicates starting from the second node
    while node:
        if node.value not in values:
            values.add(node.value)
            pred, node = node, node.next
        else:
            pred.next = node = node.next


def test_remove_dups():
    head = Node.from_iterable([1,2,3,2,3,5,2,5,6,1])
    remove_dups(head)
    assert head.to_list() == [1,2,3,5,6]
