"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-12-05"
-------------------------------------------------------
"""


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fh.readline()
    i = 0
    while i < linecount and line != '':
        print(line, end="")
        line = fh.readline()
        i += 1
    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    line = fh.readline()
    my_list = []
    while line != '':
        if line.endswith('\n'):
            line = line[0:-1]
        my_list.append(line.split(","))
        line = fh.readline()
    for i in my_list:
        for j in i:
            if j.isnumeric():
                j = int(j)
                if j > 0:
                    numbers.append(j)
    return(numbers)


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    line = fh.readline()
    main = []
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    while line != '':
        mini = list(line)
        for i in mini:
            main.append(i)
        line = fh.readline()
    for i in main:
        if i.isdigit():
            dcount += 1
        if i.isalpha():
            if i.islower():
                lcount += 1
            else:
                ucount += 1
        if i == " ":
            wcount += 1
    return(ucount, lcount, dcount, wcount)


def flatten(matrix):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list matrix. A 'flattened' list is a
    2D list that is converted into a 1D list by rows.
    matrix must be unchanged.
    Use: flat = matrix_flatten(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of int)
    Returns:
        flat - the flattened version of matrix (list of int)
    -------------------------------------------------------
    """
    flat = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            flat.append(matrix[i][j])

    return(flat)


def matrix_rotate_right(matrix):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: rotated = matrix_rotate_right(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2d list of int/float)
    Returns:
        rotated - the rotated version of matrix (2D list of int/float)
    -------------------------------------------------------
    """
    rotated = []
    for i in range(0, len(matrix[0])):
        list1 = []
        rotated.append(list1)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            rotated[j].append(matrix[i][j])
    for i in range(0, len(rotated)):
        rotated[i].sort(reverse=True)
    return(rotated)


def get_addresses(fh):
    """
    -------------------------------------------------------
    Reads an addresses from fh into a list of addresses.
    Addresses are stored in fh in the form:
        name
        street
        city
        postal code
        --
    Each address in the list of addresses is a list of the form:
    [name, street, city, postal code]
    Use: addresses = get_addresses(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        addresses - the addresses from fh (list of str)
    -------------------------------------------------------
    """
    line = fh.readline().strip()
    addresses = []
    temp = []

    while line != "":
        if line == "--":
            addresses.append(temp)
            temp = []
        else:
            temp.append(line)

        line = fh.readline().strip()
    return(addresses)
