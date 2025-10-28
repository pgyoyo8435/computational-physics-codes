# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:34:04 2024

@author: pg735
"""

from numpy import *

# Defining the function f(y, x) = y^2 - x
def f(y, x):
    return y**2 - x

# parameters for outer integral i.e., x integral
a_x, b_x, n_x = 0, 1, 10  
h_x = (b_x - a_x) / n_x

n_y = 10  # Number of intervals for inner integral i.e., y integral

def simpson_inner(x):
    # limits for the inner integral
    a_y, b_y = (x - 2) ** 2, 6
    h_y = (b_y - a_y) / n_y

    integral_y = 0
    for i in range(0, n_y, 2):
        y0 = a_y + i * h_y
        y1 = a_y + (i + 1) * h_y
        y2 = a_y + (i + 2) * h_y
        integral_y += h_y * (f(y0, x) + 4 * f(y1, x) + f(y2, x)) / 3

    return integral_y

# Outer integral by Simpson's 1/3 rule over x
integral_x = 0
for i in range(0, n_x, 2):
    x0 = a_x + i * h_x
    x1 = a_x + (i + 1) * h_x
    x2 = a_x + (i + 2) * h_x
    integral_x += h_x * (simpson_inner(x0) + 4 * simpson_inner(x1) + simpson_inner(x2)) / 3

I = integral_x

print("The value of the double integral is = ", round(I, 4))
