import json


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



def readCollection():
    
    print("""Select collection:
    1. Publisher
    2. User
    3. Videogame
    4. Review""")
    optionSelected = input("Option: ")
    
    if optionSelected == "1":
        collectionName = "publisher"
        numbreId = input("Id: ")
        idCollection = collectionName+numbreId

        
        read_document(collectionName, idCollection)

    elif optionSelected == "2":
        collectionName = "user"
        numbreId = input("Id: ")
        idCollection = collectionName+numbreId

    elif optionSelected == "3":
        collectionName = "videogame"
        numbreId = input("Id: ")
        idCollection = collectionName+numbreId
    elif optionSelected == "4":
        collectionName = "review"
        numbreId = input("Id: ")
        idCollection = collectionName+numbreId
    else:
        print("Invalid option. Please try again.")
    
    return idCollection