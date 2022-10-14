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
from functions import url_categorize

url = input("Enter the website address: ")

type = url_categorize(url)

print(type)
