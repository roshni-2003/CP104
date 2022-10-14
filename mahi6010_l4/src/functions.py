"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
from math import pi


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """

    diam = radius * 2
    return diam


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """
    radius = (s1**2 + s2**2)**(1 / 2)
    diam = radius * 2
    circ = 2 * 3.14 * radius
    area = pi * radius**2
    return (radius, diam, circ, area)


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    num = int(num1 * num2)
    den = int(den1 * den2)
    product = float(num / den)

    return (num, den, product)


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    F_FREEZING = 32
    farenheit = (celsius * 9 / 5) + F_FREEZING
    return farenheit


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    S_IN_D = 60 * 60 * 24
    S_IN_H = 60 * 60
    S_IN_M = 60

    days = seconds // S_IN_D
    hours = seconds // S_IN_H
    minutes = seconds // S_IN_M
    return (days, hours, minutes)


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    S_P_H = 3600
    S_P_M = 60
    DAY = int(initial_seconds // (24 * S_P_H))
    initial_seconds = initial_seconds % (24 * S_P_H)
    HOUR = int(initial_seconds // S_P_H)
    initial_seconds %= S_P_H
    MINUTES = int(initial_seconds // S_P_M)
    initial_seconds %= S_P_M
    SECONDS = int(initial_seconds)

    return(DAY, HOUR, MINUTES, SECONDS)
