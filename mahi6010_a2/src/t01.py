"""
-------------------------------------------------------
Program calculates the annual tax paid by a company
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""

# receive input from the user
sales = int(input("Enter the total sales: $"))

# calculate annual tax
format(float(sales))
ANNUAL_TAX = 22.5
tax = sales * ANNUAL_TAX / 100

# print final receipt
print("Projected Tax Report")
print("--------------------------")
print(f"Total sales:   ${sales:,.2f}")
print(f"Annual tax:    %{ANNUAL_TAX:.2f}")
print("--------------------------")
print(f"Tax:           ${tax:,.2f}")
