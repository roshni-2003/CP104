"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-10-30"
-------------------------------------------------------
"""

import random
from random import randint


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Converts square number to day of week.
    Use: weekDay == day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - random number (0 < int < 100)
    Returns:
        day - day of the week or error associated with number (string)
    ------------------------------------------------------
    """
    if day_number == 1:
        day = "Monday"
    else:
        if day_number == 2:
            day = "Tuesday"
        else:
            if day_number == 3:
                day = "Wednesday"
            else:
                if day_number == 4:
                    day = "Thursday"
                else:
                    if day_number == 5:
                        day = "Friday"
                    else:
                        if day_number == 6:
                            day = "Saturday"
                        else:
                            if day_number == 7:
                                day = "Sunday"
                            else:
                                if day_number > 7:
                                    day = "Error"

    return(day)


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level == pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if aqi <= 400:
        if aqi <= 300:
            if aqi <= 200:
                if aqi <= 150:
                    if aqi <= 100:
                        if aqi <= 50:
                            if aqi < 0:
                                level = "Error"
                            else:
                                level = "Good"
                        else:
                            level = "Moderate"
                    else:
                        level = "Unhealthy for Sensitive Groups"
                else:
                    level = "Unhealthy"
            else:
                level = "Very Unhealthy"
        else:
            level = "Hazardous"
    return (level)


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product == product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1 > v2:
        if v1 > v3:
            if v2 > v3:
                product = v1 * v2
            else:
                product = v1 * v3
        else:
            product = v1 * v3
    elif v1 > v3:
        product = v2 * v1
    else:
        product = v3 * v2
    return(product)


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour == rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if rgb1 == "red":
        if rgb2 == "blue":
            colour = "fuchsia"
        elif rgb2 == "green":
            colour = "yellow"
        elif rgb2 == "red":
            colour = "red"
        else:
            colour = "Error"
    elif rgb1 == "blue":
        if rgb2 == "red":
            colour = "fuschia"
        elif rgb2 == "green":
            colour = "aqua"
        elif rgb2 == "blue":
            colour = "blue"
        else:
            colour = "Error"
    elif rgb1 == "green":
        if rgb2 == "blue":
            colour = "aqua"
        elif rgb2 == "red":
            colour = "yellow"
        elif rgb2 == "green":
            colour = "green"
        else:
            colour = "Error"
    else:
        colour = "Error"

    return(colour)


def yee_ha(number):
    """
    -------------------------------------------------------
    Associates number to either yee, ha, yeeha or nada
    Use: divisible == yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number (int)
    Returns:
        divisible (str)
    -------------------------------------------------------
    """

    if number % 3 == 0:
        if number % 7 == 0:
            divisible = "Yee Ha"
        else:
            divisible = "Yee"
    elif number % 7 == 0:
        divisible = "Ha"
    else:
        divisible = "Nada"

    return(divisible)


def fizzbuzz(number):
    fzbz_str = ""
    for i in range(1, number + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                fzbz_str = fzbz_str + "fizzbuzz\n"
            else:
                fzbz_str = fzbz_str + "fizz\n"
        elif i % 5 == 0:
            fzbz_str = fzbz_str + "buzz\n"
        else:
            fzbz_str = fzbz_str + str(i) + "\n"
    return(print(fzbz_str))
