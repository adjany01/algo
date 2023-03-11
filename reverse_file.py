# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 04:14:12 2023

@author: gj
"""
import ArrayStack

def reverse_file(filename):
    """Overwrite given file with its contents
    line-by-line reversed"""
    
    S = ArrayStack.ArrayStack()
    original = open(filename)
    
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()
        
    # now we overwrite with contents in LIFO order
    output = open(filename, "w")
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()