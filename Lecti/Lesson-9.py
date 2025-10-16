# if 3 > 10:
#     print("yes")
# else:
#     print("no")

# print('I"m an ...')

# normalText = """Python Arithmetic Operators:\n
# Arithmetic operators are used to perform mathematical operations like addition,
# subtraction, multiplication and division.\n
# \tThere are 7 arithmetic operators in Python:
# \t\tAddition +\n
# \t\tSubtraction -\n
# \t\tDivision /\n
# \t\tModulus %\n
# \t\tExponentiation **\n
# \t\tFloor division //\n"""
# rawText = r"""Python Arithmetic Operators:\n
# Arithmetic operators are used to perform mathematical operations like addition,
# subtraction, multiplication and division.\n
# \tThere are 7 arithmetic operators in Python:
# \t\tAddition +\n
# \t\tSubtraction -\n
# \t\tDivision /\n
# \t\tModulus %\n
# \t\tExponentiation **\n
# \t\tFloor division //\n
# """
# print(normalText)

# userLogin = input("Name from user")
# print("Welcome, " + userLogin + ". Let's start game!")

# userLogin = input("Your login: ")
# strMsg = "Welcome, {}. Let's start game!".format(userLogin)
# print(strMsg)


# strMsg3 = "My name is {name}, I'm {age}".format(name="Student", age=25)
# print(strMsg3)  # My name is Student, I'm 25
# strMsg4 = "My name is {name}, I'm {age}".format(age=25, name="Student")
# print(strMsg4)  # My name is Student, I'm 25

import string
import random

userLogin = "".join(random.sample("abc", 3))
userPass = "".join(random.sample((string.ascii_letters + string.digits), 8))
print("login:", userLogin)
print("password:", userPass)

# print(random.sample(string.ascii_lowercase, 6))
