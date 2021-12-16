from model.sales import sales
from view import terminal as view

BETWEEN = ["Start", "End"]
LABELS = ["Id", "Customer", "Product", "Price", "Date"]


def add_transaction():
    table = view.get_inputs(LABELS[LABELS.index('Customer'):])
    sales.add_transactions(table)
    print(table)
    view.print_error_message("Not implemented yet.")

def list_transactions():
    data = sales.list_transactions()
    data.insert(0,LABELS)
    print(data)
    view.print_error_message("Not implemented yet.")

def update_transaction():
    table = view.get_inputs([LABELS[0]])
    if sales.check_id(table):
        data = view.get_inputs(LABELS[1:])
        sales.update_transaction(table,data)
    else:
        view.print_error_message("Not implemented yet.")


def delete_transaction():
    table = view.get_inputs([LABELS[0]])
    if sales.check_id(table):
        sales.delete_transaction(table)
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    print(sales.get_biggest_revenue_transaction())
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    print(sales.get_biggest_revenue_product())
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    start, end = view.get_inputs(BETWEEN[0:])
    start = sales.convert_date(start)
    end = sales.convert_date(end)
    result =sales.number_of_transactions_between(start,end)
    print(result)
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    start, end = view.get_inputs(BETWEEN[0:])
    start = sales.convert_date(start)
    end = sales.convert_date(end)
    result = sales.sum_of_transactions_between(start, end)
    print(result)
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        add_transaction()
    elif option == 2:
        list_transactions()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "Add new transaction",
               "List transactions",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            print('\n')
            operation = view.get_input("Please select an operation: ")
            print('\n')
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
