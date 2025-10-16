# Task 1
# Write a function that prints formatted text given below:
# Plain Text
# "Don't let the noise of others' opinions
# drown out your own inner voice."Steve Jobs


def text123():
    print("Don't let the noise of others' opinions")
    print("drown out your own inner voice.'Steve Jobs'")


# Task 2
# Write a function that takes two numbers as a parameter and displays all odd numbers in between.


def print_odds_between(a, b):
    for num in range(a + 1, b):
        if num % 2 != 0:
            print(num, end=" ")
    print()


a = int(input("Da un nr. de unde sa inceapa: "))
b = int(input("Da un nr. de unde sa se termine: "))
print_odds_between(a, b)
# versiunea lui ovidiu:

# n = int(input("da mi nr: "))

# def impar(a):
#     c = []
#     for i in range(a):
#         if i % 2 != 0:
#             c.append(i)
#     print(*c, sep=",")
#     return c


# f = impar(n)
# print(f)


# Task 3
# Write a function that prints a horizontal or vertical line made out of some symbol.
#  The function takes the following as a parameter: the line's length, direction, symbol.


def VHprinter(length, direction, symbol):
    if direction.lower == "horizontal":
        print(symbol * length)
    elif direction.lower == "vertical":
        for i in range(length):
            print(symbol)


# versiunea lui ovidiu:

# a = int(input("da mi dimensiune"))
# b = input("da mi simbol")
# c = input("directie: ")


# def afisare1(a, b, c):
#     if c.lower() == "orizontal":
#         print(b * a)
#     elif c.lower() == "vertical":
#         for i in a:
#             print(b)


# afisare1(a, b, c)


# Task 4
# Write a function that returns the greatest of four numbers. Numbers are passed as parameters.

# versiunea lui ovidiu:


# def maxi():
#     n1 = list(map(int, input().split(",")))
#     print(max(n1))


# Task 5
# Write a function that returns the sum of numbers in a specified range. The start and end points of the range are passed as parameters.

# versiunea lui ovidiu:

# n1 = int(input("da mi limita inferioara"))
# n2 = int(input("da mi limita superioara"))


# def sum(a, b: int, int) -> int:
#     c = 0
#     d = min(a, b)
#     g = max(a, b)
#     for i in range(d, g):
#         c += i
#     return c


# s = sum(n1, n2)

# Task 6
# Write a function that checks if a number is prime. The number is passed as a parameter. If the number is prime, return true, otherwise false.
# versiunea lui ovidiu:

# n = int(input("da mi nr: "))


# def prim(a):
#     d = 0
#     if a < 2:
#         return False
#     else:
#         for i in range(2, a):
#             if a % i == 0:
#                 d += 1
#                 break
#         if d == 0:
#             return True
#         else:
#             return False


# t = prim(n)
# print(t)

# Task 7
# Write a function that checks if a six-digit number is lucky. The number is passed as a parameter. If the number is lucky, return true, otherwise false.
# # A lucky six-digit number is a number with the sum of its first three digits being equal to the sum of its last three digits. For example, 123420 is a lucky number because 1+2+3 = 4+2+0, and 723422 is not because 7+2+3 != 4+2+2.
# versiunea lui ovidiu:

# import string
# import random

# n = random.sample(range(1, 9), 6)
# print(n)


# def lucky(n: int):
#     s = 0
#     s1 = 0
#     for i in range(len(n)):
#         if i < 3:
#             s += n[i]
#         else:
#             s1 += n[i]
#     if s == s1:
#         print("{} is lucky".format(int(n)))
#     else:
#         print("{} is not lucky".format(int(n)))


# lucky(n)
