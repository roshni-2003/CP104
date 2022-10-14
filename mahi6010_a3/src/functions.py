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
from random import randint


def feet_to_acres(feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = feet / 43560
    return(acres)


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    area = width * length
    time = area / speed
    return(time)


def date_extract(date):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = date % 10000
    month = date // 1000000
    day = (date - month * 1000000) // 10000
    return(year, month, day)


def multiply_fractions(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    num = int(num1 * num2)
    den = int(den1 * den2)
    product = float(num / den)

    return (num, den, product)


def math_quiz():
    """
    -------------------------------------------------------
    Generates two random numbers and tests if the users knows the answer
    Use: answer, sum = math_quiz()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        answer - inputted sum of both numbers by user (int)
        sum - real sum of both numbers (int)
    ------------------------------------------------------
    """
    num1 = randint(0, 999)
    num2 = randint(0, 999)
    sum = num1 + num2

    print(f"{num1: >5}")
    print(f"+ {num2: >3}")
    print()
    answer = int(input("Your answer: "))
    print()
    print(f"Your Answer: {answer}")
    print(f"Expected: {sum}")
    return
