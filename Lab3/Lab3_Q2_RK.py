# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:31:09 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def g(x, y, z):         # z = dy/dx
    return z

def f(x, y, z):         
    return 10*sin(x) - 5*z - 6*y        # dy2/dx2 = 10sin(x) - 5dy/dx - 6y

x0 = 0
xn = 6
h = 0.1
n_steps = int((xn - x0) / h)

x = linspace(x0, xn, n_steps + 1)
y = zeros(len(x))
z = y.copy()
org = y.copy()
z[0], y[0] = 5, 0

for i in range(n_steps):
    
    k1 = h * g(x[i], y[i], z[i])
    l1 = h * f(x[i], y[i], z[i])
    
    k2 = h * g(x[i] + h/2 , y[i] + k1/2 , z[i] + l1/2)
    l2 = h * f(x[i] + h/2 , y[i] + k1/2 , z[i] + l1/2)
    
    k3 = h * g(x[i] + h/2 , y[i] + k2/2 , z[i] + l2/2)
    l3 = h * f(x[i] + h/2 , y[i] + k2/2 , z[i] + l2/2)
    
    k4 = h * g(x[i] + h , y[i] + k3 , z[i] + l3)
    l4 = h * f(x[i] + h , y[i] + k3 , z[i] + l3)
    
    z[i + 1] = z[i] + (l1 + 2*l2 + 2*l3 + l4) / 6
    y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6


for i in range(len(x)):
    org[i] = -6*exp(-3*x[i]) + 7*exp(-2*x[i]) + sin(x[i]) - cos(x[i])

plt.plot(x, y, x, org)
plt.legend(["RK4", "Orignal"])

