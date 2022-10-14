"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
from functions import symmetric_difference

values1 = [10, 3, 10, 3, 1]
values2 = [8, 2, 7, 3, 6, 10, 32, 99]

difference = symmetric_difference(values1, values2)

print(f"Values 1: {values1}")
print(f"Values 2: {values2}")
print()
print(f"Difference: {difference}")
