from db.conexion import get_db

SALMONES = ["Atlántico", "Nórdico", "Pacífico"]

def ver_stock():
    db = get_db()
    print("\n=== Stock Actual ===")
    for tipo in SALMONES:
        # Buscamos el stock del tipo de salmón
        stock = db.stock.find_one({"tipo": tipo})
        if stock:
            # Verificamos si está disponible
            disponible = "Disponible" if stock.get("disponible", True) else "No disponible"
            print(f"{tipo.capitalize()}: {stock['kilos']} kilos - {disponible}")
        else:
            print(f"{tipo.capitalize()}: No registrado")
    print("======================\n")

def editar_stock():
    db = get_db()
    tipo = input("Ingrese el tipo de salmón a editar (Atlántico/Nórdico/Pacífico): ").strip().capitalize()

    # Validamos que el tipo sea válido
    if tipo not in SALMONES:
        print("Tipo de salmón no válido.")
        return

    try:
        nuevo_stock = float(input("Ingrese el nuevo stock en kilos: "))  # Pedimos el nuevo stock
        disponible_input = input("¿Está disponible? (s/n): ").strip().lower()
        # Convertimos la respuesta a booleano
        disponible = True if disponible_input == "s" else False
    except ValueError:
        print("Error: ingrese un número válido para el stock.")
        return

    # Actualizamos el stock en la base de datos
    result = db.stock.update_one(
        {"tipo": tipo},
        {"$set": {"kilos": nuevo_stock, "disponible": disponible}},  # Actualizamos kilos y disponibilidad
        upsert=True  # Si no existe, lo crea
    )
    
    if result.matched_count > 0:
        print(f"Stock actualizado para {tipo}.")
    else:
        print(f"No se pudo actualizar el stock para {tipo}.")

if __name__ == "__main__":
    while True:
        print("\n=== Gestor de Stock ===")
        print("1. Ver stock")
        print("2. Editar stock")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_stock()
        elif opcion == "2":
            editar_stock()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
