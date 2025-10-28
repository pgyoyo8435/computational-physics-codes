# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:56:36 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def g(x, y):
    return (x+y)*sin(x)

x0 = 0
xn = 6
h = 0.1

n_steps = int((xn - x0)/ h)

x = linspace(x0, xn, n_steps + 1)
y_RK2 = zeros(n_steps + 1)
y_RK4 = y_RK2.copy()
y_RK2[0], y_RK4[0] = 5, 5

for i in range(n_steps):
    
    k1 = g(x[i], y_RK2[i])*h
    k2 = g(x[i] + h/2, y_RK2[i] + k1/2)*h
    y_RK2[i + 1] = y_RK2[i] + k2
    
    k1 = g(x[i], y_RK4[i])*h
    k2 = g(x[i] + h/2, y_RK4[i] + k1/2)*h
    k3 = g(x[i] + h/2, y_RK4[i] + k2/2)*h
    k4 = g(x[i] + h, y_RK4[i] + k3)*h
    y_RK4[i + 1] = y_RK4[i] + (k1/2 + k2 + k3 + k4/2)/3

plt.plot(x, y_RK2, x, y_RK4)
plt.xlabel('$x ---------->$')
plt.ylabel('$y(x) ---------->$')
plt.title('Numerical solutions of the differential equation $\\frac{dy}{dx} = (x + y) sin(x)$')
plt.legend(['RK2', 'RK4'])
plt.grid(True)



