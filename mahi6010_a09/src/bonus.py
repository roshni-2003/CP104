"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-12-05"
-------------------------------------------------------
"""

from functions import get_addresses

fh = open("address.txt", "r", encoding="utf-8")

address = get_addresses(fh)

print(address)
