#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 18:22:09 2025

@author: mwilliams
"""

import numpy as np

class body:
    
    # defining class-wide variables G and solar mass
    G = 6.673e-11
    solarmass=1.98892e30
    
    # initializing body object with position, velocity, mass, color
    def  __init__(self, rx, ry, vx, vy, mass, color):
        
        self.rx = rx
        self.ry = ry
        self.vx = vy
        self.vy = vy
        self.mass = mass
        self.color = color
    
    # update method completes one time step
    def update(self,dt):
        
        vx += dt * fx / mass
        vy += dt * fy / mass
        rx += dt * vx
        ry += dt * vy
    
    # distance_to calculates the distance between this body and other body
    def distance_to(self, other):
        
        dx = self.rx - other.rx
        dy = self.ry - other.ry
        return np.sqrt(dx **2 + dy **2)
    
    # zeroing force between iterations
    def resetforce(self):
        fx = 0.0
        fy = 0.0
        
    # calculating the force between this body and other body
    def addforce(self,other):
        # calculating distance between the particles
        dx = other.rx - self.rx
        dy = other.ry - self.ry
        dist = np.sqrt(dx**2 + dy**2)
        # calculating gravitational force
        f = G * (self.mass * other.mass) / (dist**2)
        # adding this force to this body
        self.fx += F * dx / dist
        self.fy += F * dy / dist
    
    # putting all of the number variables in a string
    def tostring(self):
        return "" + rx + ", "+ ry + ", "+  vx + ", "+ vy + ", "+ mass
    