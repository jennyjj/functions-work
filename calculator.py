"""
This calculator script is Part 3 of the Hackbright Prep functions exercise. Please 
complete the functions below. This first one is completed for you. Remember to 
write a sentence in your docstrings that describes what the function does. 

In further study, you'll be asked to complete the doctests as well! 
"""

#########################################################################
# This one has been completed for you
def add(num1, num2):
    """Returns the sum of two numbers.

    >>> add(7, 12)
    19
    >>> add(add(2,4), 1)
    7
    """
    sum = num1 + num2

    return sum

#########################################################################
# Complete all of the functions below

def subtract(num1, num2):

    result = num1 - num2
    return result


def multiply(num1, num2):

    product = num1 * num2
    return product


def divide(num1, num2):
    result = num1 / num2
    return result

    
    


def modulo(num1, num2):

    remainder = num2 % num2
    return remainder
    
def power(base, exponent):

    result = base ** exponent
    return result


def square(num1):

    result = num1 ** 2
    return result


#####################################################################
# Uncomment this code below when you get to further study
# This code will allow us to run our doctests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"