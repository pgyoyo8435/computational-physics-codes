# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:35:36 2024

@author: pg735
"""

from numpy import*
from scipy import integrate

a, b, n = 0, 1, 10
h = (b-a)/n

def f(x):
    return exp(x-1)* x **2

intg_T, intg_S = 0, 0

for i in range(0, n):
    intg_T += h*(f(a + i*h) + f(a + (i+1)*h))/2

for i in range(0, n, 2):
    intg_S += h*(f(a + i*h) + 4*f(a + (i+1)*h) + f(a + (i+2)*h))/3

Exact = integrate.quad(f,a,b)

print("Exact Value of integral = ", Exact[0],
      "\n\nIntegral by Trapezoidal Rule = ",intg_T,
      "\nAbsolute Error Trapezoidal = ", abs(Exact[0]- intg_T),
      "\nIntegral by Simpson's 1/3 Rule = ", intg_S,
      "\nAbsolute Error Trapezoidal = ", abs(Exact[0]- intg_S))


