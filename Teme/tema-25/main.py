from employee_system import EmployeeSystem


def main():
    file_path = input("Enter the employee data file name (exemple: employees.json): ")
    system = EmployeeSystem(file_path)

    while True:
        print("\n===== EMPLOYEE SYSTEM MENU =====")
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Delete Employee")
        print("4. Search by Last Name")
        print("5. Filter by Age")
        print("6. Filter by Last Name Starting Letter")
        print("7. Show All Employees")
        print("8. Save All Employees")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            system.add_employee()

        elif choice == "2":
            system.edit_employee()

        elif choice == "3":
            system.delete_employee()

        elif choice == "4":
            system.search_by_last_name()

        elif choice == "5":
            system.filter_by_age()

        elif choice == "6":
            system.filter_by_letter()

        elif choice == "7":
            system.show_all()

        elif choice == "8":
            system.save_to_file()

        elif choice == "9":
            system.save_to_file()
            print("Exiting. Data saved.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
