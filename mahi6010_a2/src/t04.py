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
balloons = int(input("Number of balloons: "))
children = int(input("Number of children: "))

# process
balloons_received = balloons // children
balloons_left = balloons % children

# output
print(f"Each child receives {balloons_received:2d} balloons")
print(f"Balloons that won’t be distributed: {balloons_left:2d}")
