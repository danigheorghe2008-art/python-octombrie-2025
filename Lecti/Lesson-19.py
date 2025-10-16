# def userGreetings(login="utilizatorNecompletat", passw="111"):
#     if login == "admin":
#         print("Welcome, admin")
#     elif login == "student":
#         print("Welcome, student")
#     elif login == "utilizatorNecompletat":
#         print("Nu ati completat numele de utilizator")
#     else:
#         print("Welcome, guy")


# userGreetings()

# print()

# import math
# import random

# random.random()


# import string

# print(string.ascii_letters)


# def calculateExample1():
#     baseVar = int(input("input base variable: "))
#     resultVar = baseVar**2
#     print(f"The square of {baseVar} is: {resultVar}")


# calculateExample1()
# print(baseVar)


# userName = "Bob"


# def checkUser():
#     userLog = input("Input your login: ")
#     global userName
#     userName = "Jane"
#     if userLog == "admin":
#         # print("{} is admin".format(userName))
#         print(f"{userName} is admin")
#     else:
#         print("{} is user".format(userName))


# checkUser()
# print("print: " + userName)


counter = 0


def functieTest(a, b):
    print("def function")
    global counter
    counter = counter + 1
    if counter == 3:
        return
    functieTest(a, b)


functieTest(1, 2)
