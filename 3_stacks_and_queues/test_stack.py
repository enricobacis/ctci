from stack import Stack
import pytest


def test_stack():
    s = Stack()
    assert s.is_empty()
    with pytest.raises(AttributeError): s.peek()
    with pytest.raises(AttributeError): s.pop()

    s.push(1)
    s.push(2)

    assert s.peek() == 2
    assert s.pop() == 2
    assert not s.is_empty()

    assert s.peek() == 1
    assert s.pop() == 1
    assert s.is_empty()
