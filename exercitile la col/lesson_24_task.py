# Task 1
# Write a program that asks a user for a number and calculates its square root. Handle an exception that occurs when a negative number is entered, 
# and print an error message.

import math

try:
    num = float(input("Enter a number: "))
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
   
    result = math.sqrt(num)
    print(f"The square root of {num} is {result}")
 
except ValueError as e:
    print("Error:", e)

# Task 2
# Implement the first task through a function. The function must take a number as a parameter and return the square root of the number. 
# The correctness check of the data obtained must be inside the function. Create two versions of the function implementation:
# The first version does not handle the exception inside the function. All handling is on the outside;
# The second version handles the exception inside the function.

import math
 
def safe_sqrt(num):
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(num)
 
 
try:
    value = float(input("Enter a number: "))
    result = safe_sqrt(value)
    print(f"The square root of {value} is {result}")
except ValueError as e:
    print("Error:", e)

 
def task2_v1(numar):
    if numar < 0:
        raise ValueError("Eroare: Numarul trebuie sa fie pozitiv")
    return numar ** 0.5
 
try:
    numar = float(input("Introduceti un numar: "))
    rezultat = task2_v1(numar)
    print(f"Radicalul numarului {numar} este {rezultat}")
except ValueError as e:
    print(f"Eroare: {e}")
except Exception as e:
    print(f"Eroare neasteptata: {e}")

def task2_v2():
    try:
        numar = float(input("Introduceti un numar: "))
        if numar < 0:
            raise ValueError("Eroare: Numarul trebuie sa fie pozitiv")
        rezultat = numar ** 0.5
        print(f"Radicalul numarului {numar} este {rezultat}")
    except ValueError as e:
        print(f"Eroare: {e}")
    except Exception as e:
        print(f"Eroare neasteptata: {e}")
 
task2_v2()

# Task 3
# Write a program that allows a user to fill a dictionary from the keyboard with key/value pairs. After receiving the data, display a menu that 
# allows you to perform the following operations:
# Displaying the dictionary;
# Searching for a value in the dictionary;
# Replacing a value in the dictionary. A value must be found by the key;
# Displaying a value by the key entered by a user;
# Deleting a value by the key entered by a user.
# Handle an exception that occurs when the dictionary is exceeded (a user entered an invalid key), and print an error message.

dictionar = {}
 
def afisare_meniu():
    print("--------Meniu--------")
    print("1. Afisare dictionar")
    print("2. Cautare valoare")
    print("3. Inlocuire valoare")
    print("4. Cauta o valoare")
    print("5. Sterge o valoare")
    print("6. Adauga o valoare")
    print("0. Iesire")
 
def adaugare_valoare():
    key = input("Introduceti cheia: ")
    value = input("Introduceti valoarea: ")
    dictionar[key] = value
    print("Valoarea a fost adaugata")
 
def afisare_dictionar():
    for key, value in dictionar.items():
        print(f"{key}: {value}")
 
def cautare_valoare():
    key = input("Introduceti cheia: ")
    if key in dictionar:
        print(f"Valoarea pentru cheia {key} este: {dictionar[key]}")
    else:
        print("Cheia nu exista in dictionar")
 
def inlocuire_valoare():
    key = input("Introduceti cheia: ")
    if key in dictionar:
        value = input("Introduceti noua valoare: ")
        dictionar[key] = value
        print("Valoarea a fost inlocuita")
    else:
        print("Cheia nu exista in dictionar")
 
def cautare_si_afisare_valoare():
    try:
        key = input("Introduceti cheia: ")
        print(f"Valoarea pentru cheia {key} este: {dictionar[key]}")
    except KeyError:
        print("Eroare: cheia nu exista în dictionar")
 
def stergere_valoare():
    try:
        key = input("Introduceti cheia: ")
        del dictionar[key]
        print("Valoarea a fost stearsa")
    except KeyError:
        print("Eroare: cheia nu exista în dictionar")
 
while True:
    afisare_meniu()
    optiune = int(input("Introduceti optiunea: "))
    match optiune:
        case 1:
            afisare_dictionar()
        case 2:
            cautare_valoare()
        case 3:
            inlocuire_valoare()
        case 4:
            cautare_si_afisare_valoare()
        case 5:
            stergere_valoare()
        case 6:
            adaugare_valoare()
        case 0:
            break
        case _:
            print("Optiune invalida")