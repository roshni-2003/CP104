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

from functions import file_stats

fh = open("text.txt", "r", encoding="utf-8")

ucount, lcount, dcount, wcount = file_stats(fh)

print(ucount, lcount, dcount, wcount)
