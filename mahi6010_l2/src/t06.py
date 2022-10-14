"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RoshnI_P_MMahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""

# receive inputs from user about mortgage, years and yearly interest
mortgage_principal = float(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
interest_rate = float(input("Yearly interest rate (%): "))

# create constant
MTH_MORT = years * 12
I_P_M = interest_rate / 100 / 12

# calculte monthly payment
monthly_pay = mortgage_principal * \
    (I_P_M * (1 + I_P_M) ** MTH_MORT) / (((1 + I_P_M) ** MTH_MORT) - 1)

# print final monthly payment
print("The monthly payments are: $ ", monthly_pay)
