"""
-------------------------------------------------------
Program finds difference between the units in an inputted two digit number
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""
BASE_DECIMAL = 10
# input
num = int(input("Enter a positive digit number: "))

# processing (find difference between numbers)
unit_one = num // BASE_DECIMAL
unit_two = num % BASE_DECIMAL

diff = unit_one - unit_two

# output
print(f"The difference of the digits of {num} is {diff}")
