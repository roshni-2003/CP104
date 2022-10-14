"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-07"
-------------------------------------------------------
"""
from functions import feet_to_acres


feet = float(input("Square footage: "))

# Import
...
acres = feet_to_acres(feet)
...

print(f"{acres:,.2f} acres is equivalent to {feet:,.2f} square feet.")
