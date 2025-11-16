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
        
        # positions 
        self.rx = rx
        self.ry = ry
        
        # velocities 
        self.vx = vx
        self.vy = vy
        
        # mass and color
        self.mass = mass
        self.color = color
        
        # inital force accumulation 
        self.fx = 0.0
        self.fy = 0.0
       
        
    # distance_to calculates the distance between this body and other body
    def distance_to(self, other):
        
        dx = self.rx - other.rx
        dy = self.ry - other.ry
        return np.sqrt(dx **2 + dy **2)
    
    # zeroing force between iterations
    def resetforce(self):
        self.fx = 0.0
        self.fy = 0.0
        
    # calculating the force between this body and other body
    def addforce(self,other):
        
        G = 6.673e-11
        # calculating distance between the particles
        dx = other.rx - self.rx
        dy = other.ry - self.ry
        dist = np.sqrt(dx**2 + dy**2)
        # calculating gravitational force
        f = G * (self.mass * other.mass) / (dist**2)
        # adding this force to this body
        
        self.fx += f * dx / dist    # Fcos(theta) = f * dx/dist
        self.fy += f * dy / dist  
   
        
            
    # update method completes one time step
    def update(self,dt): 
        
        '''
        vx += dt * fx / mass
        vy += dt * fy / mass
        rx += dt * vx
        ry += dt * vy
        return vx, vy, rx, ry
        '''
        # perhaps this works? 
        ax = self.fx/self.mass  # calc acceleration from force/mass
        ay = self.fy/self.mass 
        
        self.vx += ax*dt        # update velocity w/ acceleration and dt
        self.vy += ay*dt 
        
        self.rx += self.vx *dt  # update positions w/ vdt 
        self.ry += self.vy *dt 
        
    
    # putting all of the number variables in a string
    def tostring(self):
        return f"Body(rx={self.rx: .3f}, ry={self.ry:.3f}, vx={self.vx:.3f}, vy={self.vy:.3f}, m={self.mass:.3f})"

    # checking what quadrant this body is in
    def inquad(self,q):
        return q.contains(self.rx,self.ry)
    

    
