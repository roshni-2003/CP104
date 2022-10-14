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
from functions import is_leap
year = int(input("Enter a year (>0): "))

result = is_leap(year)

if result is True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
