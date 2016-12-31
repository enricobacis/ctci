"""Given two strings, write a method to decide if one is a permutation of the other."""

from collections import Counter


def check_permutation(a, b):
    """time: O(n) space: O(n)"""
    if len(a) != len(b): return False
    return Counter(a) == Counter(b)


def check_permutation_2(a, b):
    """time: O(n*logn) space: O(1). It modifies the lists in place."""
    if len(a) != len(b): return False
    a.sort(); b.sort()
    return a == b


def test_check_permutation():
    assert check_permutation('abcd', 'abc') == check_permutation_2(list('abcd'), list('abc')) == False
    assert check_permutation('abcd', 'abce') == check_permutation_2(list('abcd'), list('abce')) == False
    assert check_permutation('abcd', 'acbd') == check_permutation_2(list('abcd'), list('acbd')) == True
    assert check_permutation('abab', 'baba') == check_permutation_2(list('abab'), list('baba')) == True
