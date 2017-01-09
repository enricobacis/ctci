"""
Implement a function to check fi a binary tree is a binary search tree.
"""

from tree import BinaryNode


def validate_bst(root, minval=float('-inf'), maxval=float('+inf')):
    """time: O(n) space: O(n)"""
    return ((minval < root.value < maxval)
            and (not root.left or validate_bst(root.left, minval, root.value))
            and (not root.right or validate_bst(root.right, root.value, maxval)))


def test_valid_bst(fn):

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

    assert fn(n8) == True


def test_invalid_bst(fn):

    #      8
    #     / \
    #    4   10
    #   / \   \
    #  2   12  20

    n2  = BinaryNode(2)
    n12 = BinaryNode(12)
    n4  = BinaryNode(4,  left=n2, right=n12)
    n20 = BinaryNode(20)
    n10 = BinaryNode(10,          right=n20)
    n8  = BinaryNode(8,  left=n4, right=n10)

    assert fn(n8) == False
