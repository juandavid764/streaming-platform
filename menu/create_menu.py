from db import db
from crud_operations import create_record, document_exists


def createPublisher():
    print("Ingrese los datos para un nuevo Publisher:")

    publisher_number = input("publisher_id : ")
    name = input("Publisher Name: ")
    totalsales = input("Total sales: ")
    doc_id = f"publisher_{publisher_number}"

    if document_exists(db, doc_id):
        print(
            f"El Publisher con el ID '{doc_id}' ya existe. No se puede crear un duplicado.")
        return

    # Create a new publisher.
    new_publisher = {
        "_id": doc_id,
        "type": "publisher",
        "name": name,
        # Asegurarse de que el total de ventas sea un número entero.
        "totalsales": int(totalsales)
    }

    create_record(new_publisher)
    print(f"Publisher '{name}' creado exitosamente con ID '{doc_id}'.")
