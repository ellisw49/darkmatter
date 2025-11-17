#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 18:58:39 2025

@author: mwilliams

This is good I think - bug free 
"""
'''
import numpy as np

# quadrant objects for barnes-hut tree method

class quad:
    
    def __init__(self, xmid, ymid, length):
        self.xmid = float(xmid)  # Make these float
        self.ymid = float (ymid)
        self.length = float(length)
    
    # method to check the length
    def length(self):
        return #length
    
    
    # check if this quadrant contains a given point
    def contains(self,xmid,ymid):
        # is true if there is a point in the quadrant
        
        if (xmid <= self.xmid + self.length / 2.0 and
        xmid >= self.xmid - self.length / 2.0 and
        ymid <= self.ymid + self.length / 2.0 and
        ymid >= self.ymid - self.length / 2.0):
            return True
        else: 
            return False
        
    
    # subdivide this quad into 4 subquadrants: NW, SW, NE, SE
    # creates a norhtwest quadrant shifted left and up
    def nw(self):
        return quad(self.xmid - self.length / 4.0,
            self.ymid + self.length / 4.0,
            self.length / 2.0)    

    # creates a southwest quadrant shifted left and down
    def sw(self):
        return quad(self.xmid - self.length / 4.0,
            self.ymid + self.length / 4.0,
            self.length / 2.0)
    # creates a northeast quadrant shifted right and up
    def ne(self):
        return quad(self.xmid - self.length / 4.0,
            self.ymid + self.length / 4.0,
            self.length / 2.0)
    # creates a norhtwest quadrant shifted right and down
    def se(self):
        return quad(self.xmid - self.length / 4.0,
            self.ymid + self.length / 4.0,
            self.length / 2.0)

'''

import numpy as np

class quad:
    
    def __init__(self, xmid, ymid, length):
        self.xmid = float(xmid)  # Make these float
        self.ymid = float(ymid)
        self.length = float(length)
    
    # method to check the length
    def length(self):
        return self.length  # fixed to actually return the length
    
    
    # check if this quadrant contains a given point
    def contains(self, xmid, ymid):
        # is true if there is a point in the quadrant
        
        if (xmid <= self.xmid + self.length / 2.0 and
        xmid >= self.xmid - self.length / 2.0 and
        ymid <= self.ymid + self.length / 2.0 and
        ymid >= self.ymid - self.length / 2.0):
            return True
        else: 
            return False
        
    
    # subdivide this quad into 4 subquadrants: NW, SW, NE, SE
    # creates a northwest quadrant shifted left and up
    def nw(self):
        return quad(self.xmid - self.length/4.0,
                    self.ymid + self.length/4.0,
                    self.length/2.0)    

    # creates a southwest quadrant shifted left and down
    def sw(self):
        return quad(self.xmid - self.length/4.0,
                    self.ymid - self.length/4.0,
                    self.length/2.0)
    # creates a northeast quadrant shifted right and up
    def ne(self):
        return quad(self.xmid + self.length/4.0,
                    self.ymid + self.length/4.0,
                    self.length/2.0)
    # creates a southeast quadrant shifted right and down
    def se(self):
        return quad(self.xmid + self.length/4.0,
                    self.ymid - self.length/4.0,
                    self.length/2.0)
