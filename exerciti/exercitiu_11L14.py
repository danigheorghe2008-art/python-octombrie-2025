# Task 1
# Calculate the following in a list filled with random numbers:
# Sum of negative numbers;
# Sum of even numbers;
# Sum of odd numbers;
# Product of elements with indices divisible by 3;
# Product of elements between the smallest and the largest element;
# The sum of the elements between the first and the last positive elements.

# import random

# num = [random.randint(-50, 50) for i in range(15)]
# print("Numbers:", num)


# # versiunea 2 de colegul Andrei Cristian:
# import random

# lista_numere = []
# suma_nr_negative = 0
# suma_nr_pare = 0
# suma_nr_impare = 0
# produs_elemente_divizibile = 1


# for _ in range(100):
#     numar = random.randint(-100, 100)
#     lista_numere.append(numar)

# print("Lista numer:", lista_numere)

# for numar in lista_numere:
#     if numar < 0:
#         suma_nr_negative = suma_nr_negative + numar

# print("Suma numerelor negative este:", suma_nr_negative)

# for numar in lista_numere:
#     if numar % 2 == 0:
#         suma_nr_pare = suma_nr_pare + numar

# print("Suma numerelor pare este:", suma_nr_pare)

# for numar in lista_numere:
#     if numar % 2 != 0:
#         suma_nr_impare = suma_nr_impare + numar

# print("Suma numerelor impare:", suma_nr_impare)

# for i in range(len(lista_numere)):
#     if i % 3 == 0 and lista_numere[i] != 0:
#         produs_elemente_divizibile = produs_elemente_divizibile * lista_numere[i]

# print("Produsul elementelor divizibile cu 3 este:", produs_elemente_divizibile)

# minim = min(lista_numere)
# maxim = max(lista_numere)

# index_minim = lista_numere.index(minim)
# index_maxim = lista_numere.index(maxim)

# inceput = min(index_minim, index_maxim)
# sfarsit = max(index_minim, index_maxim)

# produs_intre = 1
# for i in range(inceput + 1, sfarsit):
#     produs_intre = produs_intre * lista_numere[i]

# primul_index = None
# ultimul_index = None

# for i in range(len(lista_numere)):
#     if lista_numere[i] > 0:
#         primul_index = i
#         break

# # caut ultimul element pozitiv
# for i in range(len(lista_numere) - 1, -1, -1):
#     if lista_numere[i] > 0:
#         ultimul_index = i
#         break

# suma_intre_poz = 0
# if primul_index is not None and ultimul_index is not None and primul_index < ultimul_index:
#     for i in range(primul_index + 1, ultimul_index):
#         suma_intre_poz += lista_numere[i]

# print("Suma dintre primul si ultimul numar pozitiv:", suma_intre_poz)


print("\nTask 2")
# There is a list of integers filled with random numbers. Do the following based on this data:
# Create a list of integers containing only even numbers;
# Create a list of integers containing only odd numbers;
# Create a list of integers containing only negative numbers;
# Create a list of integers containing only positive numbers.
import random

num = [random.randint(-50, 50) for i in range(15)]
print("Numbers:", num)


even_numbers = [n for n in num if n % 2 == 0]
odd_numbers = [n for n in num if n % 2 != 0]
negative_numbers = [n for n in num if n < 0]
positive_numbers = [n for n in num if n > 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Negative numbers:", negative_numbers)
print("Positive numbers:", positive_numbers)

# versiune 2 de colegul Andrei Cristian:

# import random

# lista_numere = []
# lista_pare = []
# lista_impare = []
# lista_negative = []
# lista_pozitive = []

# for _ in range(100):
#     numar = random.randint(-100, 100)
#     lista_numere.append(numar)

# print("Lista numere:", lista_numere)

# for numar in lista_numere:
#     if numar < 0:
#         lista_negative.append(numar)
#     elif numar > 0:
#         lista_pozitive.append(numar)

#     if numar % 2 == 0:
#         lista_pare.append(numar)
#     else:
#         lista_impare.append(numar)

# print("Lista numere pare:", lista_pare)
# print("Lista numere impare:", lista_impare)
# print("Lista numere pozitive:", lista_pozitive)
# print("Lista numere negative:", lista_negative)
