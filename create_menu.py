from crud_operations import create_record, document_exists, get_document_templates
from db import db


# Function to create a document of any type


def create_document():
    # Obtener las plantillas de los documentos
    templates = get_document_templates(db)

    # Mostrar al usuario los tipos de documentos disponibles
    print("Availables documents to create:")
    for i, doc_type in enumerate(templates.keys(), start=1):
        print(f"{i}. {doc_type}")

    # Solicitar al usuario que seleccione un tipo de documento
    choice = int(
        input("Number of what you want to create: ")) - 1
    selected_type = list(templates.keys())[choice]
    fields = templates[selected_type]

    # getting the values for the fields
    print(
        f"'{selected_type}' doc being created . Please enter the values below:")
    new_document = {"type": selected_type}

    for field in fields:
        # different input for _id field
        if field == "_id":
            doc_number = input("Document id (Just the number): ")
            new_document["_id"] = f"{selected_type}_{doc_number}"
        else:
            value = input(f"Enter the value for '{field}': ")
            new_document[field] = int(value) if value.isdigit() else value

    # determine if the document already exists
    if document_exists(db, new_document["_id"]):
        print(
            f"A '{selected_type}' document with ID '{new_document['_id']}' already exists. Duplicate creation is not allowed.")
        return

    # save the document in the database
    create_record(new_document)
    print(
        f"'{selected_type}' document have been successfully created with ID '{new_document['_id']}'.")
