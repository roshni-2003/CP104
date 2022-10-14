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
s1 = float(input("Length of side 1: "))
s2 = float(input("Length of side 2: "))

# Import
from functions import pythag
...
calc = pythag(s1, s2)
...

print()
print(f"Radius of resulting circle: {calc[0]:.2f}")
print(f"Diameter of resulting circle: {calc[1]:.2f}")
print(f"Circumference of resulting circle: {calc[2]:.2f}")
print(f"Area of resulting circle: {calc[3]:.2f}")
