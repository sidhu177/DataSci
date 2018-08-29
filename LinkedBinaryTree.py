# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:25:06 2018

Taken from Data structures and algorithms using Python

@author: SIDHARTH
"""

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element','_parent','_left','_right'
        def __init__(self,element,parent=None,left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            
    class Position(BinaryTree.Position):
        def __init__(self,container,node):
            self._container = container
            self._node = node
            
        def element(self):
            return self._node._element
            
        def __eq__(self,other):
            return type(other) is type(Self) and other._node is self._node
            
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
        
    def _make_position(self,node):
        return self.Position(self,node) if node is not None else None