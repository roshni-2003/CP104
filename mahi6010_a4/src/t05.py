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
from functions import yee_ha
from random import randint

num = randint(-100, 100)


divisible = yee_ha(num)

print(f'''yee_ha({num}) → "{divisible}"''')
