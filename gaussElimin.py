# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:47:16 2018

Taken from Numerical Methods in Engineering, Cambridge, 2013, Jaan Kiusalaas

@author: SIDHARTH
"""

import numpy as np

def gaussElimin(a,b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
                
    for k in range(n-1,-1,-1):
        b[k] = (b[k]-np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b