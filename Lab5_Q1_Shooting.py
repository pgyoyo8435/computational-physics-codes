# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:40:26 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

a = float(input("Give guess vaule of y'(x0): "))
b = float(input("Give another guess vaule of y'(x0): "))

yn = -3

def Euler(guess):       #function takes guess vaule of y'(x0)
    
    x0 = 0
    xn = pi/2
    y0 = 0
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
        dzdx = -y
        return dzdx
    
    # solving ODE d2y/dx2 = -y
    for i in range(n):
        dy_dx[i+1] = dy_dx[i] + h*f(x[i], y[i], dy_dx[i])
        y[i+1] = y[i] + h*g(x[i], y[i], dy_dx[i])

    return x, y, dy_dx

x, y, z  = Euler(a)
org = zeros(len(x))

for i in range(len(x)):
    org[i] = -3*sin(x[i])

x1 , y1, z1 = Euler(b)

z_des = a + ((b - a)/(y1[-1] - y[-1]))*(yn - y[-1])

x2, y2, z2 = Euler(z_des)
print("y(xn) comes out to be ", y2[-1])

plt.plot(x, y2, x, org)
plt.xlabel('Position (x)')
plt.ylabel('y(x)')
plt.title('Solution of $\\frac{d^2y}{dx^2} = -y$ using Shooting(Euler) Method')
plt.grid(True)
plt.legend(["Shooting", "Orignal"])









