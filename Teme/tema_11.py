print("\nTask 1")
# The user types in a number. Determine how many digits this number has, find their sum and average.
#  Determine how many zeros this number has. Implement a dialog with the user through a menu.


while True:
    num = input("enter number: ")
    if not num.isdigit() and not (num.startswith("-") and num[1:].isdigit()):
        print("Invalid input. Please enter an integer.")
        continue

    print(
        "\nMeniu:\n 1.how many digits this number has\n2.sum\n3.average\n4.how many zeros this number has\n5.Exit"
    )
    ops = input("your choice: ")

    digits = [int(d) for d in num if d.isdigit()]
    digit_count = len(digits)
    digit_sum = sum(digits)
    digit_average = digit_sum / digit_count if digit_count > 0 else 0
    zero_count = digits.count(0)

    if ops == "1":
        print(digit_count)

    elif ops == "2":
        print(digit_sum)

    elif ops == "3":
        print(digit_average)

    elif ops == "4":
        print(zero_count)

    elif ops == "5":
        break


print("\nTask 2")
# Write a program that displays a chessboard with a set cell size. For example, three,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***

cell = 3  # dimensiunea unei celule
size = 6  # numărul de celule pe o linie

for r in range(size):
    for _ in range(cell):
        for c in range(size):
            print(("***" if (r + c) % 2 == 0 else "---"), end="")
        print()


print("\nTask 3")
# Write a program that tests users for their multiplication table skills.
#  The program prints two numbers, and the user must enter their product.
#  Develop several levels of difficulty (they should differ in complexity and number of questions).
#  Print the points that represent the user's skills.

import random

print("\nMeniu")
print("1. Easy (1-10) 5 questions")
print("2. Medium (1-100) 10 questions")
print("3. Hard (1-200) 15 questions")

choice = input("Enter your choice: ")
if choice == "1":  # <--------trebuie sa pun nr. in "" daca nu pun int la input
    low, high, questions = 1, 10, 5
elif choice == "2":
    low, high, questions = 1, 100, 10
elif choice == "3":
    low, high, questions = 1, 200, 15

score = 0
for i in range(questions):
    a = random.randint(low, high)
    b = random.randint(low, high)
    answer = input(f"{a} x {b} = ")
    if answer.isdigit() and int(answer) == a * b:
        score += 1
        print("Corect!")
    else:
        print(f"Wrong. The answer is {a * b}")

print(f"Your score: {score}/{questions}")

print("\nTask 4")
# Print a rhombus made out of asterisks.

n = int(input("Enter half the rhombus height: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
