# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:06:56 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

a = float(input("Give guess vaule of y'(x0): "))
b = float(input("Give another guess vaule of y'(x0): "))

yn = 0

def RK2(guess):       #function takes guess vaule of y'(x0)
    
    x0 = 0
    xn = 9
    y0 = 0
    yn = 0
    h = 0.01

    n = int((xn - x0) / h)
    x = linspace(x0, xn, n+1)
    dy_dx = zeros(len(x))
    y = zeros(len(x))
    y[0] = 0
    dy_dx[0] = guess
    
    def g(x, y, z):
        dydx = z
        return dydx
    
    def f(x, y, z):
        dzdx = 2*y + 8*x*(9 - x)
        return dzdx
    
    # solving ODE d2y/dx2 = 2*y + 8*x*(9 - x)
    for i in range(n):
        k1 = h * g(x[i], y[i], dy_dx[i])
        l1 = h * f(x[i], y[i], dy_dx[i])
        
        k2 = h * g(x[i] + h/2 , y[i] + k1/2 , dy_dx[i] + l1/2)
        l2 = h * f(x[i] + h/2 , y[i] + k1/2 , dy_dx[i] + l1/2)
        
        dy_dx[i + 1] = dy_dx[i] + l2
        y[i + 1] = y[i] + k2

    return x, y, dy_dx

x, y, z  = RK2(a)

x1 , y1, z1 = RK2(b)

z_des = a + ((b - a)/(y1[-1] - y[-1]))*(yn - y[-1])

x2, y2, z2 = RK2(z_des)
print("y(xn) comes out to be ", round(y2[-1], 4))

plt.plot(x, y2)
plt.xlabel('Position (x)')
plt.ylabel('y(x)')
plt.title('Solution of $\\frac{d^2y}{dx^2} = 2y + 8x(9 - x)$ using Shooting(RK2) Method')
plt.grid(True)
plt.legend(["Shooting"])
plt.show()








