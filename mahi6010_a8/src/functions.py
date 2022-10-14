"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-28"
-------------------------------------------------------
"""


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    my_string = []
    my_string.append(string[0])

    for i in range(1, len(string)):
        if string[i] >= 'A' and string[i] <= 'Z':
            if i != 0:
                my_string.append(" ")

        my_string.append(string[i])

    new_string = ""
    for i in my_string:
        new_string += i
    new_string = new_string.lower()
    new_string = new_string.capitalize()
    return(new_string)


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    if string[-1] == "s" or string[-1] == "sh" or string[-1] == "ch":
        plural = string + "es"
    elif string[-1] == "y":
        if string[-2] == "a" or string[-2] == "o":
            plural = string + "s"
        else:
            string = string.replace(string[-1], "")
            plural = string + "ies"
    else:
        plural = string + "s"
    return(plural)


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    common1 = []
    common = []
    length = -1 * (len(string1))
    for x in range(-1, length, -1):
        if string1[x] == string2[x]:
            common1.append(string2[x])
        else:
            break
    for y in range(-1, -len(common1) - 1, -1):
        common.append(common1[y])
    common = ''.join(common)
    return(common)


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    dash = 0
    length = 0
    for i in range(0, len(isbn)):
        if isbn[i].isnumeric():
            valid = True
        elif isbn[i] == "-":
            valid = True
            dash += 1
            if isbn[i + 1] == "-" or isbn[i - 1] == "-":
                valid = False
        else:
            valid = False

        length += 1

    if isbn[-2] == "-":
        valid = True
    else:
        valid = False

    if isbn[0:3] == "978" or isbn[0:3] == "979":
        valid = True
    else:
        valid = False
    if dash != 4:
        valid = False
    if length != 17:
        valid = False

    return(valid)


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True
    for x in range(0, len(word_list) - 1):
        word1 = word_list[x]
        word2 = word_list[x + 1]
        if word1[-1] != word2[0]:
            word_chain = False
    return(word_chain)
