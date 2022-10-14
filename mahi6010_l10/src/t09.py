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
from functions import count_frequency_value

fh = open("numbers.txt", "r", encoding="utf-8")

value = int(input("Value to count: "))

count = count_frequency_value(fh, value)

fh.close()

print(f"{value} appears {count} time(s)")
