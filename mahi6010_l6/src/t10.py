"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""

burnt_per_minute = float(input("Enter calories burned per minute: "))
start = int(input("Enter beginning number of minutes: "))
end = int(input("Enter ending number of minutes: "))
inc = int(input("Enter the increment in minutes: "))

from functions import treadmill
treadmill(burnt_per_minute, start, end, inc)
