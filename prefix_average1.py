# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 21:46:33 2018

@author: SIDHARTH
"""

def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total/(j+1)
    return A