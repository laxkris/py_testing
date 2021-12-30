"""
unit test for Stack
"""


import pytest
from my_functions.stack import Stack


@pytest.fixture
def stack():
    return Stack()


def test_stack():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s) == 0


def test_push(stack):
    stack.push(5)
    stack.push(8)
    assert len(stack) == 2


def test_pop(stack):
    stack.push("foo")
    stack.push("bar")
    stack.pop()
    assert len(stack) == 1
    assert stack.pop() == "foo"
    assert stack.pop() is None
