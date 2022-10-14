"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""

# receive user input of hourly pay and hours worked in the week

pay = float(input("Hourly rate of pay: "))
hours = float(input("Hours worked in the week: "))

# calculate total amount of money earned
total = pay * hours

# print total amount of money earned
print("Total pay for the week: $ ", '{:.2f}'.format(total))
