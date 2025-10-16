# print("to be or\n not \nto be")

# print(" " "Life is what happens when you're busy making other plans" " ")
nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
choice = (
    input("Type 'sum' to calculate the sum or 'product' to calculate the product: ")
    .strip()
    .lower()
)
if choice == "sum":
    result = sum(nums)
    print(f"Sum: {result}")
elif choice == "product":
    product = 1
    for num in nums:
        product *= num
    print(f"Product: {product}")
else:
    print("Invalid choice.")
