# Task 1
# The user types in a string. Rotate the strings and display the result.
# User types in a string
text = input("Enter a string: ")

# Rotate: move last character to the front
rotated = text[::-1]

print("Rotated string:", rotated)

# Task 2

# Ask user for input
text = input("Enter a string containing letters and digits: ")

# Initialize counters
letter_count = 0
digit_count = 0

# Loop through each character in the string
for char in text:
    if char.isalpha():       # Check if it's a letter
        letter_count += 1
    elif char.isdigit():     # Check if it's a digit
        digit_count += 1

# Display results
print("Number of letters:", letter_count)
print("Number of digits:", digit_count)

#Task 3

# Ask user for a string
text = input("Enter a string containing letters and symbols: ")

# Ask user for the symbol to search for
symbol = input("Enter the symbol to search for: ")

# Count how many times the symbol appears
count = 0
for char in text:
    if char == symbol:
        count += 1

# Display result
print(f"The symbol '{symbol}' appears {count} times in the string.")

#Task 4
# User enters the string
text = input("Enter a string: ")

# User enters the search word
word = input("Enter the word to search: ")

# Count how many times the word appears in the string
count = text.count(word)

# Display the result
print(f"The word '{word}' appears {count} times in the string.")

#Task 5
# Get user input
text = input("Enter a string: ")
search_word = input("Enter the word to search for: ")
replacement_word = input("Enter the replacement word: ")

# Replace the word
result = text.replace(search_word, replacement_word, 1)  # The '1' replaces only the first occurrence

# Print result
print("Resulting string:", result)

