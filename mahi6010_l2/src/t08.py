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

# receive input form user
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))
upper_limit = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

# calculate constants
BMI = weight / height**2
BMI_PRIME = BMI / upper_limit

# print BMI and BMI'
print("Body Mass Index (kg/m^2) = ", BMI)
print("BMI Prime = ", BMI_PRIME)
