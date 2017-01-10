"""
Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""

from tree import BinaryNode


def minimal_tree(lst):
    """time: O(n) space: O(n)"""
    if not lst: return None
    middle = len(lst) // 2
    root = BinaryNode(lst[middle])
    root.left = minimal_tree(lst[:middle])
    root.right = minimal_tree(lst[middle+1:])
    return root


def _tree_height(root):
    if not root: return 0
    return 1 + max(_tree_height(root.left), _tree_height(root.right))

def test_empty(fn):
    assert fn([]) == None

def test_only_root(fn):
    root = fn([1])
    assert _tree_height(root) == 1

def test_multiple_levels(fn):
    height = 5
    nodes = (2 ** height) - 1
    root = fn(list(range(nodes)))
    assert _tree_height(root) == height
