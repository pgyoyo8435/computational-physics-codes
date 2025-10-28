# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:36:57 2024

@author: pg735
"""


from numpy import*

def solve_linear_system_matrix_method(a, b, c, p, q, r):
    
    # Creating the coefficient matrix A and the constant matrix B
    A = array([[a, b], [p, q]])
    B = array([c, r])
    
    det = a*q - p*b
    
    # Check if the determinant is zero
    if det == 0:
        print("\nThe system has no unique solution")
    else:
        # Calculating the inverse of A
        A_inv = ([q / det, -b / det], [-p / det, a / det])
        
        # Calculating the solution matrix X
        X = dot(A_inv, B)
        print(f"\nThe solution is x = {X[0]} and y = {X[1]}")
        
    return 


#taking inputs of coefficients
a, b, c, p, q, r = [float(input(f"Enter the value of {char}: ")) for char in 'abcpqr']

solve_linear_system_matrix_method(a, b, c, p, q, r)
