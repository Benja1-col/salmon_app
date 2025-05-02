from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    
    dbs = client.list_database_names()
    
    print("Conexión exitosa a MongoDB.")
    print("Bases de datos disponibles:", dbs)

except Exception as e:
    print("Error al conectar con MongoDB:")
    print(e)
