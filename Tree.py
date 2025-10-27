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
        
        # if the node is internal:
        elif not 