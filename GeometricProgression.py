# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:04:08 2018

@author: SIDHARTH
"""

class GeometricProgression(Progression):
    def __init__(self,base=2,start=1):
        super().__init__(start)
        self._base = base
        
    def _advance(self):
        self._current *= self._base