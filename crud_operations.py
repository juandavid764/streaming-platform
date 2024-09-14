def get_document_templates(db):
    templates = {}
    for doc_id in db:
        if 'template_' in doc_id:  # Check if the document is a template"
            template = db[doc_id]
            templates[template['type']] = template['fields']
    return templates


def document_exists(db, doc_id):
    return doc_id in db


def create_record(record):
    from db import db
    from couchdb.http import ResourceConflict
    try:
        db.save(record)
        print("Successful insertion")
    except ResourceConflict:
        print("document already exist")


def read_record(id):
    from db import db
    document = db.get(id)
    return document


def update_record(id, new_record):
    from db import db
    from couchdb.http import ResourceConflict
    document = read_record(id)
    if document:
        try:
            for key, value in new_record.items():
                document[key] = value
            db.save(document)
            print("Document have been updated")
        except ResourceConflict:
            print("An error occurred")
    else:
        print("Document haven't found")


def delete_record(id):
    from db import db
    document = read_record(id)
    if document:
        db.delete(document)
        print("Successful elimination")
    else:
        print("Document haven't found")


def consultar_view(tipo, llave, valor):
    import couchdb
    from db import db
    import time

    # Utilizar la vista correspondiente según el tipo de documento
    design_doc = f"_design/{tipo}"
    view_name = f"by_{llave}"

    # Verificar si el diseño y la vista existen
    try:
        db[design_doc]
    except couchdb.ResourceNotFound:
        print(f"El diseño '{design_doc}' y la vista '{view_name}' no existen.")
        time.sleep(1)
        return ""

    # Utilizar la vista para buscar el documento por la llave
    try:
        resultados = db.view(f"{tipo}/{view_name}", key=valor)
        # Retornar los documentos encontrados
        return [row.value for row in resultados]
    except couchdb.ResourceNotFound:
        print(f"No se encontraron documentos para la llave '{llave}' y el valor '{valor}'.")
        time.sleep(1)
        return ""
    
def consultar_viewv2(tipo, llave):
    import couchdb
    from db import db
    import time

    # Utilizar la vista correspondiente según el tipo de documento
    design_doc = f"_design/{tipo}"
    view_name = f"by_{llave}"

    # Verificar si el diseño y la vista existen
    try:
        db[design_doc]
    except couchdb.ResourceNotFound:
        print(f"El diseño '{design_doc}' y la vista '{view_name}' no existen.")
        time.sleep(1)
        return ""

    # Utilizar la vista para buscar el documento por la llave
    try:
        resultados = db.view(f"{tipo}/{view_name}")
        # Retornar los documentos encontrados
        return [row.value for row in resultados]
    except couchdb.ResourceNotFound:
        print(f"No se encontraron documentos para la llave '{llave}'")
        time.sleep(1)
        return ""