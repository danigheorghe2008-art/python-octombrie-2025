print(
    "Task 1 :The user types in three digits. Create a number containing these digits. If the typed in digits are 1,5,7, the created number should be 157."
)
a = input("Enter the first digit: ")
b = input("Enter the second digit: ")
c = input("Enter the third digit: ")


three_digit_number = int(a + b + c)
print("Created number from digits:", three_digit_number)

print(
    "Task 2 : The user types in a four-digit number. Find the product of these digits. If the typed in number is 1324, the result will be as follows: 1*3*2*4 = 24."
)
four_digit_number = input("Four digit number:  ")
product = 1
for digit in four_digit_number:
    product *= int(digit)
print("product: ", product)
