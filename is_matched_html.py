# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 04:19:06 2023

@author: gj
"""
import ArrayStack

def is_matched_html(raw):

    """Return True if all HTML tags are
    properly match; False otherwise."""
    S = ArrayStack.ArrayStack()
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
