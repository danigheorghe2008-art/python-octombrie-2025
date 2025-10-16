# Part 1

# Task 1

# Write a program that allows a user to calculate the quotient (division of one number by another) of two numbers.
#  The program accepts two values from the keyboard and returns the result of the operation to the screen.
#  Handle the exception that occurs during division by zero and print the error message.

# try:

#     a = float(input("enter a number: "))
#     b = float(input("enter second number: "))
#     c = a / b
#     print(c)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: you didn't enter a number")

# Task 2

# Implement the first task through a function.
#  The function must accept two parameters and display the result of division on the screen.
#  Create two versions of the function implementation:

# The first version does not handle the exception inside the function. All handling is on the outside;

# The second version handles the exception inside the function.


# def divide(a, b):
#     return a / b


# try:
#     a = float(input("enter a number: "))
#     b = float(input("enter second number: "))

#     c = divide(a, b)
#     print(c)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: you didn't enter a number")


# def divide2(a, b):
#     try:
#         c = a / b
#         print(c)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")

#     except ValueError:
#         print("Error: you didn't enter a number")


# a = input("enter a number: ")
# b = input("enter second number: ")
# divide2(a, b)

# Task 3

# Write a program that accepts a string and tries to convert it to a number.

# Handle the exception that occurs when the conversion fails, and print an error message.

# Task 4

# Implement the third task through a function.
#  The function should accept a string and display the result of the conversion on the screen.
#  Create two versions of the function implementation:

# The first version does not handle the exception inside the function. All handling is on the outside;

# The second version handles the exception inside the function.
