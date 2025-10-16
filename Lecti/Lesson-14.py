# myEmptyTuple1 = ()
# myEmptyTuple2 = tuple()


# print(myEmptyTuple1)
# print(type(myEmptyTuple1))
# print(myEmptyTuple1)
# print(type(myEmptyTuple2))

# myTuple1 = ("element1", 12, 35.6, False)
# myTuple2 = "item1"
# userTypes = "admin", "student", "teacher"
# userName = ("Jane",)

# print("myTuple1:", myTuple1, "type: ", type(myTuple1))
# print("myTuple2:", myTuple2, "type: ", type(myTuple2))
# print("userTypes:", userTypes, "type: ", type(userTypes))
# print("userName:", userName, "type: ", type(userName))

# tupleOfList = tuple(([1, 2, 3], (4, 5, 6), [7, 8, 9]))
# print(tupleOfList)


# userTypes = ("admin", "student", "teacher", "moderator")
# # print("1st two users:", userTypes[:2])
# # print("1st two users:", userTypes[0:2])
# print("2nd and 3rd users:", userTypes[1:3])

# userTypes = ("admin", "student", "teacher", "moderator")
# # userTypesList=["admin", "student", "teacher", "moderator"]
# # creare lista goala, for(in tuple) -> append in lista goala.
# userTypesList = list(userTypes)

# userTypes[0] = "user"
# print(userTypesList)

# userTypes = ("admin", "student", "teacher", "moderator")
# user1, user2, user3, user4 = userTypes
# # user1 = userTypes[0]
# # user2 = userTypes[1]
# # user3 = userTypes[2]
# # user4 = userTypes[3]
# print(user1)  # admin
# print(user2)  # student
# print(user3)  # teacher
# print(user4)  # moderator

# userTypes = ("admin", "student", "teacher", "moderator")
# user1, *users = userTypes
# print(user1)  # admin
# print(users)  # ['student', 'teacher', 'moderator']


# userTypes = ("admin", "student", "teacher", "moderator")
# for user in userTypes:
#     print(user)

# userTypes = ("admin", "student", "teacher", "moderator")
# # print(len(userTypes))
# for i in range(len(userTypes)):
#     print(userTypes[i])
userTypes1 = ("admin", "student", "teacher", "moderator")
userTypes2 = ("user1", "user2")
# userTypes1 = 10
# print(userTypes1)
userTypes1 = userTypes1 + userTypes2
for user in userTypes1:
    print(user)
