# Print the multiplication table for the user-defined number. If the user typed in 7,
# the output should be as follows:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# …
# Task 2
# Write a currency converter program. Implement a dialog with the user through a menu.
# Task 3
# The user types in the start and end points of the range and a number. If the number is not in the range,
# the program asks the user to re-enter the number, and so on until the user enters the number correctly.
#  The program displays all numbers in the range, highlighting the number with exclamation marks.
# For instance: 1 2 3 !4! 5 6 7.

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start > end:
    start, end = end, start
while True:
    numar = int(input(f"Enter a number between {start} and {end}: "))
    if start <= numar <= end:
        break
    else:
        print("The number is not in the range. Try again.")


for i in range(start, end + 1):
    if i == numar:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")

# Task 4
# Develop a game Guess the Number. The program chooses a number in the range from 1 to 500.
#  The user tries to guess it. After each try, the program gives hints on whether the number is greater or less
#  than the guessed number.
# In the end, the program displays statistics: how many tries it took to guess the number, how long it took.
# Provide an exit by entering 0 if the user is tired of guessing the number.

import time
import random

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 500.")
print("Try to guess it (Enter 0 anytime to quit).")

starttime = time.time()
secretnumber = random(range(1, 500))
tries = 0
while True:
    guess = int(input("Your guess: "))
    if guess == secretnumber:
        print("you guessed the number!")
    elif guess < secretnumber:
        print("My number is greater than your guess.")
    elif guess > secretnumber:
        print("My number is smaller than your guess.")

    tries += 1


# varianta de la chat gpt :
import random
import time

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 500.")
print("Try to guess it! (Enter 0 anytime to quit)")

# generate random number
secret_number = random.randint(1, 500)

# start time
start_time = time.time()

tries = 0

while True:
    guess = int(input("Your guess: "))

    if guess == 0:
        print("You've chosen to stop playing. Goodbye!")
        break

    tries += 1

    if guess < secret_number:
        print("My number is greater than your guess.")
    elif guess > secret_number:
        print("My number is smaller than your guess.")
    else:
        print(f"Congratulations! You guessed the number {secret_number}!")
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print(f"It took you {tries} tries and {total_time} seconds.")
        break
