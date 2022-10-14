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
value = int(input("Enter the GIC purchase value: $"))
years = int(input("Enter the number of years invested: "))
rate = float(input("Enter the GIC interest rate (%): "))
from functions import gic
final_value = gic(value, years, rate)

print(f"{years} \t  ${final_value:,.2f}")
