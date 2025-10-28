# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:33:14 2024

@author: pg735
"""
                                                                           
from numpy import*
import matplotlib.pyplot as plt

# Parameters
v = 1.0
dx = 0.01
dt = dx / 2
x = arange(-0.5, 1 + dx, dx)
t = arange(0, 1 + dt, dt)

u_initial = ones(len(x))  # u(x, 0) = 1 for all x


# Function to solve using Central Difference
def central_difference(u):
    u_next = zeros(len(u))
    for n in range(1, len(t)):
        for i in range(1, len(x) - 1):
            u_next[i] = u[i] - (v * dt / (2 * dx)) * (u[i + 1] - u[i - 1])
        u = u_next.copy()
    return u

# Function to solve using Upwind Scheme
def upwind(u):
    u_next = zeros(len(u))
    for n in range(1, len(t)):
        for i in range(1, len(x)):
            u_next[i] = u[i] - (v * dt / dx) * (u[i] - u[i - 1])
        u = u_next.copy()
    return u

# Solve using both schemes
u_central = central_difference(u_initial)
u_upwind = upwind(u_initial)

plt.figure()
plt.plot(x, u_central, label="Central Difference Scheme", color="blue")
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Solution of PDE using Central Difference Scheme')
plt.legend()
plt.grid()

plt.figure()
plt.plot(x, u_upwind, label="Upwind Scheme", color="red")
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Solution of PDE using Upwind Scheme')
plt.legend()
plt.grid()
