name = "Nume-1"
age = 10
strMsg3 = "My name is {name}, I'm {age}".format(name="Student", age=25)
# print(strMsg3)

# strMsg3_2 = "My name is " + name + ", I'm " + str(age)
# print(strMsg3_2)


dummyText = (
    "What is Lorem Ipsum?Lorem Ipsum is simply "
    "dummy text of the printing and typesetting industry. "
    "Lorem Ipsum has been the industry's standard dummy "
    "text ever since the 1500s, when an unknown printer "
    "took a galley of type and scrambled it to make a type "
    "specimen book. It has survived not only five centuries, "
    "but also the leap into electronic typesetting, remaining "
    "essentially unchanged. It was popularised in the 1960s with "
    "the release of Letraset sheets containing Lorem Ipsum passages, "
    "and more recently with desktop publishing software like Aldus "
    "PageMaker including versions of Lorem Ipsum."
)

# print(type(dummyText))
import re


# match = re.search("\w{5}", dummyText)
# print(match.group())

# lista1 = re.findall("\w{5}", dummyText)
# print(lista1)

lista2 = re.findall(r"\b[a-zA-Z]{5}\b", dummyText)
# print(lista2)

for element in lista2:
    print(element)
