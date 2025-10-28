# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:50:32 2024

@author: pg735
"""

from numpy import*

a, b, n = -10, 10, 70
h = (b-a)/n

def f(x):
    return exp(-x**2)         # prob, density

intg_S, x_av, x_sqr_av = 0, 0, 0

for i in range(0, n, 2):
    intg_S += h*(f(a + i*h) + 4*f(a + (i+1)*h) + f(a + (i+2)*h))/3

A = 1/intg_S

def m1(x):
    return x*A*f(x)       # <x>
def m2(x):
    return x**2*A*f(x)  # <x^2>

for i in range(0, n, 2):
    x_av += h*(m1(a + i*h) + 4*m1(a + (i+1)*h) + m1(a + (i+2)*h))/3
    x_sqr_av += h*(m2(a + i*h) + 4*m2(a + (i+1)*h) + m2(a + (i+2)*h))/3
    
print("Normalisation constant A = ", round(A, 4),
      "\n<x> = ", round(x_av, 4), "\n<x^2> = ", round(x_sqr_av, 4))