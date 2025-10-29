  # -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:50:45 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def g(t, x, z):         # z = dx/dt
    return z

def f(t, x, z):         
    return -x*(2*pi)**2        # dx2/dt2 =  -x*(2*pi)**2

t0 = 0
tn = 1
h = 0.01
n_steps = int((tn - t0) / h)

t = linspace(t0, tn, n_steps + 1)
x = zeros(len(t))
z = x.copy()
z[0], x[0] = 0, 1
m = 1
k = (2*pi)**2

for i in range(n_steps):
    
    k1 = h * g(t[i], x[i], z[i])
    l1 = h * f(t[i], x[i], z[i])
    
    k2 = h * g(t[i] + h/2 , x[i] + k1/2 , z[i] + l1/2)
    l2 = h * f(t[i] + h/2 , x[i] + k1/2 , z[i] + l1/2)
    
    k3 = h * g(t[i] + h/2 , x[i] + k2/2 , z[i] + l2/2)
    l3 = h * f(t[i] + h/2 , x[i] + k2/2 , z[i] + l2/2)
    
    k4 = h * g(t[i] + h , x[i] + k3 , z[i] + l3)
    l4 = h * f(t[i] + h , x[i] + k3 , z[i] + l3)
    
    z[i + 1] = z[i] + (l1 + 2*l2 + 2*l3 + l4) / 6
    x[i + 1] = x[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

KE = (m * z**2) / 2
PE = (k * x**2) / 2
E = KE + PE

plt.plot( t, E, t, KE, t, PE)
plt.legend(['E', 'KE', 'PE'])

