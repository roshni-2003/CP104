"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""
dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

total = dirt + gravel + sand
print()
print("Material   Cubic Metres")
print(f"Dirt:  {dirt:>8.1f}")
print(f"Gravel:{gravel:>8.1f}")
print(f"Sand:  {sand:>8.1f}")
print(f"Total: {total:>8.1f}")
