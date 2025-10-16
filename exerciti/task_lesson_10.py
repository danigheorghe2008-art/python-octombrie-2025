# Task1
# The user types in the size of the square's sides. Print a solid square. The size is equal to the typed in square's side. Say the user typed in 3, the output will be as follows:
# ***
# ***
# ***
side = int(input("Enter the size of the square's sides: "))
for i in range(side):
    print("*" * side)

# # Task 2
# # The user types in the width and height of a rectangle. Print a solid rectangle of the specified height and width. Say the user typed in the height equal to 3, and width 5, the output should be as follows:
# # *****
# # *****
# # *****
# # Utilizatorul introduce dimensiunile
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

# Afișăm dreptunghiul
for _ in range(height):
    print("*" * width)

# # Task 3
# # The user types in the size of the square's sides. Print an empty square (only its sides are displayed). The side is equal to the typed in size.
size = int(input("Enter the size of the square: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")

# Task 4
# The user types in the length and width of a rectangle.
# Print an empty rectangle (only its sides are displayed). The length and width are equal to the typed in numbers.
# Get user input
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

# Print the rectangle
for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)  # Top and bottom borders
    else:
        print("*" + " " * (width - 2) + "*")  # Middle rows with spaces
