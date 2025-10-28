# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:15:19 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

x0 = 0
xn = 5
y0 = 1
h = 0.01

n = int((xn - x0) / h)
x = linspace(x0, xn, n+1)
dy_dx = zeros(len(x))
y = zeros(len(x))
y[0] = y0
dy_dx[0] = 0

def g(x, y, z):
    dydx = z
    return dydx

def f(x, y, z):
    dzdx = x*z**2 - y**2
    return dzdx

# solving ODE d2y/dx2 = x*z**2 - y**2
for i in range(n):
    k1 = h * g(x[i], y[i], dy_dx[i])
    l1 = h * f(x[i], y[i], dy_dx[i])
    
    k2 = h * g(x[i] + h/2 , y[i] + k1/2 , dy_dx[i] + l1/2)
    l2 = h * f(x[i] + h/2 , y[i] + k1/2 , dy_dx[i] + l1/2)
    
    k3 = h * g(x[i] + h/2 , y[i] + k2/2 , dy_dx[i] + l2/2)
    l3 = h * f(x[i] + h/2 , y[i] + k2/2 , dy_dx[i] + l2/2)
    
    k4 = h * g(x[i] + h , y[i] + k3 , dy_dx[i] + l3)
    l4 = h * f(x[i] + h , y[i] + k3 , dy_dx[i] + l3)
    
    dy_dx[i + 1] = dy_dx[i] + (l1 + 2*l2 + 2*l3 + l4) / 6
    y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6


plt.plot(x, y)
plt.xlabel('Position (x)')
plt.ylabel('y(x)')
plt.title('Solution of $\\frac{d^2y}{dx^2} = x(\\frac{dy}{dx})^2 -y^2 $ using RK4 Method')
plt.grid(True)
plt.show()









