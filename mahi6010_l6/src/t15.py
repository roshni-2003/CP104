"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""

n = int(input("Enter number of values: "))

from functions import statistics
minimum, maximum, total, average = statistics(n)

print()
print(f"Minimum: {minimum:.2f}")
print(f"Maximum: {maximum:.2f}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")
