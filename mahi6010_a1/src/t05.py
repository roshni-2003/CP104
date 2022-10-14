"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-09-25"
-------------------------------------------------------
"""

# receive input from user
principal = float(input("Principal: $"))
interest = float(input("Interest:"))
years = int(input("Number of years:"))
compPeryear = int(input("Number of time interest compounded per year:"))

# calculate balance
balance = principal * ((1 + (interest / compPeryear)) ** (years * compPeryear))

# display balance
print("Balance: $", balance)
