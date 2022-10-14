    """
   -------------------------------------------------------
   [program description]
   -------------------------------------------------------
   Author:  Roshni Mahindru
   ID:      210756010
   Email:   mahi6010@mylaurier.ca
   __updated__ = "2021-10-05"
   -------------------------------------------------------
   """

# input
length = float(input("Foundation length (m): "))

width = float(input("Foundation width (m): "))

foundation_height = float(input("Foundation height (m): "))

wall_height = float(input("Wall height (m): "))

concrete_cost = float(input("Cost of concrete ($/m^3): "))

brick_cost = float(input("Cost of bricks ($/m^2): "))

# process
foundation_concrete = length * width * foundation_height
final_concrete_cost = concrete_cost * foundation_concrete

bricks_for_wall = 2 * (wall_height * length) + 2 * (wall_height * width)
final_brick_cost = brick_cost * bricks_for_wall

total = final_concrete_cost + final_brick_cost

# output
print()
print(f"Concrete needed for foundation (m^3): {foundation_concrete:.2f}")
print(f"Cost of concrete: ${final_concrete_cost:,.2f}")

print(f"Bricks needed for walls (m^2): {bricks_for_wall:.2f}")
print(f"Cost of bricks: ${final_brick_cost:,.2f}")

print(f"Total cost: ${total:,.2f}")
