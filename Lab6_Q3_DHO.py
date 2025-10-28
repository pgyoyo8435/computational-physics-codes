# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:29:07 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def Euler(h):

    t0 = 0
    tn = 10
    
    n = int((tn - t0) / h)
    t = linspace(t0, tn, n+1)
    z, x = zeros(len(t)), zeros(len(t))
    x[0], z[0] = 1, 0
    
    def g(t, x, z):
        dxdt = z
        return dxdt
    
    def f(t, x, z):
        dzdt = -4*x - z/2
        return dzdt

    for i in range(n):
        z[i+1] = z[i] + h*f(t[i], x[i], z[i])
        x[i+1] = x[i] + h*g(t[i], x[i], z[i])
        
    return t, x, z

h1, h2 = 0.01, 0.05
t1, x1, z1 = Euler(h1)
t2, x2, z2 = Euler(h2)
    
plt.plot(t1, x1, t2, x2)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Damped Harmonic Oscillator $\\frac{d^2x}{dt^2} = -4x - 0.5\\frac{dx}{dt}$')
plt.legend([f"h = {h1}", f"h = {h2}"])
plt.grid()



