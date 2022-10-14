"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""

# input
date = int(input("Enter a date in the format MMDDYYYY: "))

# process
year = date % 10000
month = date // 1000000
day = (date - month * 1000000) // 10000

# output print the new date
print(f"The reformatted date: {year:04d}/{month:02d}/{day:02d}")
