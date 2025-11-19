#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 13:09:16 2025

@author: mwilliams
"""

import numpy as np

from Body import body
from Body import eps

# setting the "far" parameter and softening parameter
theta = 1

# defining the class for a Barnes-Hut tree object
class tree:
    
    # initializing the object which is an empty region of space with four sub quadrants
    def __init__(self,quad):
        
        self.body = None
        self.quad = quad
        
        # subquadrants
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None
    
    # method to check if this node is a "leaf" or "external" node by checking for subquadrants
    def isexternal(self):
        if (self.nw == None and
            self.ne == None and
            self.sw == None and
            self.se == None):
            
            return True
        else:
            return False
    
    # defining method to find combined COM
    def combine_bodies(self, b1, b2):
        m1, m2 = b1.mass, b2.mass
        x_com = (b1.rx*m1 + b2.rx*m2)/(m1 + m2)
        y_com = (b1.ry*m1 + b2.ry*m2)/(m1 + m2)
        
        vx_com = (b1.vx*m1 + b2.vx*m2)/(m1 + m2)
        vy_com = (b1.vy*m1 + b2.vy*m2)/(m1 + m2)
        
        comcolor = b1.color # making the new body the color of the first body
        
        return body(x_com, y_com, vx_com, vy_com, m1 + m2, comcolor)

    
    # insert method puts a body in this barnes-hut tree node
    def insert(self,b):
        
        # if no body in this node:
        if self.body == None:
            self.body = b
            # an empty return statement might be needed here??
        
        # if there is already a body in this node
        # and the node is internal (combine with current body and place in correct subquad):
        elif not self.isexternal():
            self.body = self.combine_bodies(self.body, b)
            #self.body = self.body.add(self.body, b)
            
            # check which quadrant b is in 
            if b.inquad(self.quad.nw()):
                self.nw.insert(b)
            
            elif b.inquad(self.quad.sw()):
                self.sw.insert(b)
            
            elif b.inquad(self.quad.ne()):
                self.ne.insert(b)
            
            elif b.inquad(self.quad.se()):
                self.se.insert(b)
            
            # or if its an external node (create new trees):
        else:
            c = self.body # c is the body that was already there
            
            # make 4 subquads
            self.nw = tree(self.quad.nw())
            self.sw = tree(self.quad.sw())
            self.se = tree(self.quad.se())
            self.ne = tree(self.quad.ne())
            
            # put body c in one of this tree's subquads
            if c.inquad(self.nw.quad):
                self.nw.insert(c)
            
            if c.inquad(self.sw.quad):
                self.sw.insert(c)
            
            if c.inquad(self.ne.quad):
                self.ne.insert(c)
            
            if c.inquad(self.se.quad):
                self.se.insert(c)
            
            # put body b in one of this tree's subquads
            if b.inquad(self.nw.quad):
                self.nw.insert(b)
            
            if b.inquad(self.sw.quad):
                self.sw.insert(b)
            
            if b.inquad(self.ne.quad):
                self.ne.insert(b)
            
            if b.inquad(self.se.quad):
                self.se.insert(b)
                
            # combine cuurent body and new body for internal node 
            self.body = self.combine_bodies(c, b)
            
                
            # clear old body and insert new body
            #self.body = None
            #self.insert(b)
        
    def update_force(self,b):
        if self.isexternal():
            if (self.body is not None) and (self.body != b):
                b.addforce(self.body)
                
                # return statement added for type error
                return np.array([b.fx,b.fy])

       
        # approximation for "far" force contributions
        else:
            if (self.quad.length /self.body.distance_to(b,eps)) < theta : 
                b.addforce(self.body)
                return np.array([b.fx,b.fy])
            
            else:
                if self.nw != None:
                    self.nw.update_force(b)
                if self.sw != None:
                    self.sw.update_force(b)
                if self.ne != None:
                    self.ne.update_force(b)
                if self.se != None:
                    self.se.update_force(b)
                
            # return updated forces from b after all children
            return np.array([b.fx, b.fy])
    
    # converting to string representation
    def tostring(self):
        if any([self.nw, self.sw, self.ne, self.se]):
            return "*" + str(self.body) + "\n" + \
               str(self.nw or "") + \
               str(self.ne or "") + \
               str(self.sw or "") + \
               str(self.se or "")
        else:
            return " " + str(self.body) + "\n"
