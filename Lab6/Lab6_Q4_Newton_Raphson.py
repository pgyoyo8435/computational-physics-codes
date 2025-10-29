# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:15:27 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 12

def g(x):
    return 2*x

tol=0.01
x0= int(input("enter the guess value ="))

while abs(f(x0)/g(x0))>= tol :
   x0 = x0 - f(x0)/ g(x0)
   
print("print the value of" , x0)

