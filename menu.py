import json
from db import db

# importamos las operaciones del crud que ya definimos
from crud_operations import create_record, read_document, update_record, delete_record, get_all_records, publishers_with_high_sales


def convert_to_json(collection):
    return json.dumps(collection, indent=4)


def menu():
    while True:
        print("""---------------------------------------
Select wanted option:
1. Create a new document
2. read a document
3. Updated a document
4. Delete a document
5. get all documents
6. get publishers with more than 500000TotalSales
7. get out
---------------------------------------""")
        option1 = input("option:  ")
        if (option1 == "1"):
            print("create_menu")
