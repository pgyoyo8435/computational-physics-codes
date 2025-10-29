# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:54:59 2024

@author: pg735
"""

from numpy import*
import matplotlib.pyplot as plt

# Generate 10,000 Gaussian random numbers with mean 0 and standard deviation 1
N = 10000
mean = 0
std_dev = 1
gaussian_random_numbers = random.normal(mean, std_dev, N)

# Plot the histogram of the Gaussian random numbers
'''
I plot Gaussian random numbers with 50 bins/vertical bars. The density = True,
ensures that the histogram is normalized for comparison with a probability density function (PDF).
'''
plt.hist(gaussian_random_numbers, bins=50, density=True,  color='g')
plt.title("Distribution of 10,000 Gaussian Random Numbers")
plt.xlabel("Value")
plt.ylabel("Probability Density")

# Plot the theoretical Gaussian distribution Denstity fuction
x = linspace(min(gaussian_random_numbers), max(gaussian_random_numbers), 1000)
Gauss_PDF = 1/(std_dev * sqrt(2 * pi)) * exp( - (x - mean)**2 / (2 * std_dev**2))
plt.plot(x, Gauss_PDF, color='r')
plt.legend(["Gaussian for sigma = 1 and rho =  0"])
plt.grid(True)


