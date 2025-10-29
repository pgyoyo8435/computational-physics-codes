# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:15:53 2024

@author: pg735
"""

def f(x):
    return 2*x**3 - 2*x - 5

def g(x):
    return 6*x**2 - 2

def NR():
    tol = 0.001
    x0 = float(input("Give the guess root: "))
    
    
    while abs(f(x0) / g(x0)) >= tol:
        x0 = x0 - f(x0) / g(x0)
        
    print("The value of root by Newton-Raphson Method is : ", "%.3f"%x0)

NR()

