# # def simpleDecorator(myFunction):
# #     print("Hello! I'm Decorator!")
# #     print("s-a executat simpleDecorator()")

# #     def simpleWrapper():
# #         print("Function starts working...")
# #         myFunction()
# #         print("See you!")

# #     return simpleWrapper


# # def simpleDecorator_v2(myFunction):
# #     print("Hello! I'm Second Decorator!")

# #     def simpleWrapper():
# #         print("Let's start...")
# #         myFunction()
# #         print("Good luck!")

# #     return simpleWrapper


# # # def sayHi():
# # #     print("Welcome!")


# # # sayHiAdvanced = simpleDecorator(sayHi)
# # # print("Print intre functii")
# # # sayHiAdvanced()


# # @simpleDecorator_v2
# # @simpleDecorator
# # def sayHi():
# #     print("Welcome!")


# # sayHi()


# def simpleDecorator_v4(myFunction):
#     print("Hello! I'm Fourth Decorator!")

#     def simpleWrapper(argX, argY):
#         print("I've got {}, {}. Function starts working...".format(argX, argY))
#         resutl = myFunction(argX, argY)
#         print("See you!")
#         return resutl

#     return simpleWrapper


# @simpleDecorator_v4
# def calculateSum_v1(a, b):
#     print("Welcome! Let's calculate...")
#     x = int(input("x: "))
#     y = int(input("y: "))
#     return x + y + a + b


# print(calculateSum_v1(3, 4))

# # calculateSum_v1 = simpleDecorator_v4(calculateSum_v1)
# # print(calculateSum_v1(3, 4))


# Exceptions

# print(1 / 0)

# try:
#     amount = int(input("Enter the amount of received items: "))
#     items_type = input("Specify the type of received items: ")
#     parts_number = int(input("Enter the number of parts: "))
#     parts_amount = amount / parts_number
# except ValueError:
#     print("We need an integer for amount!")
# except ZeroDivisionError:
#     print("You cannot divide the delivery into 0 parts")


try:
    f = open("test.txt", "w")
    # perform file operations
finally:
    f.close()
