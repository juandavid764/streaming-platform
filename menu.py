import json

# importamos las operaciones del crud que ya definimos
from create_menu import create_document
from delete_menu import deleteOption
from update_menu import update_document


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
5. Exit
---------------------------------------""")
        option1 = input("option:  ")
        if (option1 == "1"):
            print("create_menu")
            create_document()
        elif (option1 == "2"):
            print("read_menu")
        elif (option1 == "3"):
            print("update_menu")
            update_document()
        elif (option1 == "4"):
            print("delete_menu")
            deleteOption()
        elif (option1 == "5"):
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select a valid option.")
