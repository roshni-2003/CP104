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
from functions import day_of_week
from random import randint

num = randint(0, 100)

weekDay = day_of_week(num)

print(f'''day_of_week({num}) → "{weekDay}"''')
