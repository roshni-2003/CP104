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
original_time = int(input("Enter number of seconds: "))

# calculate hours, days, minutes, and seconds
time = original_time
S_P_H = 3600
S_P_M = 60
HOUR = int(time // S_P_H)
time %= S_P_H
MINUTES = int(time // S_P_M)
time %= S_P_M
SECONDS = int(time)

# output
print(f"There are {HOUR:3.0f} hours, {MINUTES:3.0f} minutes, and {SECONDS:3.0f} seconds in {original_time:3.0f} seconds")
