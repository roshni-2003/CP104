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

from functions import customer_by_id

fh = open("customers.txt", "r", encoding="utf-8")

id = input("Enter an ID: ")

result = customer_by_id(fh, id)

print(result)
