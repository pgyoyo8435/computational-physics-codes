# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:10:16 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

x = linspace(-1.5, 4, 1000)
y1 = zeros(len(x))
y2 = y1.copy()
roots = []


for i in range(len(x)):
    
    y1[i] = 5*sin(x[i])
    y2[i] = x[i]**3 + (-132 * x[i]**2 + 28*x[i] + 147) / 32
    
    if abs(y1[i] - y2[i]) <= 0.0292:
        roots.append(x[i])
        print("A possible root is: ",round(x[i], 4))

                    
plt.plot(x, y1, x, y2)
plt.xlabel('$x ---------->$')
plt.ylabel('$y(x) ---------->$')
plt.title('Graphical solutions to $ x^3 - \\frac{132}{32}x^2 + \\frac{28}{32}x + \\frac{147}{32}. =  5sin(x)$')
plt.legend(['$5sin(x)$', '$x^3 - \\frac{132}{32}x^2 + \\frac{28}{32}x + \\frac{147}{32}$'])

for root in roots:
    plt.axvline(x=root, color='r', linestyle='--', label=f'{root:.4f}')              
