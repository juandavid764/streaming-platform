from create_menu import get_document_templates
from db import db


# Función para mostrar y actualizar un documento existente
def update_document():
    templates = get_document_templates(db)

    # show the available document types
    print("Available document types to update:")
    for i, doc_type in enumerate(templates.keys(), start=1):
        print(f"{i}. {doc_type}")

    # Ask the user to select a document type
    choice = int(input("Number of the document type you want to update: ")) - 1
    selected_type = list(templates.keys())[choice]
    fields = templates[selected_type]

    # show available documents of the selected type
    print(f"Available '{selected_type}' documents to update:")
    docs_of_selected_type = [
        doc for doc in db if doc.startswith(f"{selected_type}_")]

    if not docs_of_selected_type:
        print(f"No '{selected_type}' documents found to update.")
        return

    for i, doc_id in enumerate(docs_of_selected_type, start=1):
        print(f"{i}. {doc_id}")

    # Solicitar al usuario que seleccione un documento específico por su número
    doc_choice = int(
        input('Select the number of the document to update: ')) - 1
    selected_doc_id = docs_of_selected_type[doc_choice]

    # Get the document to update
    document = db[selected_doc_id]

    # show the document fields to update (excluding _id and _rev)
    print(
        f"Fields available for updating in '{selected_doc_id}' (excluding '_id' and '_rev'):")
    for i, field in enumerate(fields, start=1):
        if field not in ['_id', '_rev']:
            print(f"{i}. {field}")

    # Ask the user for the field to update
    field_choice = int(input('Select the number of the field to update: ')) - 1
    field_to_update = fields[field_choice]

    # Ask the user for the new value of the field
    new_value = input(f"Enter new value for '{field_to_update}': ")

    # update the document with the new value
    document[field_to_update] = int(
        new_value) if new_value.isdigit() else new_value

    # save the updated document
    db.save(document)
    print(
        f"Document '{selected_doc_id}' has been successfully updated with new value for '{field_to_update}'.")
