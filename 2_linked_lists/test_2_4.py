"""
Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x. If x is contained
within the list, the values of x only need to be after the elements less than x.
"""

from linkedlist import Node


def partition(node, x):
    """time: O(n) space O(n)"""
    head = tail = Node(node.value)
    node = node.next

    while node:
        if node.value < x:    # insert as first
            head = Node(node.value, next=head)
        else:
            tail.next = Node(node.value)
            tail = tail.next  # insert as last

        node = node.next
    return head


def partition_in_place(node, x):
    """time: O(n) space: O(1)"""
    head, pivot = node, None

    while node:
        if node.value >= x and not pivot:
            pivot = node
        elif node.value < x and pivot:
            # swap the node and the pivot (first biggest element)
            node.value, pivot.value = pivot.value, node.value
            # advance the pivot (pivot is now in the left part due to swap)
            pivot = pivot.next

        node = node.next
    return head


def test_partition(fn):
    lst, x = [3, 5, 8, 5, 10, 2, 1], 5
    head = Node.from_iterable(lst)
    node = fn(head, x)

    # test for not-in-place
    if fn.__name__ == 'partition':
        assert head.to_list() == lst

    assert node is not None
    in_right = False

    # verify partitioned property
    while node:
        if node.value >= x: in_right = True
        if in_right: assert node.value >= x
        else: assert node.value < x
        node = node.next
