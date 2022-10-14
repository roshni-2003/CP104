"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-12-03"
-------------------------------------------------------
"""

from functions import scalar_multiply
from functions import generate_matrix_num

matrix = generate_matrix_num(3, 3, -10, 10, "int")

print("Matrix before scalar multiplication:")
count1 = 0
count2 = 0

for x in range(0, len(matrix[0])):
    print(f"{count2:5.0f}", end="")
    count2 += 1
print()

for i in range(0, len(matrix)):
    print(count1, end="")
    count1 += 1
    for j in range(0, len(matrix[i])):
        print(f"{matrix[i][j]:4.0f}", end=" ")

    print()

num = int(input("Enter number: "))

scalar_multiply(matrix, num)

print("Matrix after scalar multiplication:")

count1 = 0
count2 = 0

for x in range(0, len(matrix[0])):
    print(f"{count2:5.0f}", end="")
    count2 += 1
print()

for i in range(0, len(matrix)):
    print(count1, end="")
    count1 += 1
    for j in range(0, len(matrix[i])):
        print(f"{matrix[i][j]:4.0f}", end=" ")
    print()
