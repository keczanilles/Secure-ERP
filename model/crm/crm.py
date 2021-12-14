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
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    pass


def list_costumers():
    data = data_manager.read_table_from_file(DATAFILE)
    crm_data = []
    for line in data:
        crm_data.append(dict(zip(HEADERS,line)))
    return crm_data
    
# def update_costumers():
#     pass

# def delete_costumers():
#     pass