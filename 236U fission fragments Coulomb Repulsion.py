# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:29:33 2025

@author: pg735
"""

import numpy as np
import matplotlib.pyplot as plt

def coulomb_energy(A1, A_total=236, Z_total=92, r0=1.2):
    A2 = A_total - A1
    Z1 = (Z_total / A_total) * A1
    Z2 = (Z_total / A_total) * A2
    
    R1 = r0 * A1**(1/3)  # Nuclear radius
    R2 = r0 * A2**(1/3)
    
    Ec = (1.44 * Z1 * Z2) / (R1 + R2)  # Coulomb energy in MeV
    return Ec

A1_values = np.arange(50, 151)  # A1 from 50 to 150
Ec_values = [coulomb_energy(A1) for A1 in A1_values]

plt.figure(figsize=(8, 5))
plt.plot(A1_values, Ec_values, marker='o', linestyle='-', color='b')
plt.xlabel("Fragment Mass Number A1")
plt.ylabel("Coulomb Repulsion Energy (MeV)")
plt.title("Coulomb Repulsion Energy vs. Fragment Mass")
plt.grid()
plt.show()
