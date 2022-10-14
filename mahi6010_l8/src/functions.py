"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
from random import randint


def winner():
    blue = 0
    grey = 0
    string = input("Enter the winning team: ")
    if string == "blue":
        blue += 1
    elif string == "grey":
        grey += 1

    while string != " ":
        string = input("Enter the winning team: ")
        if string == "blue":
            blue += 1
        elif string == "grey":
            grey += 1
    return(blue, grey)


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    weekday = ["Sunday", "Monday", "Tuesday",
               "Wednesday", "Thursday", "Friday", "Saturday"]

    name = weekday[d - 1]
    return(name)


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """

    list = 1
    random_nums = []
    while list <= n:
        list2 = [randint(low, high + 1)]
        random_nums = random_nums + list2
        list += 1
    return(random_nums)


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    nums = len(values)
    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odds = 0
    for i in range(0, nums):
        if values[i] < 0:
            negatives += 1
        if values[i] > 0:
            positives += 1
        if values[i] == 0:
            zeroes += 1
        if values[i] % 2 == 0:
            evens += 1
        if values[i] % 2 != 0:
            odds += 1

    return(negatives, positives, zeroes, evens, odds)


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the union of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    one_list = source1 + source2
    for i in one_list:
        if i not in target:
            target.append(i)
    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    for i in source1:
        if i not in source2 and i not in target:
            target.append(i)
    for i in source2:
        if i not in source1 and i not in target:
            target.append(i)
    return target
