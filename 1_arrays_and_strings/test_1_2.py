"""Given two strings, write a method to decide if one is a permutation of the other."""

from collections import Counter


def check_permutation(a, b):
    """time: O(n) space: O(n)"""
    if len(a) != len(b): return False
    return Counter(a) == Counter(b)


def check_permutation_2(a, b):
    """time: O(n*logn) space: O(1). It modifies the lists in place."""
    if not isinstance(a, list): a = list(a)
    if not isinstance(b, list): b = list(b)
    if len(a) != len(b): return False
    a.sort(); b.sort()
    return a == b


def test_check_permutation(fn):
    assert fn('abcd', 'abc')  == False
    assert fn('abcd', 'abce') == False
    assert fn('abcd', 'acbd') == True
    assert fn('abab', 'baba') == True
