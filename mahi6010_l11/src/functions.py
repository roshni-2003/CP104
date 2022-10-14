"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2021-12-03"
-------------------------------------------------------
"""
from random import randint
from random import uniform


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(0, rows):
        list1 = []
        for j in range(0, cols):
            if value_type == "int":
                list1.append(randint(low, high))
            elif value_type == "float":
                list1.append(uniform(low, high))
        matrix.append(list1)
    return(matrix)


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(0, rows):
        list1 = []
        for j in range(0, cols):
            rand = randint(0, 25)
            list1.append(letter[rand])
        matrix.append(list1)
    return(matrix)


def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    row = len(matrix)
    count = 0
    total = 0

    for i in range(0, row):
        for j in range(0, len(matrix[i])):
            if (matrix[i][j]) <= smallest:
                smallest = matrix[i][j]
            else:
                largest = matrix[i][j]
            total += matrix[i][j]
            count += 1

    average = total / count

    return(smallest, largest, total, average)


def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j] * num
    return


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of ?)
        matrix2 - the second matrix (2D list of ?)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    equal = True
    row1 = len(matrix1)
    col1 = len(matrix1[0])
    row2 = len(matrix2)
    col2 = len(matrix2[0])

    if row1 != row2 or col1 != col2:
        equal = False
    else:
        for i in range(0, len(matrix1)):
            for j in range(0, len(matrix1[i])):
                if matrix1[i][j] != matrix2[i][j]:
                    equal = False

    return(equal)
