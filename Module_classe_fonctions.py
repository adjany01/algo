#---------CLASSE ArrayQueue--------------

class ArrayQueue:
    """FIFO queue implementation using a Python lis as underlying storage"""
    DEFAULT_CAPACITY=10

    def __init__(self):
        """create an empty queue"""

        self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
        self._size=0
        self._front=0

    def __len__(self):
        """return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""

        return self._size==0

    def first(self):
        """Return the element at the front of the queue"""

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue"""

        if self.is_empty():
            raise Empty('Queue is empty')
        answer=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size -=1
        return answer

    def enqueue(self,e):
        """Add an element to the back of the queue"""
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size +=1

    def _resize(self,cap):
        """Resize to a new list of capacity"""

        old=self._dataself._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0

#--------CLASSE ArrayStack--------

class ArrayStack:
    """LIFO stack implementation using a python list as underlying storage"""
    
    def __init__(self):
        """create an empty"""
        self._data=[]
    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data)==0
    
    def push(self,e):
        """Return but not remove the element at the top of the stack"""
        self._data.append(e)
        
    def top(self):
        """Return (but not remove) the element at the top of the stack.
        Raise Empty Exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def reverse_file(self,filename):
        S=ArrayStack()
        original=open(filename)
        for line in original:
            S.push(line.rstrip('\n'))
        original.close()
    
    def pop(self):
        """Remove and return the element from the top of the LIFO"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

        #now we overwrite with content in LIFO order
        output=open(filename,'w')
        while not S.is_empty():
            output.write(S.pop() + '\n')
        output.close()
        return
    def somme(self,a,b):
        print(a+b)

#-----CLASSE DynamicArray----------

import ctypes
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
        return self._n #retreive from array
    def __getitem__(self, k):
        """Return the item at position k"""
        if not 0 <= k < self._n:
            print('invalid index')
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

#-------classe LinkedStack----------

class LinkedStack:
    """LIFO stack implementation using a singly linked list for storage"""

    #------------------nested_Node class--------------

    class _Node:
        """Lighweight, nonpublic class for storing a singly linked node"""
        __slots__='_element','_next' #Rationaliser l'usage de la memoire

        def __init__(self,element,next): #initialise le champ des noeuds
            self._element=element       #reference a l'element utilisateur
            self._next=next              #reference au noeud siuvant
            
    #-----------------------
    def __init__(self):
        """creation d'une pile vide"""
        self._head=None
        self._size=0

    def __len__(self):
        """Retourne le nombre d'elements dans la pile"""
        return self._size

    def is_empty(self):
        """Vrai si la pile est vide"""
        return self._size==0

    def push(self,e):
        """Ajouter l'element e au sommet de la liste"""
        self._head=self._Node(e,self._head) #creer et lier au nouveau noeud
        self._size +=1

    def top(self):
        """Retourne l'element au sommet de la liste"""
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element

    def pop(self):
        """Supprime et retourne l'element depuis le sommet de laliste"""

        if self.is_empty():
            raise Empty('Stack is empty')
        answer=self._head._element
        self._head=self._head._next
        self._size -=1
        return answer

#-------LinkedQueue----------

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""

    class _Node:
        __slots__='_element','_next'

        def __init__(self,element,next):
            self._element=element
            self._next=next
    
    def __init__(self):
        """create an empty queue"""
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        """return the number of element in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is emty"""

    def first(self):
        """Return the element at the front of the queue"""

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """remove and return the first element of the queue"""

        if self.is_empty():
            raise Empty('Queue is empty')
        answer=self._head._element
        self._head=self._head._next
        self._size -=1
        if self.is_empty():
            self._tail=None
        return answer

    def enqueue(self,e):
        """Add an element to the back of the queue"""

        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest
        else:
            self._tail=newest
        self._tail=newest
        self._size +=1