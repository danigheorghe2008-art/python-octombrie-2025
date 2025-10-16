# Task 1 :The user types in a number.
# Check if it is even or odd. If the number is even,
# print the number and the text "Even number." If the number is odd, print the number and the text "Odd number."

number = int(input("Enter a number:"))
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

# task2 :# The user types in a number.
# Check if it is a multiple of 7.
# If it is, print the number and the text "Your number is a multiple of 7." If it is not, print the number and the text
# "Your number is not a multiple of 7."

number = int(input("enter the number:"))
if number % 7 == 0:
    print("Your number is a multiple of 7.")
else:
    print("Your number is not a multiple of 7")
# task 3:
# The user types in two numbers. Find the maximum of two numbers and print it.

num1 = float(input("enter number 1:"))
num2 = float(input("enter number 2:"))
maximum = max(num1, num2)
print("the maximum mumber is:", maximum)
