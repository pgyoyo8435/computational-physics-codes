# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:47:32 2024

@author: pg735
"""
from numpy import*
from sympy import*
import matplotlib.pyplot as plt

# the data points (x, y)
x_vals = [0, 1, 2, 5]
y_vals = [2, 3, 12, 147]

# symbolic variable x
x = Symbol('x')

# Lagrange polynomial
lagrange_poly = 0
for i in range(len(x_vals)):
  term = 1
  for j in range(len(x_vals)):
    if j != i:
      term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
  lagrange_poly += y_vals[i] * term

# Simplifying the polynomial
lagrange_poly = simplify(lagrange_poly)

# Convert polynomial to a function
f = lambdify(x, lagrange_poly)

y_interp = [f(x_i) for x_i in linspace(0, 6, 100)]

# Plot the data points and the polynomial
plt.plot(x_vals, y_vals, 'o')
plt.plot(linspace(0, 6, 100), y_interp)
plt.legend(['Data Points', 'Lagrange Polynomial'])
plt.title(f'Lagrange Interpolation function {lagrange_poly}')
plt.xlabel('x')
plt.ylabel('y')

# Print the polynomial
print(f"Lagrange Polynomial: {lagrange_poly}")