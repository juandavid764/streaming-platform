import couchdb
# Archivo para realizar la conexion a la bd
user = "juan"
password = "1234"
couch = couchdb.Server(f'http://{user}:{password}@localhost:5984/')

db_name = 'streaming-platform'

if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)
    from inserts import insert_data
    insert_data()

