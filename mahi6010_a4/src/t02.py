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
from functions import pollution_level

from random import randint

num = randint(0, 400)

polli_level = pollution_level(num)

print(f'pollution_level({num}) → "{polli_level}"')
