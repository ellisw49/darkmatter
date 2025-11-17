#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 13:09:16 2025

@author: mwilliams
"""

import numpy as np

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
    
    # insert method puts a body in this barnes-hut tree node
    def insert(self,b):
        
        # if no body in this node:
        if self.body == None:
            self.body = b
            # an empty return statement might be needed here??
        
        # if there is already a body in this node
        # and the node is internal (combine with current body and place in correct subquad):
        elif not self.isexternal():
            self.body = self.body.add(self.body, b)
            
            # check which quadrant b is in 
            if b.inquad(self.quad.nw()):
                if self.nw == None:
                    self.nw = tree(self.quad.nw)
                self.nw.insert(b)
            
            elif b.inquad(self.quad.sw()):
                if self.sw == None:
                    self.sw = tree(self.quad.sw)
                self.sw.insert(b)
            
            elif b.inquad(self.quad.ne()):
                if self.ne == None:
                    self.ne = tree(self.quad.ne)
                self.ne.insert(b)
            
            elif b.inquad(self.quad.se()):
                if self.se == None:
                    self.se = tree(self.quad.se)
                self.se.insert(b)
            
            # or if its an external node (create new trees):
            else:
                c = self.body # c is the body that was already there
                
                # put body c in a new tree (one of this tree's subquads)
                if c.inquad(self.quad.nw()):
                    if self.nw is None:
                        self.nw = tree(self.quad.nw)
                    self.nw.insert(c)
                
                if c.inquad(self.quad.sw()):
                    if self.sw is None:
                        self.sw = tree(self.quad.sw)
                    self.sw.insert(c)
                
                if c.inquad(self.quad.ne()):
                    if self.ne is None:
                        self.ne = tree(self.quad.ne)
                    self.ne.insert(c)
                
                if c.inquad(self.quad.se()):
                    if self.se is None:
                        self.se = tree(self.quad.se)
                    self.se.insert(c)
                
            # clear old body and insert new body
            self.body = None
            self.insert(b)
        
    def update_force(self,b):
        if self.isexternal():
            if self.body != b:
                b.addforce(self.body)
       
        # approximation for "far" force contributions
        else:
            if (self.quad.length /self.body.distance_to(b)) < 2:
                b.addforce(self.body)
            else:
                if self.nw != None:
                    self.nw.update_force(b)
                if self.sw != None:
                    self.sw.update_force(b)
                if self.ne != None:
                    self.ne.update_force(b)
                if self.se != None:
                    self.se.update_force(b)
    
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
