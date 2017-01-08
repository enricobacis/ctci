"""Implement an algorithm to determine if a string has all unique characters."""

from itertools import islice


def is_unique(string):
    """time: O(n) space: O(n)"""
    return len(string) == len(set(string))


def is_unique_2(string):
    """time: O(n*2) space: O(1)"""
    for idx1, char1 in enumerate(string):
        for char2 in islice(string, idx1 + 1, None):
            if char1 == char2:
                return False
    return True


def is_unique_3(lst):
    """time: O(n*logn) space: O(1). It modifies the list in place."""
    if not isinstance(lst, list): lst = list(lst)
    lst.sort()
    for i in xrange(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True


def test_is_unique(fn):
    assert fn('abcd') == True
    assert fn('aacd') == False
    assert fn('abbd') == False
    assert fn('abcc') == False
    assert fn('abca') == False
