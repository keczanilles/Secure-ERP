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



# def get_hr_data(datafile):
#     with open (datafile, "r") as files:
#         hr_data = []
#         for line in files:
#             data = {}
#             file = line.split(';')
#             for i in range(len(HEADERS)):
#                 data[HEADERS[i]] = file[i]
#             hr_data.append(data)
#         print(hr_data)


# get_hr_data(DATAFILE)