# Task 1

# You have a set containing country names. Provide the following features:

# Add a country;

# Delete a country;

# Search for a country by entered characters;

# Check whether the country exists inside the set.

# Initialize a set of countries
countries = {"India", "USA", "Germany", "Brazil", "Canada", "France"}


# Function to add a country
# def add_country(country):
#     countries.add(country)
#     print(f"{country} added successfully!")


# Sau:
countries.add(input("Add a country: "))
print(countries)


# Function to delete a country
# def delete_country(country):
#     if country in countries:
#         countries.remove(country)
#         print(f"{country} deleted successfully!")
#     else:
#         print(f"{country} not found in the set.")

# sau:
countries.remove(input("Mention the country: "))
print(countries)


# Function to search countries by entered characters
def search_country(keyword):
    results = [c for c in countries if keyword.lower() in c.lower()]
    if results:
        print("Search results:", results)
    else:
        print("No countries found with that keyword.")


# Function to check if a country exists
def check_country(country):
    if country in countries:
        print(f"Yes, {country} exists in the set.")
    else:
        print(f"No, {country} does not exist in the set.")


# Example usage
# add_country("Japan")
# delete_country("Brazil")
search_country("an")
check_country("India")

print("Final country set:", countries)


# Task 2

# You have two sets containing city names. Create a third set containing names present in both sets.

# Example sets
set1 = {"New York", "Paris", "Tokyo", "London"}
set2 = {"Berlin", "Paris", "London", "Rome"}

# Find cities present in both sets
common_cities = set1.intersection(set2)

print("Cities present in both sets:", common_cities)

# sau:
common = set1 & set2
print(f"My version:{common}")


# Task 3

# You have two sets containing city names. Create a third set containing names present in the first set but not in the second.
set1 = {"New York", "Paris", "Tokyo", "London"}
set2 = {"Berlin", "Paris", "London", "Rome"}

set_difference = set1.difference(set2)

print("Cities in set1 but not in set2:", set_difference)

# Task 4

# You have two sets containing city names. Create a third set containing names present in the second set but not in the first.
set1 = {"New York", "Paris", "Tokyo", "London"}
set2 = {"Berlin", "Paris", "London", "Rome"}

set_difference = set2.difference(set1)

print("Cities in set2 but not in set1:", set_difference)


# Task 5

# You have two sets containing city names. Create a third set containing names unique to each set.
set1 = {"New York", "Paris", "Tokyo", "London"}
set2 = {"Berlin", "Paris", "London", "Rome"}

unique_cities = set1.symmetric_difference(set2)

print(unique_cities)


# Task 6

# A dictionary contains a set of pairs: Country name -> Capital. Provide the possibility to add, delete, search, and replace them.
countries = {"Romania": "Bucharest", "France": "Paris", "Germany": "Berlin"}


# Add a country and its capital
def add_country(country, capital):
    if country in countries:
        return f"{country} already exists with capital {countries[country]}."
    countries[country] = capital
    return f"Added: {country} -> {capital}"


# Delete a country
def delete_country(country):
    if country in countries:
        del countries[country]
        return f"{country} has been deleted."
    return "Country not found."


# Search by country or capital (case-insensitive, partial match)
def search(term):
    term = term.lower()
    results = {
        c: cap
        for c, cap in countries.items()
        if term in c.lower() or term in cap.lower()
    }
    return results if results else "No matches found."


# Replace capital of a country
def replace_capital(country, new_capital):
    if country in countries:
        countries[country] = new_capital
        return f"Updated: {country} -> {new_capital}"
    return "Country not found."


# Show all countries and capitals
def show_all():
    return countries


print(add_country("Italy", "Rome"))
print(delete_country("France"))
print(search("ber"))
print(replace_capital("Romania", "Iasi"))
print(show_all())
