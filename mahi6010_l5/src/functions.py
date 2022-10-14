"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-22"
-------------------------------------------------------
"""


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    date = day * month
    if date == year:
        magic = True
    else:
        magic = False

    return (magic)


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    if target < v1:
        close1 = v1 - target
    else:
        close1 = target - v1
    if target < v2:
        close2 = v2 - target
    else:
        close2 = target - v2

    if close1 < 0:
        close1 = close1 * (-1)

    if close2 < 0:
        close2 = close2 * (-1)

    if close1 > close2:
        closest_to_target = v2
    elif close2 > close1:
        closest_to_target = v1
    else:
        closest_to_target = v1

    return(closest_to_target)


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        if year % 4 == 0:
            leap_year = True
        else:
            leap_year = False
    return(leap_year)


def richter(n):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        n - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    if n >= 7.5:
        result = "Catastrophe: most buildings destroyed"
    else:
        if n >= 6.5:
            result = "Disaster: buildings may collapse"
        else:
            if n > 5.5:
                result = "Serious damage: walls may crack or fall"
            else:
                if n > 5:
                    result = "Some damage"
                else:
                    result = "Little or no damage"

    return(result)


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    MIN_YRS = 5
    MIN_SAL = 30000
    years = int(input("Years employed:"))

    if years >= MIN_YRS:
        salary = int(input("Annual salary:"))
        if salary >= MIN_SAL:
            qualified = True
        else:
            qualified = False
    else:
        qualified = False

    return(qualified)


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER = 6
    WINGS = 8
    FRIES = 1.5
    SALAD = 2

    order = str(input("Order B - burger or W - wings: "))
    combo = str(input("Make it a combo? (Y/N): "))

    if order == "B":
        if combo == "Y":
            add_on = str(input("Add F - fries or S - salad: F"))
            if add_on == "F":
                price = BURGER + FRIES
            else:
                price = BURGER + SALAD
        else:
            price = BURGER
    else:
        if combo == "Y":
            add_on = str(input("Add F - fries or S - salad: F"))
            if add_on == "F":
                price = WINGS + FRIES
            else:
                price = WINGS + SALAD
        else:
            price = WINGS
    return(price)
