# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:10:50 2024

@author: pg735
"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters
l = 1.0       # length of the domain
v = 1.0       # wave velocity
t = 0.5       # total time
dx = 0.01     # spatial step size
dt = dx / 2   # time step size
nx = int(l / dx) + 1  # number of spatial grid points
nt = int(t / dt)      # number of time steps

x = np.linspace(-0.5, l + dx, nx)
t_values = np.linspace(0, t, nt)

# Initial condition: u(x, 0) = 1 for all x
def initial_cond():
    u = np.ones(nx)  # Initial condition
    return u

# Central Difference Scheme
def central_diff():
    u = np.zeros((nx, nt))  # Solution array
    u[:, 0] = initial_cond()  # Set initial condition
    
    for n in range(0, nt - 1):
        for j in range(1, nx - 1):
            u[j, n + 1] = u[j, n] - ((v * dt) / (2 * dx)) * (u[j + 1, n] - u[j - 1, n])
    return u

# Upwind Scheme
def upwind_sh():
    u = np.zeros((nx, nt))  # Solution array
    u[:, 0] = initial_cond()  # Set initial condition
    
    for n in range(0, nt - 1):
        for j in range(1, nx):
            u[j, n + 1] = u[j, n] - ((v * dt) / dx) * (u[j, n] - u[j - 1, n])
    return u

# Solve using both schemes
u_central = central_diff()  # Central Difference solution
u_upwind = upwind_sh()      # Upwind Scheme solution

# Plotting results for selected time steps
time_steps = [0, nt // 4, nt // 2, 3 * nt // 4, nt - 1]  # Different time steps to observe evolution

plt.figure(figsize=(14, 6))

# Central Difference Scheme plot
plt.subplot(1, 2, 1)

plt.plot(x, u_central[:, -1])
plt.title('Central Difference Scheme')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.grid(True)

# Upwind Scheme plot
plt.subplot(1, 2, 2)

plt.plot(x, u_upwind[:, -1])
plt.title('Upwind Scheme')
plt.xlabel('x')
plt.ylabel('u(x,t)')

plt.grid(True)

plt.tight_layout()
