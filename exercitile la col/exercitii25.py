# Task 1
# You have a text file. Create a new file where you should write all words consisting of at least seven letters found in the
# source file.
# Define the source and destination files
source_file = "source.txt"
destination_file = "long_words.txt"

# Open the source file for reading
# Making the file:
# with open(source_file, "w") as f:
#     text = f.read()
with open(source_file, "r") as f:
    text = f.read()

# Split the text into words (considering simple whitespace and punctuation)
import re

words = re.findall(r"\b\w{5,}\b", text)  # Words with 5 or more letters
# 1. re.findall(...)

# re.findall(pattern, string) searches the string for all non-overlapping matches of the regex pattern.

# It returns a list of all matches.

# In this case, the result is stored in words.

# 2. r"\b\w{5,}\b"

# The r before the string means raw string.

# This tells Python not to treat backslashes (\) as escape characters.

# So \b is interpreted by regex, not Python.

# Write the words to the new file, one per line
with open(destination_file, "w") as f:
    for word in words:
        f.write(word + "\n")

print(
    f"{len(words)} words with at least 5 letters have been written to '{destination_file}'."
)


# Task 1
# You have a text file. Create a new file where you should write all words consisting of at least seven letters found in the source file.

import string


def task1(fisier_sursa, fisier_destinatie):
    try:
        with open(fisier_sursa, "r") as f:
            text = f.read()

        cuvinte = text.split()

        cuvinte_lungi = []
        for cuvant in cuvinte:
            cuvant = cuvant.strip(string.punctuation)
            if len(cuvant) >= 7:
                cuvinte_lungi.append(cuvant)

        with open(fisier_destinatie, "w") as f_nou:
            for cuvant in cuvinte_lungi:
                f_nou.write(cuvant + "\n")

        print(f"Am gasit {len(cuvinte_lungi)} cuvinte lungi in fisierul original")

    except FileNotFoundError:
        print("Fisierul nu a fost gasit")
    except Exception as e:
        print(f"A aparut o eroare: {e}")


task1("task1.txt", "task1_nou.txt")


# Task 2
# # You have a text file. Write its lines to another file. The order of lines in the second file must match the order of lines in the source file.


def task2(fisier_sursa, fisier_destinatie):
    try:
        with open(fisier_sursa, "r") as fisier:
            linii = fisier.readlines()

        with open(fisier_destinatie, "w") as fisier_nou:
            fisier_nou.writelines(linii)

        print(
            f"{len(linii)} linii au fost copiate din {fisier_sursa} în {fisier_destinatie}"
        )

    except FileNotFoundError:
        print("Eroare: fisierul sursa nu a fost gasit!")
    except Exception as e:
        print(f"A aparut o eroare: {e}")


task2("task2.txt", "task2_nou.txt")


# Task 3
# You have a text file. Write its lines to another file. The order of lines in the second file must be inverse.


def task3(fisier_sursa, fisier_destinatie):
    try:
        with open(fisier_sursa, "r") as fisier:
            linii = fisier.readlines()

        linii_invers = linii[::-1]

        with open(fisier_destinatie, "w") as fisier_nou:
            fisier_nou.writelines(linii_invers)

        print(
            f"{len(linii)} linii au fost copiate din {fisier_sursa} în {fisier_destinatie}"
        )

    except FileNotFoundError:
        print("Eroare: fisierul sursa nu a fost gasit!")
    except Exception as e:
        print(f"A aparut o eroare: {e}")


# Task 4
# You have a text file. Add a line consisting of twelve asterisks (************) after the last line among the lines that have no comma.
# If there are no such lines in the file, the asterisks should be added after all lines of the existing file. Write the result to another file.


def task4(fisier_sursa, fisier_destinatie):
    try:
        with open(fisier_sursa, "r") as f:
            linii = f.readlines()

        linii_curate = [linie.rstrip("\n") for linie in linii]

        index_ultima = -1
        for i, linie in enumerate(linii_curate):
            if "," not in linie:
                index_ultima = i

        rezultat = []
        for i, linie in enumerate(linii_curate):
            rezultat.append(linie)
            if i == index_ultima:
                rezultat.append("************")

        if index_ultima == -1:
            rezultat.append("************")

        with open(fisier_sursa, "w") as f_out:
            for linie in rezultat:
                f_out.write(linie + "\n")

    except FileNotFoundError:
        print("Fisierul nu a fost gasit")
    except Exception as e:
        print("Eroare:", e)


task4("task4.txt", "task4_nou.txt")

# Task 5
# You have a text file. Calculate the number of words that begin with a character set by the user.


def task5(fisier_sursa):

    try:
        with open(fisier_sursa, "r") as fisier:
            text = fisier.read()
            cuvinte = text.split()
            caracter = input("Introduceti caracterul: ")
            numar_cuvinte = 0
            for cuvant in cuvinte:
                if cuvant.startswith(caracter):
                    numar_cuvinte = numar_cuvinte + 1
            print(
                f"Numarul de cuvinte care incep cu caracterul {caracter} este: {numar_cuvinte}"
            )
    except FileNotFoundError:
        print("Fisierul nu a fost gasit")
    except Exception as e:
        print(f"A aparut o eroare: {e}")


task5("task5.txt")


# Task 6
# You have a text file. Write all its lines to another file while replacing * with & and vice versa.


def task6(fisier_sursa, fisier_destinatie):

    try:
        with open(fisier_sursa, "r") as fisier:
            linii = fisier.readlines()
            for i in range(len(linii)):
                linii[i] = linii[i].replace("*", "&")

        with open(fisier_destinatie, "w") as fisier_nou:
            fisier_nou.writelines(linii)
    except FileNotFoundError:
        print("Fisierul nu a fost gasit")
    except Exception as e:
        print("Eroare:", e)


task6("task6.txt", "task6_nou.txt")
