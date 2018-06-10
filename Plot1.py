# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:45:59 2018

plotting

@author: SIDHARTH
"""

import numpy as np
from matplotlib import pylab as pl

x = np.linspace(0,100)
y1 = x**3 
y2 = x**2
pl.plot(x,y1)
pl.plot(x,y2)
pl.show()
