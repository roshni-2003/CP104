"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
from functions import list_categorize

values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]

negatives, positives, zeroes, evens, odds = list_categorize(values)

print(f"Values: {values}")
print()
print(f'''Negatives: {negatives}
Positives: {positives}
Zeroes: {zeroes}
Evens: {evens}
Odds: {odds}''')
