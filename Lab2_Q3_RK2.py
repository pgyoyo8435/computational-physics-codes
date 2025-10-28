# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:20:09 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def g(t, y):
    return y - t**2 + 1

t0 = 0
tn = 2
h = 0.1

n_steps = int((tn - t0)/ h)

t = linspace(t0, tn, n_steps + 1)

org = zeros(n_steps + 1)
y_RK2 = org.copy()
y_RK2[0] = 0.5 
org[0] = 0.5

for i in range(n_steps):
    
    k1 = g(t[i], y_RK2[i])*h
    k2 = g(t[i] + h/2, y_RK2[i] + k1/2)*h
    
    y_RK2[i + 1] = y_RK2[i] + k2    

for i in range(len(t)):
    org[i] = t[i]**2 + 2*t[i] + 1 - exp(t[i]) / 2

plt.plot(t, org, t, y_RK2)
plt.legend(['Original', 'RK2'])