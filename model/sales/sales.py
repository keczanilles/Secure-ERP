""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]



def list_costumers():
    data = data_manager.read_table_from_file(DATAFILE)
    sales_data = []
    for line in data:
        sales_data.append(dict(zip(HEADERS,line)))
    return sales_data