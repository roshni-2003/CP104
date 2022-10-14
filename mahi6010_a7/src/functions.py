"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-22"
-------------------------------------------------------
"""


def list_factors(num):
    """
    -------------------------------------------------------
    Gets a positive integer from user and returns all factors
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - Function finds factors of this num (int>0)
    Returns:
        factors - list of all factors (list)
    ------------------------------------------------------
    """
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return(factors)


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    pos_list = []
    num = int(input("Enter a positive number: "))

    while num != 0:
        if num > 0:
            pos_list.append(num)
        num = int(input("Enter a positive number: "))

    return(pos_list)


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        index - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    index = []
    for i in range(0, len(values)):
        if values[i] == target:
            index.append(i)
    return(index)


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in
    subtrahend.
    i.e. the values in the first list that appear in the
    second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    i = 0
    while i != len(minuend):
        if minuend[i]in subtrahend:
            minuend.remove(minuend[i])
            i -= 1
        i += 1

    return()


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    for i in range(0, len(values) - 1):
        if values[i] < values[i + 1]:
            in_order = True
            index = -1
        elif values[i] > values[i + 1]:
            in_order = False
            index = i + 1
            break

    return(in_order, index)
