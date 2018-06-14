# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:57:36 2018

Taken From Automate the boring Stuff using Python, By Al Sweigart, No Starch Press, 2014

@author: SIDHARTH
"""

import zipfile, os
os.chdir('E:\\')
tempZip = zipfile.ZipFile('temp.zip')
tempZip.extractall()
tempZip.close()