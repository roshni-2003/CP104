"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    i = 0
    line = fh.readline()
    while i < n and line != '':
        i = i + 1
        line = fh.readline()
    if line != '':
        result = line.strip().split(',')
    return result


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = (fh.readline())
    index = 0
    while line != "" and index != 1:
        if id_number in line:
            result = line.strip().split(",")
            index = 1
        else:
            line = (fh.readline())
    return result


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    line = fh.readline()
    list1 = []
    while line != "":
        num = int(line)
        list1.append(num)
        line = (fh.readline())

    smallest = list1[0]
    largest = list1[0]
    total = list1[0]
    for i in range(1, len(list1)):
        if list1[i] < smallest:
            smallest = list1[i]
        if list1[i] > largest:
            largest = list1[i]
        total = total + list1[i]
    average = total / len(list1)
    return (smallest, largest, total, average)


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    line = fh.readline()
    count = 0
    while line != "":
        line = line.strip()
        if int(line) == value:
            count = count + 1
        line = fh.readline()
    return (count)


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    line = fh.readline().strip()
    word = line.strip()
    while line != "":
        line = line.strip()
        if len(line) < len(word):
            word = line.strip()
        line = fh.readline().strip()
    return (word)


def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line = (fh.readline())
    highest = 0
    num = int(line.strip())
    while line != '':
        num = int(line.strip())
        if num > highest:
            highest = num
        line = (fh.readline())
    fh.write(f'\n{highest}')
    return highest
