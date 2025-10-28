# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 08:41:29 2021

@author: mani
"""

def fectorial(N):
    fect = 1
    for i in range(1,N+1):
        fect = fect*i
    return fect
    
N = int(input("Please give a positive integer: "))
print("\nThe factorial of ",N," is: ",fectorial(N))        
    