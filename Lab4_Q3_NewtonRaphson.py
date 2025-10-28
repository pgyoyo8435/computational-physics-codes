# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:49:46 2024

@author: pg735
"""

def f(x):
    return x**3 - x - 4

def g(x):
    return 3*x**2 - 1

tol = 0.001
x0 = float(input("Give the guess root: "))


while abs(f(x0) / g(x0)) >= tol:
    x0 = x0 - f(x0) / g(x0)
    
print("The value of root is : ", "%.3f"%x0)
    

