def convert_to_json(collection):
    import json
    return json.dumps(collection, indent=4)


def menu():
    # importamos las operaciones del crud que ya definimos
    from create_menu import create_menu
    from update_menu import update_menu
    from delete_menu import delete_menu
    from read_menu import read_menu
    from views_menu import views_menu
    
    while True:
        print("""---------------------------------------
Select wanted option:
1. Create a new document
2. read a document
3. Updated a document
4. Delete a document
5. complex query (views)
6. Exit
---------------------------------------""")
        option = input("option:  ")
        if (option == "1"):
            print("create_menu")
            create_menu()
        elif (option == "2"):
            read_menu()
            print("read_menu")
        elif (option == "3"):
            print("update_menu")
            update_menu()
        elif (option == "4"):
            print("delete_menu")
            delete_menu()
        elif (option == "5"):
            print("complex query (views)")
            views_menu()
            break
        elif (option == "6"):
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select a valid option.")
