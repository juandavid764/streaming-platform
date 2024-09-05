import json  # Importing json for


# importamos las operaciones del crud que ya definimos
from crud_operations import create_record, read_record, update_record, delete_record, get_all_records, publishers_with_high_sales


def convert_to_json(collection):
    return json.dumps(collection, indent=4)


if __name__ == "__main__":
    print("Samuel is gay")
