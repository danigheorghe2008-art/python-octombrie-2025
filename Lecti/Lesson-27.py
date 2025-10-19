# class Student:
#     age = 20
#     name = "Bob"


class Student:
    spec = "Computer science"

    def __init__(self, named, aged):
        self.name = named
        self.age = aged

    def showInfo(self):
        return f"Student {self.name} is {self.age} years old."

    def showMsg(self, msgText):
        return f"Student {self.name} says '{msgText}'."


student1 = Student("Nume-1", 20)
student2 = Student("Nume-2", 21)
student3 = Student("Nume-3", 22)
student4 = Student("Nume-4", 23)
student5 = Student("Nume-5", 24)

print(type(student1))
print(student1.name)
