#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:45:46 2024

@author: phy
"""

from numpy import*
import matplotlib.pyplot as plt

X = 10          # Length of the x interval
T = 100         # Total time
N = 100     
k = 0.006

x = linspace(0, X, N)
t = linspace(0, T, N)

dx = X/ (N-1)
dt = T/ (N-1)
u = zeros((len(x), len(t)))
alpha = k*(dt / dx**2)
 
# Initial condition
u[:, 0] = 0     # u(x, 0) = 0 

# Boundary condition
u[0, :] = 100  # u(0, t) = 0
u[-1, :] = 50

# Explicit scheme
for n in range(len(t) - 1):
    for i in range(1, len(x) - 1):
        u[i, n + 1] = u[i, n] + alpha * (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n])


plt.plot(x, u[:, -1], label='Numerical Solution (Explicit)')
plt.xlabel('x')
plt.ylabel('u(x, t)')
plt.title('Heat Conduction Equation: Explicit Method')
plt.legend()
plt.grid(True)
