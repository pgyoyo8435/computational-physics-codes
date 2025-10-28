# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:03:11 2024

@author: pg735
"""
from numpy import*

def f(x):
    # Handle the singularity at x = 0 (sin(x)/x -> 1 as x -> 0)
    # Since numpy computes normalised sinc = sin(pi*x)/pi*x thus multn. with pi makes sin(x)/x
    return sinc(x / pi)

# Parameters
a, b = 0, 1  # Integration limits
N, M = 1000, 1000     # Number of random points, number of trials 

x_vals = linspace(a, b, 1000)
f_vals = f(x_vals)
f_max = max(f_vals)     # value of max(f(x)) for x in [0,1]


def monte_carlo(a, b, N, func_max):
    count = 0                       # For number of points within the function curve
    box_area = (b - a) * func_max   # Area of the bounding box (width * height)

    # Monte Carlo iterations
    for _ in range(N):
        # Generate random x between a and b
        x_rand = random.uniform(a, b)
        # Generate random y between 0 and max(f(x))
        y_rand = random.uniform(0, func_max)

        # Check if the random point (x_random, y_random) lies under the curve
        if y_rand <= f(x_rand):
            count += 1

    # Estimate of the integral is the fraction of points under the curve times the area of the box
    estimated_area = (count / N) * box_area
    
    return estimated_area

results = []
for _ in range(M):
    result = monte_carlo(a, b, N, f_max)
    results.append(result)

I = mean(result)
    
# Perform the Monte Carlo integration using hit-or-miss method

print("value of Integral = ", I)


