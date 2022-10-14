"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-08"
-------------------------------------------------------
"""
seconds = int(input("Number of seconds: "))

# Import
from functions import time_split
...
time = time_split(seconds)
...

print(
    f"Days: {time[0]}, Hours: {time[1]}, Minutes: {time[2]}, Seconds: {time[3]}")
