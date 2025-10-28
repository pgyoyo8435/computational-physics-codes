# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:26:05 2024

@author: pg735
"""

def f(x):
    return x**3 - 5*x + 3
tol = 0.001

a, b = [float(input(f"Give the value of {char}: ")) for char in 'ab']

while f(a) * f(b) >= 0:
    print("The assumed values of a and b aren't correct!")
    a, b = [float(input(f"Give the value of {char}: ")) for char in 'ab']

while ((b-a) >= tol):
    
    c = (a+b)/2         # middle point
 
    if (f(c) == 0.0):   # Check if middle point is root
        break
    
    if f(c) < 0:
        a = c
    else:
        b = c

print("The value of root is : ","%.3f"%c)
     