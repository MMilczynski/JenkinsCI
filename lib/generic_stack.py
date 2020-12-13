"""This is a python example of a C# stack (LIFO) from the TDD course on pluralsight.

https://app.pluralsight.com/library/courses/test-driven-development-big-picture/table-of-contents
"""
from lib.base_stack import BaseStack


class GenericStack(BaseStack):
    """Stack containing generic-type elements."""

    def push(self, new_element):
        """Adds item to end of stack.
        """
        self._elements.append(new_element)
        self._counter += 1

    def pop(self):
        """Removes last element from stack and returns it. Will return None otherwise
        """
        if self._counter > 0:
            self._counter -= 1
            return self._elements.pop(self._counter)
        return None

    def reset(self):
        """Resets current stack.
        """
        self._elements = []
        self._counter = 0
