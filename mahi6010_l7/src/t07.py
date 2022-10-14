"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-05"
-------------------------------------------------------
"""
from functions import meal_costs

b_total, l_total, s_total, a_total = meal_costs()

print("Total:")
print(f"Breakfast:   $ {b_total:5.2f}")
print(f"Lunch:       $ {l_total:5.2f}")
print(f"Supper:      $ {s_total:5.2f}")
print()
print(f"Grand Total: $ {a_total:5.2f}")
