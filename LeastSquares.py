# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:53:44 2018

Taken from Mastering Python for Finance

@author: SIDHARTH
"""

import numpy as np

A = np.array([[2,1,1],[1,3,2],[1,0,0]])
B = np.array([4,5,6])
C = np.linalg.solve(A,B)
print(C)