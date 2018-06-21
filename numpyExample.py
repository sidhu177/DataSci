# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:53:44 2018

@author: SIDHARTH
"""

import numpy as np
x1 = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
x2 = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
x_angle = np.array([30, 60, 90, 120, 150, 180])
x_sqr = np.array([9, 16, 25, 225, 400, 625])
x_bit = np.array([2, 4, 8, 16, 32, 64])
a = np.greater_equal(x1,x2)
b = np.mod(x1,x2)
c = np.exp(x1)
d = np.reciprocal(x1)
e = np.negative(x1)
f = np.isreal(x1)
g = np.sqrt(np.square(x_sqr))
h = np.sin(x_angle*np.pi/180)
i = np.tan(x_angle*np.pi/180)
j = np.right_shift(x_bit,1)
k = np.left_shift (x_bit,1)
print(a,b,c,d,e,f,g,h,i,j,k)