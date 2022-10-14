"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""

from functions import text_analyze

txt = input("Enter a string: ")

uppr, lwr, dgt, wht = text_analyze(txt)

print(f"upper case letters: {uppr}")
print(f"lower case letters: {lwr}")
print(f"digits: {dgt}")
print(f"whitespace characters: {wht}")
