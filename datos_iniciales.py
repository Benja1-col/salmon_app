from db.conexion import get_db

def cargar_datos():
    db = get_db()

    # Colección de usuarios
    usuarios = db.usuarios
    if usuarios.count_documents({}) == 0:
        usuarios.insert_many([
            {"username": "admin", "password": "admin123", "rol": "admin"},
            {"username": "vendedor1", "password": "vendedor123", "rol": "vendedor"},
            {"username": "vendedor2", "password": "vendedor456", "rol": "vendedor"}
        ])
        print("Usuarios insertados.")
    else:
        print("ℹ️ Usuarios ya existen. No se insertaron.")

    # Colección de salmones (stock)
    salmones = db.salmones
    if salmones.count_documents({}) == 0:
        salmones.insert_many([
            {"tipo": "Atlantico", "precio_kilo": 5000, "costo_kilo": 3000, "stock": 100},
            {"tipo": "Nordico", "precio_kilo": 7000, "costo_kilo": 4500, "stock": 100},
            {"tipo": "Pacifico", "precio_kilo": 3000, "costo_kilo": 1500, "stock": 100}
        ])
        print("Stock inicial de salmones insertado.")
    else:
        print("ℹ️ El stock ya fue insertado anteriormente.")

if __name__ == "__main__":
    cargar_datos()
