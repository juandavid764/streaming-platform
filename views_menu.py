


def views_menu():
    from crud_operations import consultar_viewv2
    from crud_operations import get_document_templates
    from db import db
    import json

    # Obtener las plantillas de los documentos
    templates = get_document_templates(db)

    # Mostrar al usuario los tipos de documentos disponibles
    print("Availables documents to read with view:")
    for i, doc_type in enumerate(templates.keys(), start=1):
        print(f"{i}. {doc_type}")

    selected_option = int(input("Select the collection to consult: "))

    if selected_option == 1:
        print("consult publishers with sales over 1000")
        tipo = "publishers"
        llave = "totalsales"
        resultados = consultar_viewv2(tipo, llave)
        if resultados:
            for resultado in resultados:
                print(json.dumps(resultado, indent=4))
    elif selected_option == 2:
        print("consult reviews with rating over 3")
        tipo = "reviews"
        llave = "rating"
        resultados = consultar_viewv2(tipo, llave)
        if resultados:
            for resultado in resultados:
                print(json.dumps(resultado, indent=4))
      
    elif selected_option == 3:
        print("consult users from colombia")
        tipo = "users"
        llave = "country"
        resultados = consultar_viewv2(tipo, llave)
        if resultados:
            for resultado in resultados:
                print(json.dumps(resultado, indent=4))

    elif selected_option == 4:
        print("consult videogames with adventure genre")
        tipo = "videogames"
        llave = "genre"
        resultados = consultar_viewv2(tipo, llave)
        if resultados:
            for resultado in resultados:
                print(json.dumps(resultado, indent=4))

    else:
        print("Invalid option selected.")