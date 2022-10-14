"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""
num = int(input("Enter a number: "))

from functions import sum_even
total = sum_even(num)

print(f"The sum of all even numbers from 2 to {num} is: {total}")
