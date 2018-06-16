# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 11:28:33 2018

Taken From Python 3 Object Oriented Programming, Dusty Phillips, Packt Publishing,2015

@author: SIDHARTH
"""

def format_string(string,formatter=None):
    class Default:
        def format(self, string):
            return str(string).title()
                
    if not formatter:
        formatter = Default()
        
    return formatter.format(string)
    
Input_string = input('Enter the String\n')
print("Input String: " + Input_string)
print("Output String: " + format_string(Input_string))
