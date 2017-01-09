class Node(object):
    """Node class represent a node in a tree"""

    __slots__ = ['value', 'children']

    def __init__(self, value, children=None):
        self.value = value
        self.children = children


class BinaryNode(object):
    """Node class represent a node in a binary tree"""

    __slots__ = ['value', 'left', 'right']

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
