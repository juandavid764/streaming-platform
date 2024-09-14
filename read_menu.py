def read_menu():
    import json
    from crud_operations import get_document_templates, read_record

    from db import db
    templates = get_document_templates(db)

    # show the available document types
    print("Available document types to read:")
    for i, doc_type in enumerate(templates.keys(), start=1):
        print(f"{i}. {doc_type}")


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