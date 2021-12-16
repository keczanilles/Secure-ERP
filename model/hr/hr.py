""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def add_employees(table):
    table = table
    table.insert(0, util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"))
    temp_list = data_manager.read_table_from_file(DATAFILE, separator=';')
    temp_list.append(table)
    print(temp_list)
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')


def list_employees():
    data = data_manager.read_table_from_file(DATAFILE)
    hr_data = []
    for line in data:
        hr_data.append(dict(zip(HEADERS,line)))
    return hr_data

def check_id(table):
    table = ''.join(table)
    data = data_manager.read_table_from_file(DATAFILE)
    id = []
    for line in data:
        id.append(line[0])
    if table in id:
        return True
    else:
        return False

def update_employee(table, data):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    for dicts in list:
        if dicts[0] == table:
            dicts[1] = data[0]
            dicts[2] = data[1]
            dicts[3] = data[2]
            dicts[4] = data[3]
    data_manager.write_table_to_file(DATAFILE, list, separator=';')

def delete_employee(table):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    temp_list = []
    for dicts in list:
        if dicts[0] != table:
            temp_list.append(dicts)
        else:
            continue
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')


def get_oldest_youngest():
    pass


def get_average_age():
    pass

def has_birthday_within_two_weeks():
    pass


def clearance(number):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    number = "".join(number)
    counter = 0
    for i in list:
        if int(i[4]) >= int(number):
            counter += 1
    return counter

#  SALES = 3 PRODUCTION = 4 HR = 2 
def count_employees_per_department():
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    departments = []
    numbers = []
    for i in list:
        departments.append(i[3])
    for i in sorted(set(departments)):
        x = departments.count(i)
        numbers.append(x)
    keys = sorted(set(departments))
    dicts = dict(zip(keys, numbers))
    return dicts
