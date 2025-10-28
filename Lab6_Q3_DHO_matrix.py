# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:13:10 2024

@author: pg735
"""


from numpy import*
import matplotlib.pyplot as plt

t0 = 0
tn = 20
x0 = 1
v0 = 0
h = 0.1                 # h = 0.12 is critical value
h1 = 0.13

def mat(h):
    
    f0 = array([x0, v0])
    f0_ = array([x0, v0])
    
    D = array([[1, h],                  # coefficient matrix for d2x/dt2 = -0.5dx/dt - 4x
               [-4*h, 1-h*0.5]])
    det = (1 - 0.5*h + 4*h**2)          # determinant
    
    D_inv = array([[ (1-h*0.5)/det, -h/det ],   # Inverse matrix 
               [ 4*h/det, 1/det ]])
    
    n = int((tn - t0)/ h)
    t = linspace(t0, tn, n + 1)
    
    f, f1 = [], []
    f.append(f0)
    f1.append(f0)
    
    for i in range(n):
        f0 = dot(D, f0)
        f.append(f0)
        
        f0_ = dot(D_inv, f0_)
        f1.append(f0_)
        
    f = array(f)
    f1 = array(f1)
    return t, f, f1

t, f, f1 = mat(h)
t_, f_, f1_ = mat(h1) 

plt.plot(t, f[:, 0], t_, f_[:, 0])
plt.xlabel('Time (t)')
plt.ylabel('x(t)')
plt.title('Solution of the Damped Harmonic Oscillator Problem')
plt.legend([f"h = {h}", f"h = {h1}"])




