import json
from crud_operations import read_record


def readOption():
    print("Read menu:")
    print("1. Review")
    print("2. Publisher")
    print("3. Videogame")
    print("4. User")

    selected_option = int(input("Select the collection to consult: "))

    if selected_option == 1:
        collection = "publisher_"
        idToRead = input("Type the id to consult: ")
        doument = read_record(collection+idToRead)
        print(json.dumps(doument, indent=4))
    elif selected_option == 2:
        collection = "review_"
        idToRead = input("Type the id to consult: ")
        doument = read_record(collection+idToRead)
        print(json.dumps(doument, indent=4))
    elif selected_option == 3:
        collection = "videogame_"
        idToRead = input("Type the id to consult: ")
        doument = read_record(collection+idToRead)
        print(json.dumps(doument, indent=4))
    elif selected_option == 4:
        collection = "user_"
        idToRead = input("Type the id to consult: ")
        doument = read_record(collection+idToRead)
        print(json.dumps(doument, indent=4))
    else:
        print("Invalid option selected.")