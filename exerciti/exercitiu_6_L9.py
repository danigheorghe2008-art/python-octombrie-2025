print("Task 1")
# Print the multiplication table for the user-defined number. If the user typed in 7, the output should be as follows:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# …


def multiplication_table():
    a = int(input("Enter a number to print its multiplication table: "))
    for i in range(1, 11):
        print(f"{a} * {i} = {a * i}")


multiplication_table()

print("Task 2")
# Write a currency converter program. Implement a dialog with the user through a menu.


def currency_converter():
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
    }


while True:
    print("Currency Converter Menu:")
    print("1. Convert currency")
    print("2. Show rates")
    print("3. Exit")

    c = int(input("Choose an option: "))
