"""
Given a binary tree, design an algorithm which creates a linked list of all the
nodes at each depth (e.g., if you have a tree with depth D, you'll have D
linked lists).
"""

from tree import BinaryNode


def list_of_depths(root):
    """time: O(n) space: O(n)"""
    nodes = [root]
    levels = [nodes]

    while nodes:
        children = []
        for node in nodes:
            if node.left: children.append(node.left)
            if node.right: children.append(node.right)
        if children:
            levels.append(children)
        nodes = children

    return levels


def test_list_of_depth(fn):

    #      8
    #     / \
    #    4   10
    #   / \   \
    #  2   6   20

    n2  = BinaryNode(2)
    n6  = BinaryNode(6)
    n4  = BinaryNode(4,  left=n2, right=n6)
    n20 = BinaryNode(20)
    n10 = BinaryNode(10,          right=n20)
    n8  = BinaryNode(8,  left=n4, right=n10)

    levels = list_of_depths(n8)
    levels = [map(lambda node: node.value, level) for level in levels]
    assert levels == [[8], [4, 10], [2, 6, 20]]
