"""
-------------------------------------------------------
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-12-02"
-------------------------------------------------------
"""

from functions import stats
from functions import generate_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Lowest number: "))
high = int(input("Highest number: "))
type = "int"

matrix = generate_matrix_num(rows, cols, low, high, type)
smallest, largest, total, average = stats(matrix)

print()

for x in range(0, cols):
    if type == "int":
        print(f"{x:5.0f}", end="")
    else:
        print(f"{x:7.0f}", end="")
print()

for i in range(0, len(matrix)):
    print(i, end="")
    for j in range(0, len(matrix[i])):
        if type == "int":
            print(f"{matrix[i][j]:4.0f}", end=" ")
        else:
            print(f"{matrix[i][j]:6.2f}", end=" ")
    print()

print(
    f"\nSmallest: {smallest:3.2f} \nLargest: {largest:3.2f} \nTotal: {total:3.2f} \nAverage:{average:3.2f}")
