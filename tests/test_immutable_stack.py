"""Tests using pytest for ImmutableStack operations.
"""
import numpy as np
from lib.immutable_stack import ImmutableStack


def test_push():
    """Test to check that new ImmutableStack instance is created
       upon push operation.
    """
    stack = ImmutableStack()
    new_stack = stack.push(1)
    assert id(stack) != id(new_stack)
    assert stack.length() == 0
    assert new_stack.length() == 1
    assert stack.peek() is None
    assert new_stack.peek() == 1
