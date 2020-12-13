"""Module containing a baseline stack class.
"""


class BaseStack:
    """Simple baseline stack class."""

    def __init__(self, new_elements=None):
        """Contruct instance.

        Attributes:
            _elements: holds elements, list
            _counter: contains current number of elements, int

        Args:
            none
        """
        self._elements = []
        if new_elements is not None:
            self._elements = new_elements
        self._counter = len(self._elements)

    def length(self):
        """Returns number of elements in stack."""
        return self._counter
