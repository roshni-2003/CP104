"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""

# receive input from user in integer form
fahrenheit = int(input("Temperature (F): "))

# Calculate and display the temperature in degrees celcius
FREEZE_IN_F = 32

celcius = round((fahrenheit - FREEZE_IN_F) * (5 / 9))

# format text to add one decimal place
print("Temperature (C): ", '{:.1f}'.format(celcius))
