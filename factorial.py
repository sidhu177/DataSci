# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:16:33 2018

@author: SIDHARTH
"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
        
'''Power Rule'''
def power(x,n):
    if n==0:
        return 1
    else:
        return x * power(x,n-1)