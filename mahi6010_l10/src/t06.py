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

from functions import number_stats

fh = open("numbers.txt", "r", encoding="utf-8")

smallest, largest, total, average = number_stats(fh)

fh.close()

print(
    f"Smallest: {smallest}\nLargest: {largest}\nTotal: {total}\nAverage: {average:.2f}")
