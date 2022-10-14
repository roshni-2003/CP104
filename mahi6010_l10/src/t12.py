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

from functions import find_shortest

fh = open("words.txt", "r", encoding="utf-8")

word = find_shortest(fh)

fh.close()

print(word + " is the first shortest word")
