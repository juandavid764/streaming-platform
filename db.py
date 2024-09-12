import couchdb
from inserts import insert_data 


# Archivo para realizar la conexion a la bd
#couch = couchdb.Server('http://juan:1234@localhost:5984/')
# couch = couchdb.Server('http://sebastian:1234@localhost:5984/')

user = input("Enter your CouchDb username: ")
password = input("Enter your CouchDb password: ")
couch = couchdb.Server(f'http://{user}:{password}@localhost:5984/')


db_name = 'streaming-platform'
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)
    insert_data()

print(f"Conectado a la base de datos: {db_name}")
