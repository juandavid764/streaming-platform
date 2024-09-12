import json  # Importing json for
from menu import menu
# importamos las operaciones del crud que ya definimos

def convert_to_json(collection):
    return json.dumps(collection, indent=4)


if __name__ == "__main__":
    menu()
