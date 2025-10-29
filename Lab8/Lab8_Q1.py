#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:15:10 2024

@author: phy
"""

from numpy import*
import matplotlib.pyplot as plt

# Parameters
dy = 0.1
dx = dy / 2
y = arange(-2, 2 + dy, dy)
x = arange(0, 2 + dx, dx)

u = zeros((len(x), len(y)))

u[0, :] = sin(y)  # Initial condition u(0, y) = sin(y) for all y

#solving by Central Difference Scheme
for n in range(len(x) - 1):
    for j in range(1, len(y) - 1):
        u[n+1 , j] = u[n, j] - (x[n] * dx / (2 * dy)) * (u[n, j+1] - u[n, j-1])

u_exact = sin(y - x**2 / 2)

plt.figure()
plt.plot(x, u[0, :], label="Central Difference Scheme", color="blue")
plt.plot(x, u_exact, label="Exact Solution", color="red")
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Solution of PDE using Central Difference Scheme')
plt.legend()
plt.grid()


