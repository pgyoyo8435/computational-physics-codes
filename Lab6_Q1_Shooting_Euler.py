# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:52:32 2024

@author: pg735
"""

from numpy import *
import matplotlib.pyplot as plt

# Functions for the differential equations
def dx_dt(t, x, y):
    return x**2 + (t - 3)*x + sin(t)

def dy_dt(t, x, y):
    return y**2 + sqrt(t**2 + 1) + cos(t)*x

def RK4(guess):
    t0 = 0
    tn = 2
    h = 0.01
    n = int((tn - t0) / h)
    
    t = linspace(t0, tn, n+1)
    x = zeros(len(t))
    y = zeros(len(t))
    
    x[0] = 1  # Initial condition for x
    y[0] = guess  # Initial guess for y
    
    for i in range(n):
        k1_x = h * dx_dt(t[i], x[i], y[i])
        k1_y = h * dy_dt(t[i], x[i], y[i])

        k2_x = h * dx_dt(t[i] + h/2, x[i] + k1_x/2, y[i] + k1_y/2)
        k2_y = h * dy_dt(t[i] + h/2, x[i] + k1_x/2, y[i] + k1_y/2)

        k3_x = h * dx_dt(t[i] + h/2, x[i] + k2_x/2, y[i] + k2_y/2)
        k3_y = h * dy_dt(t[i] + h/2, x[i] + k2_x/2, y[i] + k2_y/2)

        k4_x = h * dx_dt(t[i] + h, x[i] + k3_x, y[i] + k3_y)
        k4_y = h * dy_dt(t[i] + h, x[i] + k3_x, y[i] + k3_y)

        x[i+1] = x[i] + (k1_x + 2*k2_x + 2*k3_x + k4_x)/6
        y[i+1] = y[i] + (k1_y + 2*k2_y + 2*k3_y + k4_y)/6

    return t, x, y

a, b = [float(input(f"Give the {name} guess value of y'(0): ")) for name in ["first", "second"]]
yn = 3

t1, x1, y1 = RK4(a)
t2, x2, y2 = RK4(b)

slope_guess = a + ((b - a) / (y2[-1] - y1[-1])) * (yn - y1[-1])

# Solve with the computed slope
t3, x3, y3 = RK4(slope_guess)

# Print the final y(t=2)
print("y(t=2) comes out to be ", y3[-1])

# Plot the results
plt.plot(t3, y3, label="Numerical Solution y(t)")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Shooting Method Solution')
plt.grid(True)
plt.show()
