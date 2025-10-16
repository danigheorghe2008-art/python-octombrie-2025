print("------Task 1------")
# Print all prime numbers in the user-specified range. A number is prime if it is divisible only by itself and by one.
#  For instance, 3 is a prime number, but 4 is not.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


start = int(input("Enter a numbert to start with: "))
end = int(input("Enter a numbert to end with: "))
if start >= end:
    start, end = end, start
print(f"All prime numbers between {start} and {end}: ")
for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=" ")
print("\n")


print("------Task 2------")
# Print the multiplication table for all numbers from 1 to 10. For example:
# 1*1 = 1 1*2 = 2 ….. 1*10 = 10
# ..................................
# 10*1 = 10 10*2 = 20 …. 10*10 = 100

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}*{j} = {i*j} ", end="\t")
    print()
print()


print("------Task 3------")
# Print the multiplication table in the user-specified range.
#  If the user specified 3 and 5, the multiplication table might look like this:
# 3*1 = 3 3*2 = 6 3*3 = 9 … 3*10 = 30
# .....................................
# 5*1 = 5 5*2 = 10 5*3 = 15 … 5*10 = 50
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    a, b = b, a
for i in range(a, b):
    for j in range(a, b + 1):
        print(f"{i}*{j} = {i*j} ", end="\t")
    print()
