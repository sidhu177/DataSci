# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:31:53 2018

parsing Text File Taken from "Beginning Python Visualization by Shai Vaingast, Apress"
"""

def srchfile(filename,substr):
    lines = open(filename).readlines()
    fmt = r'%' + str(int((len(lines)))+1)+r'd:%s'
    for index, line in enumerate(lines):
        if line.find(substr)!=-1:
            try:
                print(fmt % (index,line.rstrip()))
            except UnicodeEncodeError:
                print("%d: ---- encoding error ---" %index)
                
