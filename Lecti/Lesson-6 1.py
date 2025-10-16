# valoareDeLaUtilizator = int(input("Varsta ta este: "))
# print(valoareDeLaUtilizator)


# print(bool(0))  # False
# print(bool(" "))  # True
# print(bool(0.0))  # False
# print(bool(None))  # False
# print(bool("IT Step Academy"))  # True
# print(bool(1))  # True

# numarGeamuri = 0
# print(numarGeamuri)

# numarGeamuriDinCladire = None
# print(numarGeamuriDinCladire + 1)


# numarDulapuri = 5
# numarUsi = 2
# if not (numarDulapuri == 3 and numarUsi == 2):
#     print("Camera este mobilata")
# else:
#     print("Camera nu este mobilata")


# number = int(input("Enter the answer number: "))
# if number == 1:
#     print("You've chosen answer A")
# else:
#     if number == 2:
#         print("You've chosen answer B")
#     else:
#         if number == 3:
#             print("You've chosen answer C")
#         else:
#             if number == 4:
#                 print("You've chosen answer D")
#             else:
#                 print("There is no such answer.")


# account = int(input("Enter how much you put: "))
# account = abs(account)

# if account > 0:
#     withdrawal = int(input("Enter how much you take: "))
#     withdrawal = abs(withdrawal)
#     if withdrawal < account:
#         # account -= withdrawal
#         account = account - withdrawal
#         print("Here are your", withdrawal, ".")
#         print("There are", account, "left.")
#     else:
#         print("There are only", account, ".")
# else:
#     print("There are no money in piggy bank")


# number = 1
# while number < 20:
#     print(number, "is greater than 0 and less than 3")
#     number = number + 1
#     number += 1


line = input("Enter some string: ")
for c in line[0:6:1]:
    print(c)
