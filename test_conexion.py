from pymongo import MongoClient

try:
    # Intenta conectarte al servidor MongoDB local
    client = MongoClient("mongodb://localhost:27017/")
    
    # Intenta obtener el nombre de las bases de datos
    dbs = client.list_database_names()
    
    print("Conexión exitosa a MongoDB.")
    print("Bases de datos disponibles:", dbs)

except Exception as e:
    print("Error al conectar con MongoDB:")
    print(e)
