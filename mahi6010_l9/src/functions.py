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


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    if chemical.endswith('OH') is True:
        hydroxide = True
    else:
        hydroxide = False
    return(hydroxide)


def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    if url.endswith('com'):
        url_type = "business"
    elif url.endswith('org'):
        url_type = "non-profit"
    else:
        url_type = "other"
    return(url_type)


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product id.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    category = product_code[:3]
    _id = product_code[3:7]
    qualifier = product_code[7:]

    if len(category) == 3 and category.isupper():
        print(f"Category {category:s} is valid.")
    else:
        print(f"Category {category:s} is not valid.")

    if len(_id) == 4 and _id.isnumeric():
        print(f"ID {_id} is valid.")
    else:
        print(f"ID {_id} is not valid.")

    if qualifier and qualifier[0].isupper():
        print(f"Qualifier {qualifier} is valid.")
    else:
        print(f"Qualifier {qualifier} is not valid.")

    return()


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """

    lowercase = s.lower()

    vowel_counts = {}

    for vowel in "aeiou":
        count = lowercase.count(vowel)

        vowel_counts[vowel] = count

    counts = vowel_counts.values()

    count = sum(counts)
    return(count)


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """

    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    for character in txt:
        if character.isupper():
            uppr += 1
        elif character.islower():
            lowr += 1
        elif character.isspace():
            whtspc += 1
        elif character.isdigit():
            dgts += 1

    return(uppr, lowr, dgts, whtspc)


def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = s.replace(',', '.')
    return(out)


def total_digits(s):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    num_list = []
    total = 0
    for char in s:
        if char.isnumeric():
            num_list.append(char)

    for i in range(0, len(num_list) + 1):
        total += i

    return(total)
