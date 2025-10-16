# Task 1
# The user inputs a fruit from the keyboard. Display the number of times this fruit occurs as an element.
# Task 2
# Improve Task 1 by adding the possibility to calculate how many times this fruit occurs as a part of an element. Here, for example, "banana, apple, bananamango, mango, 
# strawberry-banana".
# The word "banana" occurs three times.
# Task 3
# You have a tuple containing names of car manufacturers (a name may occur from 0 to N times). The user inputs a manufacturer and a replacement word. 
# Replace all elements in the tuple with the replacement word. The match must be complete.
# Task 4
# You have a tuple of integers. Display statistics on the number of digits in tuple elements. For instance:
# One digit — 3 elements;
# Two digits — 4 elements;
# # Three digits — 5 elements.

import random

fructe = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
user_input = input("Introdu un fruct: ").strip().lower()
contor = fructe.count(user_input)
print(f"Task 1 : Fructul {user_input} apare de {contor} ori")

contor_partial = 0
for element in fructe:
    element_lower = element.lower()
    start = 0
    while True:
        pozitie = element_lower.find(user_input, start)
        if pozitie == -1:
            break
        contor_partial += 1
        start = pozitie + 1

print(f"Task 2 : Fructul {user_input} apare de {contor_partial} ori")

producatori = ("Audi", "Mercedes", "Toyota", "Audi", "Renault", "Volkswagen", "Dacia", "Renault", "BMW", "Honda", "Toyota", "Renault")

print(producatori)

input_task3 = input("Introdu producatorul pe care vrei sa il inlocuiesti: ").strip()
inlocuitor = input("Introdu cu ce cuvant sa il inlocuiesc: ").strip()

cuv_inlocuit = []
for producator in producatori:
    if producator == input_task3:
        cuv_inlocuit.append(inlocuitor)
    else:
        cuv_inlocuit.append(producator)

cuv_inlocuit = tuple(cuv_inlocuit)
print(f"Task 3 : Rezultatul tuplei este {cuv_inlocuit}")


numere_random = []
for _ in range(0, 20):
    numar = random.randint(-999, 999)
    numere_random.append(numar)

tupla_numere = tuple(numere_random)

print(f"Lista numere: ", tupla_numere)

o_cifra = []
doua_cifre = []
trei_cifre = []

for numar in tupla_numere:
    cifre = len(str(abs(numar)))
    if cifre == 1:
        o_cifra.append(numar)
    elif cifre == 2:
        doua_cifre.append(numar)
    elif cifre == 3:
        trei_cifre.append(numar)
    
print(f"Task 4 : {len(o_cifra)} cifre, {len(doua_cifre)} numere de 2 cifre, {len(trei_cifre)} numere de 3 cifre")

