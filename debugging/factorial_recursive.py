#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a given number n.
# The factorial of a number n (denoted as n!) is the product of all integers from 1 to n.
# For example: 5! = 5 * 4 * 3 * 2 * 1 = 120.

# Parameters:
# n (int): The number for which we want to calculate the factorial.

# Returns:
# int: The result of the factorial of n.
def factorial(n):
    if n == 0:
        return 1  # The factorial of 0 is defined as 1.
    else:
        return n * factorial(n-1)  # Recursive call to calculate the factorial.

# Retrieves the first argument passed via the command line
# and converts it to an integer. Then, we call the factorial function.
f = factorial(int(sys.argv[1]))

# Prints the result of the factorial calculation.
print(f)