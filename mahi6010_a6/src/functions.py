"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-15"
-------------------------------------------------------
"""


def winner():
    """
    -------------------------------------------------------
    Asks the user to enter a series of strings that represent
    the output of a game with a loop
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        blue - Number of times blue won the game (int >= 0)
        grey - Number of times grey won the game (int >= 0)
    ------------------------------------------------------
    """
    blue = 0
    grey = 0
    string = input("Enter the winning team: ")
    if string == "blue":
        blue += 1
    elif string == "grey":
        grey += 1

    while string != "":
        string = input("Enter the winning team: ")
        if string == "blue":
            blue += 1
        elif string == "grey":
            grey += 1
    return(blue, grey)


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = False
    i = 1
    while i <= num:
        if (num % i) == 0:
            prime = True
        i += 1
    return(prime)


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"Principal: ${principal:.2f}")
    print(f"Interest Rate: {rate:.2f}%")
    print(f"Monthly Payement: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    balance = principal
    month = 1
    rate = rate / 1200

    while balance > 0:
        interest = (balance * rate)
        balance = balance + interest - payment
        print(f"{month:>5.0f}{interest:>9.2f}{payment:>10.2f}{balance:>10.2f}")
        if balance < payment:
            interest = (balance * rate)
            payment = balance
            balance = 0
            print(f"{month:>5.0f}{interest:>9.2f}{payment:>10.2f}{balance:>10.2f}")
        month += 1

    return()


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count = 0
    if num == 0:
        count = 1

    if num < 0:
        num *= -1

    while num != 0:
        count += 1
        num = num // 10

    return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1
    while i < num:
        if num % i == 0:
            total += i
        i = i + 1

    return(total)
