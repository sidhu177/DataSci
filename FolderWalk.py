# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:06:40 2018

Taken From Automate the boring Stuff using Python, By Al Sweigart, No Starch Press, 2014 

@author: SIDHARTH
"""

import os

for folderName, subfolders, filenames in os.walk('E:\\temp'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF' + folderName + ':' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ':'+ filename)
        
    print('')