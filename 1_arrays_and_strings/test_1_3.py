"""Write a method to replace all spaces in a string with '%20'."""


def URLify(string, length):
    """time: O(n) space: O(n)"""
    return string.rstrip().replace(' ', '%20')


def test_URLify():
    assert URLify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
