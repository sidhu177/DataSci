# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:25:48 2018

Taken from "Python Data Analyst" by Sandeep Nagar, Apress

@author: SIDHARTH
"""

import matplotlib.pyplot as pl
import numpy as np

x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(3*x)/x
pl.plot(x,y,'k--', linewidth=3)
pl.plot(x,y2,'m-.')
pl.plot(x,y3,color='#87a3cc',linestyle='-')
