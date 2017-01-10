"""
Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than one.
"""

from tree import BinaryNode


def check_balanced(root):
    """time: O(n) space: O(n)"""

    class UnbalancedException(Exception): pass

    def get_height(node):
        if not node: return 0
        height_left = get_height(node.left)
        height_right = get_height(node.right)
        if abs(height_left - height_right) > 1:
            raise UnbalancedException()
        return 1 + max(height_left, height_right)

    try: get_height(root)
    except UnbalancedException: return False
    return True


def test_empty_tree(fn):
    assert fn(None) == True

def test_only_root(fn):
    root = BinaryNode(1)
    assert fn(root) == True

def test_only_left_child(fn):
    root = BinaryNode(1, left=BinaryNode(2))
    assert fn(root) == True

def test_only_right_child(fn):
    root = BinaryNode(1, right=BinaryNode(2))
    assert fn(root) == True

def test_degenerate(fn):
    root = BinaryNode(1, right=BinaryNode(2, right=BinaryNode(3)))
    assert fn(root) == False

def test_complex(fn):

    #      3
    #     / \
    #    2   5
    #   /   / \
    #  1   4   6

    n1 = BinaryNode(1)
    n2 = BinaryNode(2, left=n1)
    n4 = BinaryNode(4)
    n6 = BinaryNode(6)
    n5 = BinaryNode(5, left=n4, right=n6)
    root = BinaryNode(3, left=n2, right=n5)
    assert fn(root) == True

    #      3
    #     / \
    #    2   5
    #   /   / \
    #  1   4   6
    #           \
    #            7

    n7 = BinaryNode(7)
    n6.right = n7
    assert fn(root) == True

    #      3
    #     / \
    #    2   5
    #   /   / \
    #  1   4   6
    #           \
    #            7
    #             \
    #              8

    n8 = BinaryNode(8)
    n7.right = n8
    assert fn(root) == False
