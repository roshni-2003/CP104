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

width = float(input("Width (m): "))
length = float(input("Length (m): "))
speed = float(input("Speed (m^2/minute): "))

# import
from functions import mow_lawn
time = mow_lawn(width, length, speed)

print(f"Mowing the lawn takes {time:.0f} minutes")
