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

from functions import matrix_equal
from functions import generate_matrix_char

matrix1 = generate_matrix_char(3, 3)
matrix2 = generate_matrix_char(3, 3)

print("First matrix:")

for x in range(0, len(matrix1[0])):
    print(f"{x:7d}", end="")
print()

for i in range(0, len(matrix1)):
    print(f"{i:<6.0f}", end="")
    for j in range(0, len(matrix1[i])):
        print(f"{matrix1[i][j]:6s}", end=" ")

    print()

print()

print("Second matrix:")

for x in range(0, len(matrix2[0])):
    print(f"{x:7d}", end="")
print()

for i in range(0, len(matrix2)):
    print(f"{i:<6.0f}", end="")
    for j in range(0, len(matrix2[i])):
        print(f"{matrix2[i][j]:6s}", end=" ")

    print()

print()
equal = matrix_equal(matrix1, matrix2)

print(equal)
