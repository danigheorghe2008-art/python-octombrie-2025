# def askAdditionalInfo(queryStr: str):
#     infoInd = 1
#     infoList = []
#     while True:
#         infoName = input("Name of the {} #{}:".format(queryStr, infoInd))
#         if infoName == "":
#             print("No info. Input stopped.")
#             break
#         else:
#             infoList.append(infoName)
#             infoInd += 1
#     if len(infoList) > 0:
#         if queryStr == "hobby":
#             print("You have {} hobbies.".format(infoInd - 1))
#         elif queryStr == "programming languages":
#             print("You know {} programming languages.".format(infoInd - 1))

#     else:
#         print("You have no info at all")
#     return infoList


# askAdditionalInfo(1)


# lista = [1, 2, 3]
# lista2 = list((1, 2))
# tupla = tuple((1, 2, 3))
# # tupla = ()
# # tupla = 1, 2, 3, 4

# setX = {1, 2, 3}
# setY = set({1, 2, 3, 4})


# passwordsSet = {"111", ["222", "333"]}
# passwordsSet = {"111", {"222", "333"}}
# passwordsSet = {"111", ("333", "222")}
# print(passwordsSet)

# userNames = {"Joe", "Bob", "Kate"}
# for name in userNames:
#     print(name)


# mySet = {1, 2, 3, 4, 5}
# print(mySet)
# mySet.discard(400)
# print(mySet)
# mySet.remove(500)
# print(mySet)
# mySet.discard(10)
# print(mySet)


# frozenA = frozenset(["Hanna", "Joe", "Kate"])
# frozenB = frozenset(["Bob", "Joe", "Jane", "Kate", "Jack"])
# print("frozenA:", frozenA)
# print("frozenB:", frozenB)
# print("Intersection of frozensets:")
# print(frozenA & frozenB)
# print(frozenA.intersection(frozenB))
# print("Union of frozensets:")
# print(frozenAfrozenB)
# print(frozenA.union(frozenB))
# print("Difference of two frozensets:")
# print(frozenB - frozenA)
# print(frozenB.difference(frozenA))


# word1 = input("1st word:")
# word2 = input("2nd word:")
# if set(word1) == set(word2):
#     print("Yes")
# else:
#     print("No")

word1 = input("1st word:")
word2 = input("2nd word:")
if frozenset(word1) == frozenset(word2):
    print("Yes")
else:
    print("No")


# listA = list(["Bob", "Joe", "Jane", "Kate", "Jack"])

myDict2 = {"key-1": "student", "Bucuresti, Strada Dorobanti nr.3 etc": "admin"}
