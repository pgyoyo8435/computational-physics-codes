# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:37:22 2024

@author: pg735
"""


from numpy import*
import matplotlib.pyplot as plt

a = float(input("Give guess vaule of y'(x0): "))
b = float(input("Give another guess vaule of y'(x0): "))

yn = 0

def RK4(guess):       #function takes guess vaule of y'(x0)
    
    x0 = 0
    xn = pi/4
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
        dzdx = cos(x) - 4*y
        return dzdx
    
    
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


    return x, y, dy_dx

x, y, z  = RK4(a)

x1 , y1, z1 = RK4(b)

z_des = a + ((b - a)/(y1[-1] - y[-1]))*(yn - y[-1])

x2, y2, z2 = RK4(z_des)
print("y(xn) comes out to be ", round(y2[-1], 4))

plt.plot(x, y2)
plt.xlabel('Position (x)')
plt.ylabel('y(x)')
plt.title('Solution of $\\frac{d^2y}{dx^2} = -4y + cos(x)$ using Shooting(RK4) Method')
plt.grid(True)
plt.legend(["Shooting"])
plt.show()








