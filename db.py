import couchdb

# Archivo para realizar la conexion a la bd
couch = couchdb.Server('http://sebastian:1234@localhost:5984/')


db_name = 'streaming-platform'
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

print(f"Conectado a la base de datos: {db_name}")
