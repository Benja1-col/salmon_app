from pymongo import MongoClient

def get_db():
    # Conectar a MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Conexión a MongoDB local
    db = client["acme_smoked_fish"]  # Nombre de la base de datos
    return db
