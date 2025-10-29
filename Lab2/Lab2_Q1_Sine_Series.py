# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:47:03 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

def factorial(N):
    fect = 1
    for i in range(1,N+1):
        fect = fect*i
    return fect

def sin(x):
    sinx = 0
    for j in range(10):
        num = factorial(2*j + 1)
        sinx += ((-1)**j * x**(2*j + 1)) / num
    return sinx

x0 = 0
xn = pi

n_steps1 = int((xn - x0)/(pi/20))
n_steps2 = int((xn - x0)/(pi/3))

x1 = linspace(x0, xn, n_steps1 + 1)
x2 = linspace(x0, xn, n_steps2 + 1)

y1 = zeros(len(x1))
y2 = zeros(len(x2))

for i in range(len(x1)):
    y1[i] = sin(x1[i])

for i in range(len(x2)):
    y2[i] = sin(x2[i])

plt.plot(x1, y1, x2 , y2)
plt.xlabel('$x$')
plt.ylabel('$sin(x)$')
plt.title('Taylor Series Approximation of $sin(x)$')
plt.legend(['$h = \\frac{\pi}{20}$','$h = \\frac{\pi}{3}$'])
plt.grid(True)

