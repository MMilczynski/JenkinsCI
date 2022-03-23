"""Module implementing immutable stack.

For more infor see:
https://app.pluralsight.com/library/courses/test-driven-development-big-picture/table-of-contents
"""
from lib.base_stack import BaseStack


class ImmutableStack(BaseStack):
    """An immutable stack is not supposed to change its state. The push and pop 
       methods should therefore return a new stack instance. Compared to the 
       GenericStack the Immuatble Stack should have an additional peek method to
       return the top-most element.  
    """

    def push(self, new_element):
        """Returns new stack with pushed element

        Args:
            new_element: object

        Returns:
            new ImmutableStack instance
        """
        new_elements = self._elements[:]
        new_elements.append(new_element)
        return ImmutableStack(new_elements=new_elements)

    def peek(self):
        """Returns top-most element

        Args:

        Returns:
            top-most element otherwise None if empty
        """
        if self._counter > 0:
            return self._elements[self._counter - 1]
        return None

    def pop(self):
        """Returns new instance of ImmutableStack with one element less.

        Args:
            none

        Returns:
            new ImmutableStack instance
        """
        new_elements = self._elements[:]
        new_elements.pop()
        return ImmutableStack(new_elements=new_elements)
