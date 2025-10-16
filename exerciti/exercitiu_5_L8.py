# Task 1
# The user types in two numbers. Find the sum and average of numbers in the specified range.
# start = int(input("Enter the first number: "))
# end = int(input("Enter the second number: "))
# if start > end:
#     start, end = end, start
# num1 = list(range(start, end + 1))
# total = sum(num1)
# average = total / len(num1)
# print(f"the sum: {total}")
# print(f"the average: {average}")


# Task 2
# The user types in a number. Calculate the factorial of a number. For instance, if the user typed in 3, the factorial is 1*2*3 = 6.
# The formula for calculating the factorial: n! = 1*2*3…*n, where n is the user-defined number.

# n = int(input("enter a number: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(f"factorial of {n} is {factorial}")

# Task 3
# The user types in the line length. Print a horizontal line made out of * of the specified length.
# For instance, if the typed in number is 7, the output will be as follows: *******.
# a = int(input("Enter a number to print a a line of the simbol * : "))
# print("*" * a)

# Task 4
# The user types in the length of a line and a symbol to fill the line. Print a horizontal line made out of the typed in symbol of the specified length.
# If the typed in number and symbol are 5 and &, the output will be as follows: &&&&&.

# a = int(input("Enter a number to print a a line of a symbol: "))
# b = str(input("Enter the symbol: "))
# print(b * a)
