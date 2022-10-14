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

from functions import generate_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Lowest number: "))
high = int(input("Highest number: "))
type = input("Type of value: ")

matrix = generate_matrix_num(rows, cols, low, high, type)

print(matrix)
