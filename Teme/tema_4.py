print("Task 1")
# print("The user types in three numbers. The program prints the sum or product of these numbers based on the user's choice.")
nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
choice = (
    input(
        "Type 'sum' to calculate the sum or type 'product' to calculate the product: "
    )
    .strip()
    .lower()
)
if choice == "sum":
    print(sum(nums))
elif choice == "product":
    product = 1
    for num in nums:
        product *= num
    print(f"Product: {product}")
else:
    print("invalid choice")
print("Task 2")
# print("The user types in three numbers. Based on the user's choice, the program prints a maximum of three, a minimum of three, or arithmetic mean of three numbers.")
nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
choice = input("type 'min','max' or 'mean': ").strip().lower()
if choice == "min":
    print(f"Minimum : {min(nums)}")
elif choice == "max":
    print(f"Maximum : {max(nums)}")
elif choice == "mean":
    print(f"Aritmetic Mean: {sum(nums)/3}")
else:
    print("Invalid choice.")
print("Task 3")
# print("The user types in the number of meters. Based on the user's choice, the program converts meters to miles, inches, or yards.")
meters = float(input("Enter number of meters: "))
print("Convert to: 'miles', 'inches', or 'yards'")
choice = input("Your choice: ").strip().lower()

if choice == "miles":
    print(f"{meters} meters = {meters * 0.000621371} miles")
elif choice == "inches":
    print(f"{meters} meters = {meters * 39.3701} inches")
elif choice == "yards":
    print(f"{meters} meters = {meters * 1.09361} yards")
else:
    print("Invalid choice.")
