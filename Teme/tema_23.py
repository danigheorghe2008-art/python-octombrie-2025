print("Task 1")
# Write a program that asks a user for a number and calculates its factorial.
#  Handle an exception that occurs when a negative number is entered,
#  and print an error message.

import math

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")

except ValueError as e:
    print("Error: ", e)


print("Task 2")
# Implement the first task through a function. The function should take a number as a parameter and return the factorial.
#  The correctness check of the data obtained must be inside the function. Create two versions of the function implementation:
# The first version does not handle the exception inside the function. All handling is on the outside;
# The second version handles the exception inside the function.

# version 1

import math


def factorial_v1(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)


try:
    num = int(input("Enter a number: "))
    result = factorial_v1(num)
    print(f"The factorial of {num} is {result}")

except ValueError as e:
    print("Error:", e)


# version 2

import math


def factorial_v2(n):
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return math.factorial(n)
    except ValueError as e:
        print("Error:", e)
        return None


number = int(input("Enter a number: "))
result = factorial_v2(number)
if result is not None:
    print(f"The factorial of {number} is {result}")
