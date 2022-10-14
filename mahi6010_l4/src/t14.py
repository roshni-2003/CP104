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
from functions import time_values
...
time = time_values(seconds)
...

print(
    f"""{seconds} is the same as:
    {time[0]} days
    {time[1]} hours
    {time[2]} minutes""")
