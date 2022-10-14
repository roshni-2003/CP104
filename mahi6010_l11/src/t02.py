"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-12-02"
-------------------------------------------------------
"""

from functions import generate_matrix_char

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

matrix = generate_matrix_char(rows, cols)

print("Matrix of characters:")
print(matrix)
