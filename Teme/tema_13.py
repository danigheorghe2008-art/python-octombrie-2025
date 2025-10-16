print("\nTask 1")
# The user types in an arithmetic expression. For example, 23+12.
#  Print its result. In our example, the output is 35.
#  The arithmetic expression can have only three parts: number, operation, number. Possible operations: +, -, *, /.
# folosind eval:

# a = input("Enter an arithmetic expression (exemple: 23+12): ")

# result = eval(a)
# print("Result:", result)

# deoarece eval e destul de periculos de folosit o poti face manual asa:

# a = input("Enter an arithmetic expression (exemple: 23+12): ")

# for b in "+-*/":
#     if b in a:
#         num1, num2 = a.split(b)
#         num1, num2 = int(num1), int(num2)

#         if b == "+":
#             result = num1 + num2
#         elif b == "-":
#             result = num1 - num2
#         elif b == "*":
#             result = num1 * num2
#         elif b == "/":
#             result = num1 / num2

#         print("Result:", result)
#         break

print("/nTask 2")
# You have a list of integers filled with random numbers.
#  Find the largest and the smallest elements, count negative and positive elements, as well as zeros. Print the results.

import random

num = [random.randint(-50, 50) for i in range(15)]
print("Numbers:", num)

largest = max(num)
smallest = min(num)
negative = sum(1 for n in num if n > 0)
positive = sum(1 for n in num if n < 0)
zero = sum(1 for n in num if n == 0)

print(f"The largest number: {largest}")
print(f"The smallest number: {smallest}")
print(f"How many negeatve numbers: {negative}")
print(f"How many positive numbers: {positive}")
print(f"How many zeroes: {zero}")
