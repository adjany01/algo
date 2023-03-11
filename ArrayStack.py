# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 04:10:22 2023

@author: gj
"""

class Empty(Exception):
    """Error attempting to access an
    element from an empty container"""
    pass


class ArrayStack:
    """ LIFO stack implementation using
    a Python list as underlying storage"""
    
    def __init__(self):
        """ Create an empty stack"""
        self._data = []
        
    def __len__(self):
        """Return the number of
        elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to top of the stack"""
        self._data.append(e)
    
    def top(self):
        """Remove and return the element
        from the top of the stack (i.e. LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack
        (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

