print("------Task 1------")
#  The user types in two numbers. Find the sum of all even, odd numbers and multiples of 9 in the specified range,
#  as well as arithmetic mean of each group.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    a, b = b, a

sum_even = 0
count_even = 0

sum_odd = 0
count_odd = 0

sum_mult9 = 0
count_mult9 = 0

for num in range(a, b + 1):
    if num % 2 == 0:
        sum_even += num
        count_even += 1
    if num % 2 != 0:
        sum_odd += num
        count_odd += 1
    if num % 9 == 0:
        sum_mult9 += num
        count_mult9 += 1

mean_even = sum_even / count_even if count_even != 0 else None
mean_odd = sum_odd / count_odd if count_odd != 0 else None
mean_mult9 = sum_mult9 / count_mult9 if count_mult9 != 0 else None

print("Even numbers: sum =", sum_even, end="")
if mean_even is not None:
    print(", Arithmetic mean =", mean_even)
else:
    print(" (No even numbers found in range)")

print("Odd numbers: Sum =", sum_odd, end="")
if mean_odd is not None:
    print(", Arithmetic mean =", mean_odd)
else:
    print(" (No odd numbers found in range)")

print("Multiples of 9: Sum =", sum_mult9, end="")
if mean_mult9 is not None:
    print(", Arithmetic mean =", mean_mult9)
else:
    print(" (No multiples of 9 found in range)")


print("------Task 2------")
#  The user types in the length of a line and a symbol to fill the line.
#  Print a vertical line made out of the typed in symbol of the specified length.
#  For instance, if the typed in number and symbol are 5 and %, the output will be as follows:
#  %
#  %
#  %
#  %
#  %

a = str(input("Enter a symbol: "))
b = int(input("Enter how many times to print the symbol: "))
for _ in range(b):
    print(a)

print("------Task 3------")
#  The user types in numbers. If the number is greater than 0, print "Your number is positive";
#  if it is less than zero, print "Your number is negative"; if it is equal to 0, print "Your number is equal to zero."
#  When the user types in 7, the program stops and prints "Good bye!"

while True:
    a = float(input("Enter a number: "))
    if a == 7:
        print("Good bye!")
        break
    if a > 0:
        print("Your number is positive")
    elif a < 0:
        print("Your number is negative")
    else:
        print("Your number is equal to zero.")
    break
