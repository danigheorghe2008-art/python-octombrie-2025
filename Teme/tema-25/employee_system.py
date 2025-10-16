import json
import os
from employee import Employee


class EmployeeSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = []
        self.load_from_file()

    # ---manipularea fisierelor---

    def load_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    data = json.load(f)
                    self.employees = [Employee.from_dict(e) for e in data]
                except json.JSONDecodeError:
                    print("File is empty or corrupted. Starting with an empty list.")
        else:
            print("File not found. Starting with an empty list.")

    def save_to_file(self):
        with open(self.file_path, "w") as f:
            json.dump([e.to_dict() for e in self.employees], f, indent=4)
            print("Employee list saved successfully.")

    def save_results_to_file(self, results, file_name="search_results.json"):
        with open(file_name, "w") as f:
            json.dump([e.to_dict() for e in results], f, indent=4)
            print(f"Search results saved to {file_name}")

    # ---operatile de adaugare,editare,stergere---

    def add_employee(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        position = input("Enter position: ")
        self.employees.append(Employee(first_name, last_name, age, position))
        print("Employee added successfully!")

    def edit_employee(self):
        last_name = input("Enter the last name of the employee to edit: ")
        for emp in self.employees:
            if emp.last_name.lower() == last_name.lower():
                emp.first_name = (
                    input(
                        f"Enter new first name, leave empty to not change ({emp.first_name}): "
                    )
                    or emp.first_name
                )
                emp.age = int(
                    input(f"Enter new age, leave empty to not change ({emp.age}): ")
                    or emp.age
                )
                emp.position = (
                    input(
                        f"Enter new position, leave empty to not change ({emp.position}): "
                    )
                    or emp.position
                )
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self):
        last_name = input("Enter the last name of the employee to delete: ")
        for emp in self.employees:
            if emp.last_name.lower() == last_name.lower():
                self.employees.remove(emp)
                print("🗑️ Employee deleted.")
                return
        print("Employee not found.")

    # ---functi de cautare---

    def search_by_last_name(self):
        last_name = input("Enter last name to search: ")
        results = [
            e for e in self.employees if e.last_name.lower() == last_name.lower()
        ]
        self.display_results(results)
        self.ask_to_save(results)

    def filter_by_age(self):
        age = int(input("Enter age to filter: "))
        results = [e for e in self.employees if e.age == age]
        self.display_results(results)
        self.ask_to_save(results)

    def filter_by_letter(self):
        letter = input("Enter starting letter of last name: ").lower()
        results = [e for e in self.employees if e.last_name.lower().startswith(letter)]
        self.display_results(results)
        self.ask_to_save(results)

    def display_results(self, results):
        if not results:
            print("No matching employees found.")
        else:
            print("\n--- Matching Employees ---")
            for emp in results:
                print(emp)

    def ask_to_save(self, results):
        if results and input("Save results to file? (yes/no): ").lower() == "yes":
            self.save_results_to_file(results)

    def show_all(self):
        if not self.employees:
            print("No employees in the system.")
        else:
            print("\n--- All Employees ---")
            for emp in self.employees:
                print(emp)
