"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-23"
-------------------------------------------------------
"""
# import
from functions import product_largest
from random import randint

num1 = randint(-30, 30)
num2 = randint(-30, 30)
num3 = randint(-30, 30)

largest_product = product_largest(num1, num2, num3)

print(f'''product_largest({num1}, {num2}, {num3}) → {largest_product}''')
