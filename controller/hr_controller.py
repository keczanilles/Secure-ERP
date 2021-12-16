from model.hr import hr
from view import terminal as view

LABELS =  ["Id", "Name", "Date of birth", "Department", "Clearance"]


def add_employee():
    table = view.get_inputs(LABELS[1:])
    hr.add_employees(table)
    print(table)
    view.print_error_message("Not implemented yet.")


def list_employees():
    data = hr.list_customers()
    data.insert(0,LABELS)
    view.print_table(data)


def update_employee():
    table = view.get_inputs([LABELS[0]])
    print(table)
    if hr.check_id(table):
        data = view.get_inputs(LABELS[1:])
        hr.update_employee(table, data)
    else:
        view.print_error_message("Not implemented yet.")



def delete_employee():
    table = view.get_inputs([LABELS[0]])
    if hr.check_id(table):
        hr.delete_employee(table)
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    print(hr.get_oldest_youngest())
    view.print_error_message("Not implemented yet.")


def get_average_age():
    today = view.get_inputs(["Enter the actual date: "])
    print(hr.get_average_age(today))
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    today = view.get_inputs(["Enter the date: "])
    print(hr.has_birthday_within_two_weeks(today))
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    number = view.get_inputs([LABELS[4]])
    print(hr.clearance(number))
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        add_employee()
    elif option == 2:
        list_employees()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "Add new employee",
               "List employees",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Please select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
