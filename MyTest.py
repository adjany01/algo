# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:55:40 2023

@author: gj
"""

import Module
import unittest

#----------------Teste des fonctions de la classe DynamicArray-------------

class TestDynamicArray(unittest.TestCase):
    
    def testlen(self):
        A = Module.DynamicArray()
        self.assertEqual(A.__len__(),0)
    
    def testAppend(self):
        A = Module.DynamicArray()
        A.append(20) # Ajout d'un element
        self.assertEqual(A.__len__(),1)
        
#----------------Teste des fonctions de la classe ArrayStack---------------
    
class TestArrayStack(unittest.TestCase):
    
    def testMutiple(self):
        """ teste des fonctions: push(), pop(), top(),
        is_empty() et __len__()"""
        
        As = Module.ArrayStack()
        for i in range(1,4):
            As.push(i)
        As.pop()
        self.assertEqual(As.top(),2)
        self.assertEqual(As.__len__(),2)
        self.assertFalse(False, As.is_empty)
        
#---------------------Teste de la fonction reverse_file-------------------

class Testfunct1(unittest.TestCase):
    
    def testReverse(self):
        pass

#----------------------Teste de la fonction is_matched-------------------

class Testfunct2(unittest.TestCase):
    
    def testIs_m(self):
        pass

#-------------------Teste de la fonction is_matched_html-------------------

class Testfunct3(unittest.TestCase):
    
    def testIs_mHTML(self):
        pass

#--------------Teste des fonctions de la classe ArrayQueue-----------------

class TestArrayQueue(unittest.TestCase):
    
    def testMutiple1(self):
        """teste des fonctions: enqueue(e), dequeue(), first(),
        is_empty(), __len__()"""
        Aq = Module.ArrayQueue()
        for k in range(1,4):
            Aq.enqueue(k)
        Aq.dequeue()
        self.assertEqual(Aq.first(), 2)
        self.assertEqual(Aq.__len__(),2)
        self.assertFalse(False, Aq.is_empty)

#--------------Teste des fonctions de la classe LinkedStack-----------------

class TestLinkedStack(unittest.TestCase):
    
    def testMultiple2(self):
        """teste des fonctions: push(), pop(), top(), __len__(),
        """
        Ls = Module.LinkedStack()
        Ls.push(10)
        Ls.push("Python")
        Ls.push("est")
        Ls.push("un langage de programmation")
        Ls.pop()
        Ls.top()
        Ls.top()
        self.assertEqual(Ls.__len__(),3)
        self.assertFalse(False, Ls.is_empty)

#--------------Teste des fonctions de la classe LinkedQueue-----------------

class TestLinkedQueue(unittest.TestCase):
    
    def testMultipe3(self):
        """teste des fonctions: enqueue(e), dequeue(), first(),
        is_empty(), __len__()"""
        Lq = Module.LinkedQueue()
        for k in range(1,4):
            Lq.enqueue(k)
        Lq.dequeue()
        self.assertEqual(Lq.first(), 2)
        self.assertEqual(Lq.__len__(),2)
        self.assertFalse(False, Lq.is_empty)

#--------------Teste des fonctions de la classe CircularQueue--------------

class TestCircularQueue(unittest.TestCase):
    
    def testmMultuole5(self):
        """teste des fonctions: enqueue(e), dequeue(), first(),
        is_empty(), __len__()"""
        Cq = Module.CircularQueue()
        for k in range(1,4):
            Cq.enqueue(k)
        Cq.dequeue()
        self.assertEqual(Cq.first(), 2)
        self.assertEqual(Cq.__len__(),2)
        self.assertFalse(False, Cq.is_empty)

#-----------Teste des fonctions de la classe _DoublyLinkedBase-------------

class Test_DoublyLinkedBase(unittest.TestCase):
    
    def testMultiple4(self):
        """teste des fonctions: is_empty(), __len__(), """
        Dl = Module._DoublyLinkedBase()
        self.assertFalse(False, Dl.is_empty)
        self.assertEqual(Dl.__len__(),0)

#--------------Teste des fonctions de la classe LinkedDeque--------------

class TestLinkedDeque(unittest.TestCase):
    
    def testmMultuole5(self):
        Ld = Module.LinkedDeque()
        self.assertFalse(False, Ld.is_empty)
        self.assertEqual(Ld.__len__(),0)


if __name__=='__main__':
    unittest.main()