"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-16"
-------------------------------------------------------
"""
num1 = int(input("Numerator 1: "))
den1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
den2 = int(input("Denominator 2: "))

# import
from functions import multiply_fractions
fraction = multiply_fractions(num1, den1, num2, den2)

print(f"Result: {fraction[0]}/{fraction[1]} = {fraction[2]: 0.3f}")
