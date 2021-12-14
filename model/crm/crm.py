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
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')
    
    print(temp_list)


def list_costumers():
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

def update_costumers(table, data):
    list = list_costumers()
    temp_list = []
    for dicts in list:
        for key, value in dicts.items():
            if key == 'id' and value == table:
                dicts = zip(HEADERS, (table,data))
                temp_list.append(dicts)
                # dicts[value] = data_manager.write_table_to_file(DATAFILE, data, separator=';')
    print(temp_list)

# update_costumers('_6jmMi4H+b', '1,2,3')

    
    # def get_least_bought_meal(data_set):
    # meal = sorted(data_set, key=lambda v: v["quantity"]) 
    # least_bought = meal[0]["meal"]
    # return least_bought
    
    

# def delete_costumers():
#     pass
# print(list_costumers())