# ask 1
# The user inputs a fruit from the keyboard. Display the number of times this fruit occurs as an element.

fruits = ["apple", "strawberry", "banana", "mango"]

fruits_inp = input("Enter a fruit:")
fruit_count = fruits.count(fruits_inp)
print(fruit_count)

# Task 2
# Improve Task 1 by adding the possibility to calculate how many times this fruit occurs as a part of an element. Here, for example, "banana, apple, bananamango, mango, strawberry-banana".
# The word "banana" occurs three times.

fruits = ["banana", "apple", "bananamango", "mango", "strawberry-banana"]

fruits_input = input("Enter a fruit:")
fruit_count = sum(element.count(fruits_input) for element in fruits)
print(fruit_count)

# Task 3
# You have a tuple containing names of car manufacturers (a name may occur from 0 to N times). The user inputs a manufacturer and a replacement word. Replace all elements in the tuple with the replacement word. The match must be complete.


# Task 4
# You have a tuple of integers. Display statistics on the number of digits in tuple elements. For instance:
# One digit — 3 elements;
# Two digits — 4 elements;
# Three digits — 5 elements.
