# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:53:50 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def g(x, y):
    return x*y

x0 = 1
xn = 3
h = 0.1

n_steps = int((xn - x0)/ h)

x = linspace(x0, xn, n_steps + 1)
y = zeros(n_steps + 1)
org = y.copy()
y_mod = y.copy()
y_RK2 = y.copy()
y_RK2[0] = 5 
org[0] = 5
y[0] = 5
y_mod[0] = 5

for i in range(n_steps):
    y[i + 1] = y[i] + g(x[i], y[i])*h
    org[i + 1] = 5*exp((x[i]**2 -1)/2)
    y_mod[i + 1] = y_mod[i] + g(x[i] + h/2, y[i])*h 
    
    k1 = g(x[i], y[i])*h
    k2 = g(x[i] + h/2, y[i] + k1/2)*h
    y_RK2[i + 1] = y_RK2[i] + k2    

plt.plot(x, y, x, y_mod, x, org, x, y_RK2)
plt.legend(['Euler', 'Modifeid Euler', 'Original', 'RK2'])