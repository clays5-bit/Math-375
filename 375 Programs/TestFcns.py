# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 16:13:55 2025

@author: richa
"""
import numpy as np
def F(x):
    A = .1*np.ones((5,5))
    for i in range(5):
        A[i,i] = ((x-i)**2/2*(i+1))+1
    for i in range(4):
        A[i,i+1] = (x+i+1)
    for i in range(4):
        A[i+1,i] = x/(i+1)
    return np.linalg.eigvals(A).max()

def G(x):
    n = 100; h = 1./n; dt = .4*h**2; r =.4;s = 1-2*r
    M = np.diag(s*np.ones((n)))+np.diag(
        r*np.ones((n-1)),k=1)+np.diag(r*np.ones((n-1)),k=-1)
    T = 0.
    u = np.zeros((n,1))
    D = 0.
    while T<1. :
        u = M@u; 
        u[-1] += r* (-4*(.5-T)**2+1)
        u[0] += r*( -.5*(x-T)**2+1)
        D += np.sum(u[40:60])*dt*h
        T+=dt
    return .5*(D-1)**2

def H(x):
    h = (.5*(6*x-2)**2)*np.sin(12*x-4)+10*(x-.5)+5
    return h

def dH(x):
    dh = (216*(1/3-x)**2)*np.cos(12*x-4)-(12-36*x)*np.sin(12*x-4)+10
    return dh

def ddH(x):
    ddh = 36*(-(72*x**2-48*x+7)*np.sin(12*x-4)-8*(1-3*x)*np.cos(12*x-4))
    return ddh

#Re-written version of H(x) for FPI
def C(x):
    g = ((.5*(6*x-2)**2*np.sin(12*x-4)+.2)/-10)+.5
    return g