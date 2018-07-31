# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 23:37:28 2018

@author: SIDHARTH
"""

def scale(data, factor):
    ''' Multiply all entries of numeric data list by the given factor.
    
    data  : an instance of any sequence containing numbers
    factor: used to multiply for scaling
    '''
    for j in range(len(data)):
        data[j]*=factor
        
    print(data)