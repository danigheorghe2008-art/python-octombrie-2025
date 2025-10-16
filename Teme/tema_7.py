print("Task 1")
#  The user types in two numbers (start and end points of the range).
#  Analyze all the numbers in this range as follows: if the , print it.
start = int(input("Enter the number to start with: "))
end = int(input("Enter the number to end with: "))

print("number is a multiple of 7: ")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num)

print("Task 2")
#  The user types in two numbers (start and end points of the range). Analyze all the numbers in this range. Print the following:
# 1. All numbers in the range;
# 2. All numbers in the range in descending order;
# 3. All numbers that are multiples of 7;
# 4. How many numbers are multiples of 5.

# 1
start = int(input("Enter the number to start with: "))
end = int(input("Enter the number to end with: "))

print("numbers in range: ")
for num in range(start, end + 1):
    print(num, end=" ")
print()
# 2
print("numbers in range in descending order: ")
for num in range(end, start - 1, -1):
    print(num, end=" ")
print()
# 3
print("Multiples of 7 in the range:")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num, end=" ")

# 4
print("How many numbers in range are a multiple of 5: ")
count = 0
for num in range(start, end + 1):
    if num % 5 == 0:
        count += 1

print(f"Count of multiples of 5: {count}")
