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
from functions import rgb_mix
from random import randint

colours_to_mix = ["blue", "green", "red", "cyan"]
num1 = randint(0, 3)
num2 = randint(0, 3)


mix = rgb_mix(colours_to_mix[num1], colours_to_mix[num2])

print(
    f'''rgb_mix("{colours_to_mix[num1]}", "{colours_to_mix[num2]}") → "{mix}"''')
