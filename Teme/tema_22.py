# Module: Exceptions
# Part 1

print("Task 1")
# Write a program that asks a user for name and age.
#  After receiving the data, the program must output a greeting in the format: "Hello, {name}! Your age is {age}".
#  Handle an exception that occurs when an invalid age is entered (age < 0 or age > 130) and output an error message.

try:
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))

    if age < 0 or age > 130:
        raise ValueError("Invalid age entered.")

    print(f"Hello, {name}! Your age is {age}")

except ValueError as e:
    print("Error:", e)

print("Task 2")
# Implement the first assignment through a function. The function must take name and age as parameters and return a formatted string.
#  The correctness check of the data received must be inside the function. Create two versions of the function implementation:
# The first version does not handle the exception inside the function. All processing is outside the function;
# The second version handles the exception inside the function.

print("version 1")


def greet(name1, age1: int):
    if age1 < 0 or age1 > 130:
        raise ValueError("Invalid age entered.")
    return f"Hello, {name1}! Your age is {age1}"


try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(greet(name, age))
except ValueError as e:
    print("Error:", e)

print("version 2")


def greet2(name1, age1):
    try:
        if age < 0 or age > 130:
            raise ValueError("Invalid age entered.")

        return f"Hello, {name}! Your age is {age}"

    except ValueError as e:
        print("Error:", e)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(greet2(name, age))

print("Task 3")
# Write a program that allows a user to enter a set of positive (numbers greater than zero) numbers from the keyboard.
#  The numbers should be accumulated in a list. After receiving all the values, the program should analyze the data.
#  If a negative value is detected, the program should generate an exception. If all values in the list are positive,
#  the program should return to the screen the sum of all the numbers in the list.
# The exception generated should be handled by the program code.

list1 = []
print("Enter positive numbers (enter 0 to stop):")
while True:
    try:
        num = int(input("Enter number: "))
        if num == 0:
            break
        if num < 0:
            raise ValueError("Negative number detected.")
        list1.append(num)

    except ValueError as e:
        print("Error:", e)
        break

if list1:
    print("Sum of positive numbers:", sum(list1))


print("Task 4")
# Implement the third task through a function.
#  The function should take a list as an argument and return the sum of the list elements.
#  The correctness check should be inside the function. Create two versions of the function implementation:
# The first version does not handle the exception inside the function. All processing is outside the function;
# The second version handles the exception inside the function.


print("version 1")


def list_sum(list2):
    for num in list2:
        if num < 0:
            raise ValueError("Negative number detected.")
    return sum(list2)


try:
    list2 = [2, 4, 34, 85, 15, 7, 2, 78, 33, 9]
    print(f"the list: {list2} and the list's sum: {list_sum(list2)}")
except ValueError as e:
    print("Error:", e)

print("version 1")


def list_sum_ex(list3):
    try:
        for num in list3:
            if num < 0:
                raise ValueError("Negative number detected.")
            return sum(list3)
    except ValueError as e:
        print("Error:", e)


list3 = [2, 4, 34, 85, 15, 7, 2, 78, 33, 9]
print(f"the list: {list3} and the list's sum: {list_sum_ex(list3)}")
