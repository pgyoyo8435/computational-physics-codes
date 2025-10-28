# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:07:03 2024

@author: pg735
"""

# Python program to sort an array in ascending order

A = [124, 45, 89, 67, 30, 200, 145, 765, 18, 0, 11]
B = A.copy()

# Perform to arrange the array in ascending/descending order

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]     # swapping elements to ascending order
            
        if B[i] < B[j]:
            B[i], B[j] = B[j], B[i]     # swapping elements to descending order
            

# Output the sorted array
print("The ascending order of array", A)
print("\nThe descending order of array", B)

