# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 19:55:08 2017

Root Mean Square with For and While

@author: SIDHARTH
"""

import numpy as np
from numpy import sqrt
x = [1,2,3,4,5,6,7,8,9,10]
def rms(x):
    index = 0
    sigma = 0
    while index <len(x):
        acc = x[index]**2
        sigma = acc + sigma
        index += 1    
    rms = sqrt(sigma/len(x))
    return rms
def frms(x):
    sigma = 0
    for i in x:
        acc = i**2
        sigma = acc + sigma
    rms = sqrt(sigma/len(x))
    return rms
Tol = 0.0001
print('While RMS value', rms(x))
print('For RMS value', frms(x))
Calc = abs(rms(x)-frms(x))
if Tol>Calc:
    print('For and While match')
else:
     print('Tolerance Exceeded')