""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from os import sep
from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def add_customers(table):
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




def list_customers():
    data = data_manager.read_table_from_file(DATAFILE)
    crm_data = []
    for line in data:
        crm_data.append(dict(zip(HEADERS,line)))
    return crm_data

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

def update_customers(table, data):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    for dicts in list:
        if dicts[0] == table:
            dicts[1] = data[0]
            dicts[2] = data[1]
            dicts[3] = data[2]
    data_manager.write_table_to_file(DATAFILE, list, separator=';')
                
    # def get_least_bought_meal(data_set):
    # meal = sorted(data_set, key=lambda v: v["quantity"])
    # least_bought = meal[0]["meal"]
    # return least_bought


def delete_customers(table):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    temp_list = []
    for dicts in list:
        if dicts[0] != table:
            temp_list.append(dicts)
        else:
            continue
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')


def subscribed_emails():
    data = data_manager.read_table_from_file(DATAFILE, separator=';')
    subscribed = []
    for i in data:
        if i[3] == '1':
            subscribed.append(i[2])
    return subscribed
