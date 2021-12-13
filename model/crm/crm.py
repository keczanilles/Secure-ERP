""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


# def get_crm_data(datafile):
#     with open (datafile, "r") as files:
#         crm_data = []
#         for line in files:
#             data = {}
#             file = line.split(';')
#             for i in range(len(HEADERS)):
#                 data[HEADERS[i]] = file[i]
#             crm_data.append(data)
#         print(crm_data)
#         return crm_data


# get_crm_data(DATAFILE)