from model.sales import sales
from view import terminal as view

BETWEEN = ["Start", "End"]
LABELS = ["Id", "Customer", "Product", "Price", "Date"]


def add_transaction():
    table = view.get_inputs(LABELS[LABELS.index('Product'):])
    sales.add_transactions(table)

    

def list_transactions():
    data = sales.list_transactions()
    data.insert(0,LABELS)
    view.print_table(data)
    

def update_transaction():
    table = view.get_inputs([LABELS[0]])
    if sales.check_id(table):
        data = view.get_inputs(LABELS[2:])
        sales.update_transaction(table,data)
    else:
        view.print_message("The ID doesn't exist.")


def delete_transaction():
    table = view.get_inputs([LABELS[0]])
    if sales.check_id(table):
        sales.delete_transaction(table)
    else:
        view.print_message("The ID doesn't exist.")


def get_biggest_revenue_transaction():
    data = sales.get_biggest_revenue_transaction()
    view.print_general_results(data, 'Biggest revenue transaction(s)')


def get_biggest_revenue_product():
    data = sales.get_biggest_revenue_product()
    view.print_general_results([data], 'Biggest revenue product')
    


def count_transactions_between():
    start, end = view.get_inputs(BETWEEN[0:])
    start1 = sales.convert_date(start)
    end1 = sales.convert_date(end)
    result =sales.number_of_transactions_between(start1,end1)
    view.print_general_results([result], f'Transactions between {start} and {end}')
    


def sum_transactions_between():
    start, end = view.get_inputs(BETWEEN[0:])
    start1 = sales.convert_date(start)
    end1 = sales.convert_date(end)
    result = sales.sum_of_transactions_between(start1, end1)
    view.print_general_results([result], f'Sum of transactions between {start} and {end}')
    


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
