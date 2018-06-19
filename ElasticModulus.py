# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 19:56:36 2018

Given Force, length, width and cross-sectional area and ellongation calculates Young's Modulus

@author: SIDHARTH
"""

f = eval(input('Input Force in Newtons\n'))
A = eval(input('Cross Sectional Area in Meter Square\n'))
dl = eval(input('ellongation in meters\n'))
l = eval(input('length in meters\n'))

'''stress is force by area'''
P = f/A
'''Strain is ellongation by length'''
e = dl/l
'''Young's Modulus'''
E = P/e
print('Youngs Modulus is ', E)


