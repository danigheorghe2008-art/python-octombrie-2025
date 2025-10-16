categoryList = ["Drama", "Comedy", "Mystery", "Romance"]
# for category in categoryList:
#     print(category)
# print(categoryList[0])


# for i in range(len(categoryList)):
#     print(categoryList[i])
#     if i == 2:
#         print("Ai o reducere la produsul: " + categoryList[i])

categoryList.append("Produs nou")
# categoryList.extend(["Produs-2", "Produs-3"])
# categoryList.insert(0, "Produs-0")
# categoryList.remove("Comedy")
# print(categoryList)

# print(categoryList.index("Comedy"))
# print("Index-ul produsului Produs-0 este: " + str(categoryList.index("Drama")))


# adaug mai multe elemente ->extend
# print(categoryList.extend([1, 5, 9, 13]))

# adaug un element-->care in cazul de mai jos este o lista
print(categoryList.append([1, 5, 9, 13]))
print(categoryList)
# print(categoryList.sort())

# cart = ["Laptop", "Mouse"]
# cart.append("Mouse")
# print(cart)

customers = ["Bob", "Anna", "Joe", "Bob", "Nick"]
for customer in customers:
    if customer == "Bob":
        print(True)
        break
