import requests
import json
from db import db
from couchdb.http import ResourceConflict

db_url = f"http://juan:1234@localhost:5984/streaming-platform"


def create_record(record):
    try:
        db.save(record)
        print("Insercion exitosa")
    except ResourceConflict:
        print("document already exist")


def read_record(id):
    document = db.get(id)
    return document


def update_record(id, new_record):
    document = read_record(id)
    if document:
        try:
            for key, value in new_record.items():
                document[key] = value
            db.save(document)
            print("Document have been updated")
        except ResourceConflict:
            print("An error occurred")
    else:
        print("Document haven't found")


def delete_record(id):
    document = read_record(id)
    if document:
        db.delete(document)
    else:
        print("Document haven't found")


def get_all_records(type=None):
    query = {
        "selector": {}
    }
    if type:
        query["selector"]["type"] = type

    try:
        response = requests.post(
            f'{db_url}/_find',
            headers={"Content-Type": "application/json"},
            data=json.dumps(query)
        )
        if response.status_code == 200:

            results = response.json().get('docs', [])
            return results
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []


# queries
# Getting publishers with more than 500000TotalSales
def publishers_with_high_sales():
    query = {
        "selector": {
            "type": "publisher",
            "totalsales": {"$gt": 500000}  # "Greather than" operator
        }
    }

    response = requests.post(
        f'{db_url}/_find', headers={"Content-Type": "application/json"}, data=json.dumps(query))
    results = response.json().get('docs', [])
    return results

def useQuerys():
    print("Available functions:")
    print("1. create_record")
    print("2. read_record")
    print("3. update_record")
    print("4. delete_record")
    print("5. get_all_records")
    print("6. publishers_with_high_sales")

    choice = input("Enter the number of the function you want to use: ")

    if choice == "1":
        record = {}
        record = json.loads(input("Enter the JSON string to insert: "))
        create_record(record)

    elif choice == "2":
        id = input("Enter the ID of the record: ")
        result = read_record(id)
        print(result)

    elif choice == "3":
        id = input("Enter the ID of the record: ")
        new_record = {}
        new_record = json.loads(input("Enter the JSON string to update: "))
        update_record(id, new_record)

    elif choice == "4":
        id = input("Enter the ID of the record: ")
        delete_record(id)

    elif choice == "5":
        type = input("Enter the type of records to retrieve (optional): ")
        results = get_all_records(type)
        print(results)

    elif choice == "6":
        results = publishers_with_high_sales()
        print(results)

    else:
        print("Invalid choice")


