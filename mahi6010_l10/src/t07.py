"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""
from functions import append_max_num

fh = open("numbers.txt", "r+", encoding="utf-8")

num = append_max_num(fh)

fh.close()

print(num)
