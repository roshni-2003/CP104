"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-09"
-------------------------------------------------------
"""

date_number = int(input("Enter a date in the format MMDDYYYY: "))

# import
from functions import date_extract
date = date_extract(date_number)

print(f"The reformatted date: {date[0]}/{date[1]}/{date[2]}")
