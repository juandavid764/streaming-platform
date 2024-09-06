
from crud_operations import delete_record


def readOption():
    print("Delete menu:")
    print("1. Review")
    print("2. Publisher")
    print("3. Videogame")
    print("4. User")

    selected_option = int(input("Select the collection to delete: "))

    if selected_option == 1:
        collection = "publisher_"
        idToDelete = input("Type the id to delete: ")
        delete_record(collection+idToDelete)
    elif selected_option == 2:
        collection = "review_"
        idToDelete = input("Type the id to delete: ")
        delete_record(collection+idToDelete)
    elif selected_option == 3:
        collection = "videogame_"
        idToDelete = input("Type the id to delete: ")
        delete_record(collection+idToDelete)
    elif selected_option == 4:
        collection = "user_"
        idToDelete = input("Type the id to delete: ")
        delete_record(collection+idToDelete)
    else:
        print("Invalid option selected.")