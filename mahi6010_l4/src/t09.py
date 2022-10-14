"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-07"
-------------------------------------------------------
"""

num1 = int(input("Enter numerator of fraction 1: "))
den1 = int(input("Enter denominator of fraction 1: "))
num2 = int(input("Enter numerator of fraction 2: "))
den2 = int(input("Enter denominator of fraction 2: "))

# Import
from functions import fraction_product
...
fraction = fraction_product(num1, den1, num2, den2)
...

print(f"Product = {fraction[0]} / {fraction[1]}")
print(f"Decimal = {fraction[2]:.2f}")
