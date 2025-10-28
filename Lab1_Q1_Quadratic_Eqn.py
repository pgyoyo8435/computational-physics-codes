# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:07:31 2024

@author: pg735
"""

from numpy import*

def quad_eqn(a,b,c):
    
    if a == 0:
        return "This is not a Qudratic Equation!"
    
    det = b**2 - 4*a*c
    D = sqrt(abs(det))
    x2 = (-b - D)/(2*a)
      
    if det > 0:
        print("\nThe equation has Real and Distinct Roots as: ", x1, " and ", x2)
        
    elif det == 0:
        print("\nThe equation has Real and Identical Roots as: ", x1, " and ", x2)
    
    elif det < 0 :
        print("\nThe equation has Complex Roots as:")
        print()
        print("x1 = ", complex(-b/(2*a), D/(2*a)))
        print("x1 = ", complex(-b/(2*a), -D/(2*a)))
    
    return

a, b, c = [float(input(f"Give the value of {char}: ")) for char in 'abc']
quad_eqn(a,b,c)

