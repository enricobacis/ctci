"""
TODO
"""

import pytest


def fn():
    """time: O() space: O()"""
    pass


def fn_2():
    """time: O() space: O()"""
    pass


def test_fn(fn):
    assert fn() == None
