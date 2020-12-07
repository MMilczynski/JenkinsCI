"""This is a python example of a C# stack (LIFO) from the TDD course on pluralsight.

https://app.pluralsight.com/library/courses/test-driven-development-big-picture/table-of-contents
"""


class GenericStack:
    """Stack containing generic-type elements
    """

    def __init__(self):
        """
        """
        self._items = []
        self._counter = 0

    def push(self, item):
        """Adds item to end of stack.
        """
        self._items.append(item)
        self._counter = len(self._items)

    def pop(self):
        """Removes last element from stack and returns it. Will return None otherwise
        """
        if self._counter > 0:
            self._counter -= 1
            return self._items.pop(self._counter)
        else:
            return None
