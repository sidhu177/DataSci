# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:25:48 2018

Taken from "Introduction to Python for Engineers" by Sandeep Nagar, Apress

@author: SIDHARTH
"""

import matplotlib.pyplot as pl
import numpy as np

pl.figure()
a = np.random.randn(50)
pl.hist(a,15)
pl.show
