print("Task 1")
#  The user types in a number from 1 to 100. If the number is a multiple of 3 (divisible by 3 without remainder),
#  print the word Fizz. If the number is a multiple of 5, print the wordBuzz. If the word is a multiple of 3 and 5,
#  print Fizz Buzz. If the word is not a multiple of 3 and 5, print the number.
#  If the user typed in a number out of the range, print an error message.
a = int(input("Enter a number from (1-100): "))
if a < 1 or a > 100:
    print("Error: Number out of range!")
elif a % 3 == 0 and a % 5 == 0:
    print("Fizz Buzz")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("buzz")
else:
    print("number is not a multiple of 3 or 5: ", a)
print("Task 2")
# Write a program that, at the user's choice, raises the typed in number to the power of 0 through 7.
a = float(input("Enter number: "))
print("Powers from 0-7:")
for i in range(8):
    print(f"{a}^{i} = {a**i}")
print("Task 3")
#  Write a program that calculates the cost of a call for different mobile phone operators.
#  The user types in the cost of the call and chooses operators for the outgoing and incoming calls. Print the cost.
a = float(input("Enter the base cost of the call: "))
print("Choose operator for outgoing call:")
print("1. Operator A (1.0x)")
print("2. Operator B (1.2x)")
print("3. Operator C (1.5x)")
out_op = int(input("Enter your choice (1-3): "))

print("Choose operator for incoming call:")
print("1. Operator A (1.0x)")
print("2. Operator B (1.3x)")
print("3. Operator C (1.7x)")
in_op = int(input("Enter your choice (1-3): "))

out_f = {1: 1.0, 2: 1.2, 3: 1.5}
in_f = {1: 1.0, 2: 1.3, 3: 1.7}

if out_op not in out_f or in_op not in in_f:
    print("Error: Invalid operator selection.")

final_cost = a * out_f[out_op] * in_f[in_op]
print(f"The Final cost is: {final_cost:.2f}")
