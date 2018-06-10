# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:45:59 2018

plotting taken from " Introduction to python for Engineers" By Sandeep Nagar, Apress

@author: SIDHARTH
"""

import numpy as np
from matplotlib import pylab as pl

pl.figure(figsize=(9,7), dpi=100)
pl.subplot(1,1,1)
X = np.linspace(-np.pi*2, np.pi*2,10e4,endpoint=True)
S , S2 = np.sin(X), np.cos(X)
pl.plot(X,S,color ="blue", linewidth=1.0,linestyle="-",label="$sin(x)$")
pl.plot(X,S2,color="red", linewidth=1.5,linestyle="--",label="$sin(2x)$")
pl.xlim(-2*np.pi,2.5*np.pi)
pl.xticks(np.linspace(-2.5*np.pi,2.5*np.pi,9,endpoint=True))
pl.ylim(-1.2,1,2)
pl.yticks(np.linspace(-1,1,5,endpoint=True))
pl.title('$sin(x)$ and $cos(x)$ waves')
pl.ylabel('$sin(x)$ and $cos(x)$')
pl.xlabel('$x$')
pl.grid(True)
pl.legend()
pl.show()
