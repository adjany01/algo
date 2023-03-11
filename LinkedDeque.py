# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 04:50:49 2023

@author: gj
"""

import _DoublyLinkedBase

class Empty(Exception):
    """Error attempting to access an
    element from an empty container"""
    pass

class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation
    based on a doubly linked list """
    def first(self):
        """Return (but not remove) the element
        at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element
    
    def last(self):
        """Return (but not remove) the
        element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header_next)
    
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer
        
    def delete_first(self):
        """Remove and return the element from the
        front of the deque.
        Raise Empty exception if deque is empty."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete._node(self._header._next)
    
    def delete_last(self):
        """Remove and return the element from the
        back of the deque.
        Raise Empty exception if deque is empty."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
