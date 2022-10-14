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
sweatband = float(input("Enter sweatband cost: "))
pants = float(input("Enter pants cost: "))
jacket = float(input("Enter jacket cost: "))

# process total amount
total = sweatband + pants + jacket

# output receipt
print()
print("Clothes      Cost")
print(f"Sweatband    ${sweatband:6.2f}")
print(f"Pants        ${pants:6.2f}")
print(f"Jacket       ${jacket:6.2f}")
print(f"Total        ${total:6.2f}")
