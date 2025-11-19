#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 18:22:09 2025

@author: mwilliams
"""

import numpy as np


# defining class-wide variables G and solar mass
G = 39.5
eps = 0.1 # au

class body:
    
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
    def distance_to(self, other, eps):
        
        dx = other.rx - self.rx
        dy = other.ry - self.ry
        return np.sqrt(dx **2 + dy **2 + eps **2)
    
    # zeroing force between iterations
    def resetforce(self):
        self.fx = 0.0
        self.fy = 0.0
        
    # calculating the force between this body and other body
    def addforce(self,other):
        
        # adding softening factor
        
        dx = other.rx - self.rx
        dy = other.ry - self.ry
        
        dist = body.distance_to(self,other,eps)

        # calculating gravitational force
        f = G * (self.mass * other.mass) / (dist**2)
        # adding this force to this body
 
        self.fx += f * dx / dist
        self.fy += f * dy / dist
        return np.array([self.fx, self.fy])

    
    def update(self, dt, order, method, bodies = None):
        
        # setting up force aggregations for barnes-hut vs. direct sum
        if method == 'BH':
            def fupdate(body):
                from Tree import tree
                from BarnesHut import this_tree
                force = this_tree.update_force(self) #(body)
                return np.array([self.fx, self.fy])   
               #return force 

        '''
        if method == 'DS':
            
            def fupdate(body):
                force = np.array([self.fx,self.fy])
                for b in bodies:
                    if b is not self:
                        force += b.addforce(b)  # was originally (body, b)
        '''
        
        if method == "DS":
            def fupdate(temp_body):
                fx, fy = 0.0, 0.0
                for b in bodies:
                    if b is not self:
                        dx = b.rx - temp_body.rx
                        dy = b.ry - temp_body.ry
                        dist = np.sqrt(dx*dx + dy*dy + eps*eps)
                        f = G * mass * b.mass / dist**2
                        fx += f * dx/dist
                        fy += f * dy/dist
                return np.array([fx, fy])
           
        # RK4 
        
        # evaluate initial acceleration
        mass = self.mass
        f0 = np.array([self.fx,self.fy])
        a0 = f0 / mass
        v0 = np.array([self.vx,self.vy])
        r0 = np.array([self.rx,self.ry])
        
        
        # first order evaluation
        
        # velocity step
        k1v = a0 * dt
        v1real = v0 + k1v * dt
        
        # position step
        k1r = v0 * dt
        r1 = r0 + k1r * dt
        
        # force evaluation from step 1
        temp_pos = r0 + (k1r / 2) * dt # half step in the first order direction

        temp_body = body(temp_pos[0], temp_pos[1], v0[0], v0[1], mass, self.color)
        self.mass = 0  # replace force.body w/ temp body for force calculation 
        f1 = fupdate(temp_body)
        self.mass = mass
        
        # second order evaluation
        
        # acceleration and velocity from first order half step
        a1 = f1 / mass
        v1 = v0 + k1v * dt / 2
        
        self.resetforce()
        
        # velocity step
        k2v = (a1 + (k1v / 2)) * dt
        v2real = v1 + (k1v + k2v) * dt / 2
        
        # position step
        k2r = (v1 + (k1r / 2))  * dt
        r2 = r1 + (k1r + k2r) * dt / 2
        
        # force evaluation from step 2
        temp_pos1 = r0 + dt * k2r
        
        temp_body = body(temp_pos1[0], temp_pos1[1], v1[0], v1[1], mass, self.color)
        self.mass = 0  # replace this body w/ temp body for force calculation 
        f2 = fupdate(temp_body)
        self.mass = mass  
        
        # third order evaluation 
        
        # acceleration and velocity from 2nd order step
        a2 = f2 / mass
        v2 = v0 + k2v * dt
        
        self.resetforce()
        
        # velocity step
        k3v = (a2 + (k2v / 2)) * dt
        v3real = v2 + (k2v + k3v) * dt / 2 
    
        # position step
        k3r = (v2 + (k2r / 2)) * dt 
        r3 = r2 + (k2r + k3r) * dt / 2 
        
        # force evaluation from step 3
        temp_pos2 = r0 + dt * k3r
        
        temp_body = body(temp_pos2[0], temp_pos2[1], v2[0], v2[1], mass, self.color)
        self.mass = 0  # replace force.body w/ temp body for force calculation 

        f3 = fupdate(temp_body)
        
        self.mass = mass
        
        # fourth order evaluation
        
        # acceleration and velocity from 3rd order step
        a3 = f3 /mass
        v3 = v0 + k3v * dt 
        
        self.resetforce()
        
        # velocity step
        k4v = (a3 + (k3v) ) * dt 
        #v4real = v3 + (k4v) * dt # long live pookie rip
        
        # position step
        k4r = (v3 + (k3r))* dt 
        #r4  = r3 + (k4r) * dt 
    
        # final rk4 evaluation
        
        v4 = v0 + (dt / 6) * (k1v + 2 * k2v + 2 * k3v + k4v)
        r4 = r0 + (dt / 6) * (k1r + 2 * k2r + 2 * k3r + k4r)
        
        # returning the values
        if order == 1:
            self.rx , self.ry = r1
            self.vx, self.vy = v1real
        if order == 2:
            self.rx , self.ry = r2
            self.vx, self.vy = v2real
        if order == 3:
            self.rx , self.ry = r3
            self.vx, self.vy = v3real
        if order == 4:
            self.rx , self.ry = r4
            self.vx, self.vy = v4
            
     
    
    # putting all of the number variables in a string
    def tostring(self):
        return f"Body(rx={self.rx: .3f}, ry={self.ry:.3f}, vx={self.vx:.3f}, vy={self.vy:.3f}, m={self.mass:.3f})"

    # checking what quadrant this body is in
    def inquad(self,q):
        return q.contains(self.rx,self.ry)
    
