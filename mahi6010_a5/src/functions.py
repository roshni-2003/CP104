"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-07"
-------------------------------------------------------
"""


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, num + 1):
        product = product * i
    return(product)


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    prints a table of the number of calories burned every
    five minutes given the number of calories burned per
    minute (per_minute) an the total number of minutes run.
    Use: calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - calories burnt per minute (float > 0)
        minutes - total mins run (int > 0)
    Returns:
        None
    -----------------------------
    """
    for i in range(5, minutes + 1, 5):
        cal_burn = i * per_minute
        print(f"{i}:    {cal_burn:.1f}")
    return()


def open_triangle(num_rows):
    """
    -------------------------------------------------------
    takes an integer parameter and prints a triangle of #
    characters with an empty center.
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of rows (int > 0)
    Returns:
        None
    -----------------------------
    """
    triangle = "#"
    for x in range(num_rows):
        print("#" + " " * (x) + "#")
    return()


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("    ", end=" ")

    for x in range(start, stop + 1):
        print(f"{x:5.0f}", end=" ")
    print()

    print("   ", end=" ")

    for x in range(start, stop + 1):
        print("-----", end="-")
    print()

    for x in range(start, stop + 1):
        print(f"{x:2.0f} |", end=" ")
        for y in range(start, stop + 1):
            mult = x * y
            print(f"{mult:5.0f}", end=" ")
        print()
    return()


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    sum = 0
    end = (increment * count) + start
    for x in range(start, end, increment):
        sum += x
    return(sum)
