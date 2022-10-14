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

from functions import customer_record

rec_num = int(input("Enter a record number: "))

fh = open("customers.txt", "r", encoding="utf-8")

result = customer_record(fh, rec_num)

fh.close()

print(result)
