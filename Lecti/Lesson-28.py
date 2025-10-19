# class Student:
#     age = 20
#     name = "Bob"

import random


# class Student:
#     spec = "Computer science"

#     # public
#     def __init__(self, named, aged):
#         self.name = named
#         # public property
#         self.age = aged
#         # private property
#         self.__personID = random.randint(1, 100)

#     def __getPersonID(self):
#         return f"{self.__personID}"

#     def getPersonIDPublic(self):
#         return f"{self.__getPersonID()}"

#     def showInfo(self):
#         return f"Student {self.name} is {self.age} years old."

#     def showMsg(self, msgText):
#         return f"Student {self.name} says '{msgText}'."


# student1 = Student("Nume-1", 20)
# student2 = Student("Nume-2", 21)
# student3 = Student("Nume-3", 22)
# student4 = Student("Nume-4", 23)
# student5 = Student("Nume-5", 24)

# print(type(student1))
# print(student1.name)
# print(student1.showInfo())
# print(student1.__getPersonID())
# student1.__personID = 1111
# print(student1.__personID)
# print(student1.getPersonIDPublic())


class Person:
    def __init__(self, firstName: str, lastName: str, age: int):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

    def getHi(self, msgText):
        return f"{msgText}! I am {self.firstName}."

    # def showInfo(self):
    #     return f"Student {self.name} is {self.age} years old."


personX = Person("Prenume-1", "Nume-1", 20)
# print(personX.firstName)


class Student(Person):
    spec = "Computer Science"

    def isSuccessful(self, meanScore):
        return True if meanScore <= 75 else False


student1 = Student("Alex", "Popescu", 21)
print(student1.lastName)
