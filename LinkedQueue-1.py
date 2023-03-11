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

if __name__=='__main__':
    Linkedqueue=LinkedQueue()
    Linkedqueue.enqueue(4)
    Linkedqueue.enqueue(6)
    Linkedqueue.enqueue(6)
    Linkedqueue.enqueue(1)

    print(Linkedqueue.__len__())