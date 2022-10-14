"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-12-04"
-------------------------------------------------------
"""
from functions import file_integers

fh = open("numbers.txt", "r", encoding="utf-8")

nums = file_integers(fh)


print(nums)
