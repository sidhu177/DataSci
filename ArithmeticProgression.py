# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:01:18 2018

@author: SIDHARTH
"""

class ArithmeticProgression(Progression):
    def __init__(self,increment=1,start=0):
        super().__init__(start)
        self._increment = increment 
        
    def _advance(self):
        self._current += self._increment