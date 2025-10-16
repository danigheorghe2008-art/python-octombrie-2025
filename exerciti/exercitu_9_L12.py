# Task 1
# The user types in a string. Rotate the strings and display the result.

mystring = input("Enter the string: ")
print(mystring[::-1])

# Task 2
# The user types in a string. Count the number of letters and digits in the string. Print both results.
a = str(input("Enter string: "))
l = sum(c.isalpha() for c in a)
d = sum(c.isdigit() for c in a)
print("Letters:", l)
print("Digits:", d)


# Task 3
# The user types in a string and a symbol to be searched for. Count how many times this symbol appears in the string. Print the result.


# Task 4
# The user types in a string and a search word. Count how many times this word appears in the string. Print the result.


# Task 5
# The user types in a string, a search word, and a replacement word. Replace one word with another one in the string. Print the resulting string.
