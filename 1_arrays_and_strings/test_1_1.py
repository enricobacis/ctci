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
    lst.sort()
    for i in xrange(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True


def test_is_unique():
    assert is_unique('abcd') == is_unique_2('abcd') == is_unique_3(list('abcd')) == True
    assert is_unique('aacd') == is_unique_2('aacd') == is_unique_3(list('aacd')) == False
    assert is_unique('abbd') == is_unique_2('abbd') == is_unique_3(list('abbd')) == False
    assert is_unique('abcc') == is_unique_2('abcc') == is_unique_3(list('abcc')) == False
    assert is_unique('abca') == is_unique_2('abca') == is_unique_3(list('abca')) == False
