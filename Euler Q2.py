# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:06:37 2024

@author: pg735
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation f(x,t) = dx/dt = 2x + 10
def f(t, x):
    return 2*x + 10

# Parameters
t0 = 0       # Initial time
t_n = 10     # End time
dt = 0.1     # Time step
x0 = 0       # Initial condition

# Number of steps
n_steps = int((t_n - t0) / dt)


t = np.linspace(t0, t_n, n_steps + 1)
x = np.zeros(n_steps + 1)               # initialising solution array
x[0] = x0

# Euler's method
for i in range(n_steps):
    x[i + 1] = x[i] + f(t[i], x[i]) * dt

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t, x, label="Euler's Method")
plt.xlabel('Time (t)')
plt.ylabel('x(t)')
plt.title('Solution of $\\frac{dx}{dt} = 2*x + 10$ using Euler\'s Method')
plt.grid(True)
plt.legend()
plt.show()
