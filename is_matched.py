# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 04:16:06 2023

@author: gj
"""
import ArrayStack

def is_matched(expr):
    """Return true if all delimiters are
    properly match; False otherwise."""
    
    lefty = "({[" #opening delimiters
    righty = ")}]" # respective closing delimiters
    S = ArrayStack.ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
            
    return S.is_empty()
