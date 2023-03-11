# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 23:53:11 2023

@author: gj
"""
import ctypes

#--------------------Class Empty--------------------------
class Empty(Exception):
    """Error attempting to access an
    element from an empty container"""
    pass

#---------------------Class DynamicArray---------------------
class DynamicArray:
    """ A dynamic array class as a simplified Python list """
    def __init__(self):
        """Create an empty array."""
        self._n = 0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity)
        # low-level array
        
    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """Return the item at position k"""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k] # retreive from array
    
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            # not enough room
            self._resize(2*self._capacity)
        # so double capacity
        self._A[self._n] = obj
        self._n += 1
        
    def _resize(self, c):
        """Resize internal array to capacity c"""
        B= self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def _make_array(self,c):
        """Return new array with capacity c."""
        return (c*ctypes.py_object)()

#--------------------Class ArrayStack---------------------
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
        """return (but not remove) the element
        from the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

#------------------Function reverse_file--------------------
def reverse_file(filename):
    """Overwrite given file with its contents
    line-by-line reversed"""
    
    S = ArrayStack()
    original = open(filename)
    
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()
        
    # now we overwrite with contents in LIFO order
    output = open(filename, "w")
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()
    
#------------------Function is_matched--------------------
def is_matched(expr):
    """Return true if all delimiters are
    properly match; False otherwise."""
    
    lefty = "({[" #opening delimiters
    righty = ")}]" # respective closing delimiters
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
            
    return S.is_empty()

#------------------Function is_matched_html--------------------
def is_matched_html(raw):

    """Return True if all HTML tags are
    properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find(">", j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        
        if not tag.startswith("/"):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j=raw.find("<", k+1)
    return S.is_empty()
    
#---------------Class ArrayQueue----------------
class ArrayQueue():
    """ FIFO queue implementation using a Python
    list as underlying storage"""
    
    DEFAULT_CAPACITY = 10
    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return (but not remove) the
        element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[self._front]
    
    def dequeue(self):
        """Remove and return the first element
        of the queue (i.e. FIFO).
        Raise Empty exception if the queue is empty"""
        
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
        
    def enqueue(self, e):
        
        # Add an element to the back of queue.
        if self._size == len(self._data):
            self.resize(2 *len(self._data)) # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def _resize(self, cap): # we assume cap >= len(self)
    
        # Resize to a new list of capacity >= len(self).
        old = self._data # keep track of existing list
        self._data = [None] * cap # allocate list with new capacity
        walk = self._front
        for k in range(self._size): # only consider existing elements
            self._data[k] = old[walk] # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulus
        self._front = 0 # front has been realigned

#----------------Class LinkedStack----------------------
class LinkedStack(ArrayQueue):
    
    """LIFO Stack implementation using
    a singly linked list for storage"""
    # ------------ nested _Node class -----------
    class _Node:
        """ Lightweight, nonpublic class
        for storing a singly linked node."""
    
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    #-------------- stack methods ------------------
    
    def __init__(self):
        """ Create an empty stack."""
        super().__init__()
        self._head = None
        self._size = 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1
    
    def top(self):
        """ Return (but not remove) the element
        at the top of the stack
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element
    
    def pop(self):
        """Remove and return the element
        at the top of the stack (LIFO).
        Raise Empty exception if the stack is empty."""
        
        
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


#----------------Class LinkedQueue-----------------------
class LinkedQueue(ArrayQueue):
    """FIFO queue implementation using
    a singly linked list for storage """
    
    class _Node:
        """ Lightweight, nonpublic class
        for storing a singly linked node."""
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0
    
    def first(self):
        """Return (but not remove)
        the element at the front of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty( ):
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty( ): # special case as queue is empty
            self._tail = None # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None) # node will be new tail node
        if self.is_empty():
            self._head = newest # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest # update reference to tail node
        self._size += 1

#---------------------Class CircularQueue---------------------
class CircularQueue(LinkedQueue):
    """Queue implementation using
    circularly linked list for storage"""
    class _Node:
        """Lightweight, nonpublic class
        for storing a singly linked node
        (omitted here; identical to that
        of LinkedStack._Node)"""
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        """ Create an empty queue"""
        self._tail = None
        self._size = 0
    
    def first(self):
        """Return (but not remove)
        the element at the front of
        the queue. Raise Empty
        exception if the queue is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element
        
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty( ):
            raise Empty("Queue is empty")
        oldhead = self._tail._next
        if self._size == 1: # removing only element
            self._tail = None # queue becomes empty
        else:
            self._tail._next = oldhead._next # bypass the old head
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None) # node will be new tail node
        if self.is_empty( ):
            newest._next = newest # initialize circularly
        else:
            newest._next = self._tail._next # new node points to head
            self._tail._next = newest # old tail points to new node
        self._tail = newest # new node becomes the tail
        self._size += 1
        
    def rotate(self):
        """"Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next

#----------------Class _DoublyLinkedBase-----------------------
class _DoublyLinkedBase(ArrayQueue):
    """ A base class providing a doubly
    linked list representation"""
    class _Node:
        """Ligthweight, nonpublic class
        for storing q doubly linked node"""
        __slots__ = "_element", "_prev", "_next"
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing
        nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size +=1
        return newest
    
    def _delete_node(self, node, predeccessor):
        """Delete nosentinel node from
        the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predeccessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


#----------------Class LinkedDequeue-----------------------
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

