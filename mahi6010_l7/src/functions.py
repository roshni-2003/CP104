"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-05"
-------------------------------------------------------
"""
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)

    guess = int(input("Guess: "))
    tries = 1
    while guess != number:
        if guess > number:
            print("Too high, try again.")
        else:
            print("Too low, try again.")
        guess = int(input("Guess: "))
        tries += 1
    print("Congratulations - good guess!")
    return(tries)


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    while current < target:
        add = current * rate / 100
        current = current + add
        years += 1

    return(years)


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    num = float(input("First value: "))
    minimum = num
    maximum = num
    total = num
    n = 1
    while num >= 0:
        num = float(input("Next value: "))
        if num < 0:
            average = total / n
        else:
            total = total + num
            if num < minimum:
                minimum = num
            elif num > maximum:
                maximum = num
            n += 1
    return(minimum, maximum, total, average)


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    y_or_n = "Y"
    day = 1
    breakfast_total = 0
    lunch_total = 0
    supper_total = 0
    while y_or_n == "Y":
        print(f"For Day {day}")
        print()
        breakfast = float(input("How much was breakfast? $"))
        breakfast_total = breakfast_total + breakfast
        lunch = float(input("How much was lunch? $"))
        lunch_total = lunch_total + lunch
        supper = float(input("How much was supper? $"))
        supper_total = supper_total + supper
        total = breakfast + lunch + supper
        print(f"Your total for the day was ${total:.2f}")
        print()
        y_or_n = input("Were you away another day (Y/N)?")
        print()

    grand_total = breakfast_total + lunch_total + supper_total

    return(breakfast_total, lunch_total, supper_total, grand_total)


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    num = int(input(f"Enter a value between {low} and {high}: "))
    while num > high or num < low:
        if num > high:
            print("Value entered is too high")
            num = int(input(f"Enter a value between {low} and {high}: "))
        else:
            print("Value entered is too low")
            num = int(input(f"Enter a value between {low} and {high}: "))
    return(num)
