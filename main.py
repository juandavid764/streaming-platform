

def convert_to_json(collection):
    import json  # Importing json for
    return json.dumps(collection, indent=4)


if __name__ == "__main__":
    from menu import menu
    menu()
