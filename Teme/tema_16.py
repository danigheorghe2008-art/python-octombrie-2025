print("Task 1")
# Write a function that prints formatted text given below:
# "Don't compare yourself with anyone in this world...
#  if you do so, you are insulting yourself."
#                                           Bill Gates


def Bill_Gates_text():
    print("\"Don't compare yourself with anyone in this world...")
    print('if you do so, you are insulting yourself."')
    print("                                         Bill Gates")


Bill_Gates_text()


print("Task 2")
# Write a function that takes two numbers as a parameter and displays all even numbers in between.


def even_num_displayer():
    a = int(input("enter the start of the parameter: "))
    b = int(input("enter the end of the parameter: "))
    if a > b:
        a, b = b, a
    for i in range(a + 1, b):
        if i % 2 == 0:
            print(i, end=" ")
    print()


even_num_displayer()

print("Task 3")
# Write a function that prints an empty or solid square made out of some symbol. The function takes the following as parameters:
#  the length of the side of the square, a symbol, and a boolean variable:
# if it is True, the square is solid;
# if False, the square is empty.


def squere1(lenght: int, symbol: str, solid: bool):
    if solid == True:
        for i in range(lenght):
            print(symbol * lenght)
    else:
        print(symbol * lenght)
        for i in range(lenght - 2):
            print(symbol + " " * (lenght - 2) + symbol)
        if lenght > 1:
            print(symbol * lenght)


squere1(5, "*", False)

print("Task 4")
# Write a function that returns the smallest of five numbers. Numbers are passed as parameters.


def smallest_of_five():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    d = int(input("Enter a number: "))
    e = int(input("Enter a number: "))
    smallest = min(a, b, c, d, e)
    print("smallest number is:")
    return smallest


print(smallest_of_five())

print("Task 5")
# Write a function that returns the product of numbers in a specified range. The start and end points of the range are passed as parameters.
#  If the order of these points is incorrect (e.g., 5 is the end, and 25 is the start), swap them.


def product_of_range(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product


print(product_of_range(1, 5))

print("Task 6")


# Write a function that counts how many digits a number has. The number is passed as a parameter.
#  Return the received number of digits from the function. For example, if the passed number is 3456, it has 4 digits.


def count_digits(number):
    return len(str(abs(number)))


print(count_digits(54678))

print("Task 7")
# Write a function that checks if a number is a palindrome. The number is passed as a parameter.
#  If the number is a palindrome, return true, otherwise false.
# A palindrome is a number which reads the same backward as forward. For instance, 123321 is a palindrome,
#  546645 is a palindrome, but 421987 is not.


def polindrome_Checker_num(number):
    num = str(number)
    if num == num[::-1]:
        print("Number is a polindrome")
    else:
        print("Number is not polindrome")
    print(num)


polindrome_Checker_num(546645)
