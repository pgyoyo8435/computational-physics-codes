# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:16:53 2024

@author: pg735
"""

from sympy import sqrt, sympify

# Prompt user to input an irrational number
user_input = input("Enter an irrational number: ")

# Convert the input string to a symbolic expression
irrational_number = sympify(user_input)

print(f"The irrational number you entered is: {irrational_number}")
print(f"The numerical value is: {irrational_number.evalf()}")

