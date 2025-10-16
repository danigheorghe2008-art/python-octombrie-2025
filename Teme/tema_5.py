print("Task 1")
# The user types in a number from 1 to 7 that represents a day of the week.
#  Print its name. For example, if the number is 1, then you should display "Monday"; if 2, display "Tuesday," etc.
nums = int(input("Enter a number from (1-7) for a day of the week: "))
if nums in [1]:
    print("Monday")
elif nums in [2]:
    print("Tuesday")
elif nums in [3]:
    print("Wednesday")
elif nums in [4]:
    print("Thursday")
elif nums in [5]:
    print("Friday")
elif nums in [6]:
    print("Saturday")
elif nums in [7]:
    print("Sunday")
print("Task 2")
# The user types in a number from 1 to 12 that represents a month. Print its name.
#  For example, if the number is 1, display "January"; if 2, display "February," etc.
m_nums = int(input("Enter a number (1-12) for the month: "))
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
if 1 <= m_nums <= 12:
    print("Month:", months[m_nums - 1])
else:
    print("Invalid Number")
print("Task 3")
# The user types in a number. If the number is greater than 0, print "Your number is positive";
#  if it is less than zero, print "Your number is negative"; if it is equal to 0, print "Your number is equal to zero."
a = int(input("Enter number: "))
if a > 0:
    print("Your number is positive")
elif a < 0:
    print("Your number is negative")
else:
    a == 0
    print("Your number is equal to zero.")
print("Task 4")
# The user types in two numbers. Determine if these numbers are equal. If they are not, print them in ascending order.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if a == b:
    print("The number are equal")
else:
    print("Numbers in ascending order:", sorted([a, b]))
