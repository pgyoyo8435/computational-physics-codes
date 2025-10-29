# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:28:37 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

X = 1.0          # Length of the x interval
T = 0.01         # Total time
dx = 0.1         
dt = 0.0025      


x = arange(0, X + dx, dx)
t = arange(0, T + dt, dt)
u = zeros((len(x), len(t)))

# Initial condition
u[:, 0] = sin(3 * pi * x / 2)     # u(x, 0) = sin(3 * pi * x / 2)

# Boundary condition
u[0, :] = 0  # u(0, t) = 0

# Explicit scheme
for n in range(0, len(t) - 1):
    for i in range(1, len(x) - 1):
        u[i, n + 1] = u[i, n] + (dt / dx**2) * (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n])
        
    # Apply Neumann boundary condition at x = 1, du/dx = 0
    u[-1, n + 1] = u[-2, n + 1]
    
    '''
     u[-1, n + 1] = u[-2, n + 1] correctly implements the Neumann boundary condition at x = 1, du/dx = 0
     as on the right boundary [u[−1,n+1]−u[−2,n+1]]/dx ≈ 0
    '''

# Exact solution
u_exact = exp(-9 * pi**2 * t / 4)[:, None] * sin(3 * pi * x[None, :] / 2)

# Plot the results
plt.plot(x, u[:, -1], label='Numerical Solution (Explicit)', linestyle='-.')
plt.plot(x, u_exact[-1, :], label='Exact Solution')
plt.xlabel('x')
plt.ylabel('u(x, t)')
plt.title('Heat Conduction Equation: Explicit Method')
plt.legend()
plt.grid(True)

fig = plt.figure()
ax = plt.axes(projection='3d')
 
x = arange(0, 1.1, 0.1)
t = linspace(0, 0.01, len(x) )
# syntax for plotting
ax.plot_surface(x, t, u_exact, cmap='viridis',\
                edgecolor='green')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('t', fontsize=12)
ax.set_zlabel('u(x, t)', fontsize=12)
ax.set_title('3D Surface plot for Wave Eqaution')
plt.show()

