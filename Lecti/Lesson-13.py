categoryList = ["Drama", "Comedy", "Mystery", "Romance"]

# adaug mai multe elemente ->extend
# print(categoryList.extend([1, 5, 9, 13]))

# adaug un element-->care in cazul de mai jos este o lista
# print(categoryList.append([1, 5, 9, 13]))
# print(categoryList)
# eroare,
# ["Drama", "Comedy", "Mystery", "Romance", 1, 5, 9, 13]
# print(categoryList.sort())

# for(categoryList)


# variabila1 = 10
# variabila2 = variabila1
# print("variabila2=" + str(variabila2))
# variabila2 = 20
# print("variabila1=" + str(variabila1))
# print("variabila2=" + str(variabila2))

# variabila1 = True
# variabila2 = variabila1
# variabila2 = False
# print(variabila1)
# print(variabila2)


# list1 = [1, 2, 3, 4, 5]
# print(list1)  # [1, 2, 3, 4, 5]

# list2 = list1
# list3 = list2
# print(list2)  # [1, 2, 3, 4, 5]

# list2[1] = "Hello"
# print(list3)  # [1, 'Hello', 3, 4, 5]
# print(list2)  # [1, 'Hello', 3, 4, 5]
# print(list1)  # [1, 'Hello', 3, 4, 5]


# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list3 = [1, 2, 3, 4, 5]
# print(list2 is list1)  # True
# print(list3 is list1)  # False

# list4 = list1.copy()
# print(list4 is list1)
# list5 = list(list1)


print(categoryList[0])
myTbl = [[[111, 1110], [112, 1120], [113, 1130]], [221, 222, 223]]
alDoileaElement = myTbl[1]
print(alDoileaElement)
print(alDoileaElement[0])
print(myTbl[1][0])
