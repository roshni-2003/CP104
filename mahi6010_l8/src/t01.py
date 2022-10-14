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
from functions import get_weekday_name

for i in range(0, 12):
    num = int(input("Number between 1 - 7: "))
    weekday = get_weekday_name(num)
    print(weekday)
    print()
