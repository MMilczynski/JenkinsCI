"""This is a very simple app.
"""
import numpy as np

from lib.generic_stack import GenericStack


def stack_operations():
    """Fills stack with some items and empty it afterwards.
    """
    # create stack
    stack = GenericStack()

    # fill stack with content
    stack.push([1, 2, 3, 4, 5])
    stack.push(np.array([1, 2, 3, 4, 5]))

    print('Finished filling stack')

    # empty stack
    stack.pop()
    stack.pop()

    print('Finished emptying stack')


if __name__ == '__main__':
    stack_operations()
