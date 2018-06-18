# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 22:08:58 2018

Taken from Python 3 Object Oriented Programming,Dusty Phillips, Packt

@author: SIDHARTH
"""

import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)
        
class Polygon:
    def __init__(self):
        self.vertices = []
    def add_point(self,point):
        self.vertices.append((point))
    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
        