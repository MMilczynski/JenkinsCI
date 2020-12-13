"""Tests using pytest for GenericStack operations.
"""
import numpy as np
import pytest

from lib.generic_stack import GenericStack


@pytest.fixture
def stack_init():
    """Create empty stack.

    Args:
        none

    Returns:
        stack : GenericStack empty
    """
    return GenericStack()


@pytest.fixture
def stack_with_content():
    """Create stack, fill it with content and return it

    Args:
        none

    Returns:
        stack : GenericStack, has some conten
    """
    stack = GenericStack()
    stack.push(1)
    stack.push("2")
    stack.push(np.array([1, 2, 3, 4, 5]))
    return stack


def test_pop(stack_with_content):
    """Tests the pop operation of our stack.

    Args:
        stack_with_content : pytest.fixture

    Returns:
        none
    """
    assert np.array_equal(stack_with_content.pop(), np.array([1, 2, 3, 4, 5]))
    assert stack_with_content.pop() == "2"
    assert stack_with_content.pop() == 1


def test_push(stack_init):
    """Tests push operation on stack.

    Args:
        stack_init : pytest.fixture

    Returns:
        none
    """
    stack_init.push(1)
    stack_init.push([1, 2, 3, 4, 5])

    assert stack_init.pop() == [1, 2, 3, 4, 5]
    assert stack_init.pop() == 1


def test_empty_stack_init(stack_init):
    """Tests empty stack behavior on empty stack.

    Args:
        stack_init : pytest.fixture

    Returns:
        none
    """
    assert stack_init.pop() is None


def test_empty_stack_with_content(stack_with_content):
    """Tests empty stack behavior on stack with some content.

    Args:
        stack_with_content : pytest.fixture

    Returns:
        none
    """
    stack_with_content.pop()
    stack_with_content.pop()
    stack_with_content.pop()

    assert stack_with_content.pop() is None


def test_stack_reset(stack_with_content):
    """Tests reset operation on stack with content.
    """
    stack_with_content.reset()

    assert stack_with_content.pop() is None
