"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-22"
-------------------------------------------------------
"""
# import
from functions import closest

target = float(input("Enter target: "))
v1 = float(input("Enter v1: "))
v2 = float(input("Enter v2: "))


result = closest(target, v1, v2)

print(f"Closest value to {target} is {result}")
