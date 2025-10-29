# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:50:03 2024

@author: pg735
"""

from numpy import *

# Defining the function f(y, x) = sqrt(sin(x + y))
def f(y, x):
    return sqrt(sin(x + y))

# parameters for outer integral i.e., x integral
a_x, b_x, n = 0, pi/2, 10 
h_x = (b_x - a_x) / n 

# parameters for inner integral i.e., y integral
a_y, b_y = 0, pi/2
h_y = (b_y - a_y) / n

def simpson_inner(x):
    integral_y = 0
    for i in range(0, n, 2):
        y0 = a_y + i * h_y
        y1 = a_y + (i + 1) * h_y
        y2 = a_y + (i + 2) * h_y
        integral_y += h_y * (f(y0, x) + 4 * f(y1, x) + f(y2, x)) / 3

    return integral_y

# Outer integral by Simpson's 1/3 rule over x
integral_x = 0
for i in range(0, n, 2):
    x0 = a_x + i * h_x
    x1 = a_x + (i + 1) * h_x
    x2 = a_x + (i + 2) * h_x
    integral_x += h_x * (simpson_inner(x0) + 4 * simpson_inner(x1) + simpson_inner(x2)) / 3

I = integral_x

print("The value of the double integral is = ", round(I, 4))
