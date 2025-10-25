# Task 1
# Implement a class Human. Class fields should store the following: full name, date of birth, contact number,
#  city, country, home address. Implement class methods for data input and output,
#  provide access to individual fields through class methods.


class Human:
    def __init__(
        self,
        full_name="",
        date_of_birth="",
        contact_number="",
        city="",
        country="",
        home_address="",
    ):
        self.__full_name = full_name
        self.__date_of_birth = date_of_birth
        self.__contact_number = contact_number
        self.__city = city
        self.__country = country
        self.__home_address = home_address

    def human_input(self):
        print("Please imput your data:")
        self.__full_name = input("Enter full name: ")
        self.__date_of_birth = input("Enter date of birth: ")
        self.__contact_number = input("Enter contact number: ")
        self.__city = input("Enter city: ")
        self.__country = input("Enter country: ")
        self.__home_address = input("Enter home address: ")

    def display_data(self):
        print(f"Full Name: {self.__full_name}")
        print(f"Date of Birth: {self.__date_of_birth}")
        print(f"Contact Number: {self.__contact_number}")
        print(f"City: {self.__city}")
        print(f"Country: {self.__country}")
        print(f"Home Address: {self.__home_address}")

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, name):
        self.__full_name = name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date):
        self.__date_of_birth = date

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, number):
        self.__contact_number = number

    def get_city(self):
        return self.__city

    def set_city(self, city_name):
        self.__city = city_name

    def get_country(self):
        return self.__country

    def set_country(self, country_name):
        self.__country = country_name

    def get_home_address(self):
        return self.__home_address

    def set_home_address(self, address):
        self.__home_address = address


if __name__ == "__main__":
    person = Human()
    person.human_input()
    print("\n--- Entered Data ---")
    person.display_data()

# Task 2
# Create a class City. Class fields should store the following: city name, region name,
#  country name, number of citizens, zip code, area code.
#  Implement class methods for data input and output, provide access to individual fields through class methods.

# class City:
#     def __init__(self, city_name="", region_name="", country_name="", citizens=0, zip_code="", area_code=""):
#         self.__city_name = city_name
#         self.__region_name = region_name
#         self.__country_name = country_name
#         self.__citizens = citizens
#         self.__zip_code = zip_code
#         self.__area_code = area_code

#     def input_city_data(self):
#         self.__city_name = input("Enter city name: ")
#         self.__region_name = input("Enter region name: ")
#         self.__country_name = input("Enter country name: ")

# Task 3
# Create a class Country. Class fields should store the following: country name, continent,
#  population, calling code, capital, city names.
#  Implement class methods for data input and output, provide access to individual fields through class methods.


# Task 4
# Create a class Fraction. Class fields should store the following: numerator and denominator .
#  Implement class methods for data input and output, provide access to individual fields through class methods.
#  Also, create class methods for arithmetic operations (add, subtract, multiply, divide, etc.).
