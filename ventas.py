from db.conexion import get_db
from datetime import datetime

# Definición de los precios y costos de los salmón
SALMONES = {
    "atlántico": {"precio": 5000, "costo": 3000},
    "nórdico": {"precio": 7000, "costo": 4500},
    "pacífico": {"precio": 3000, "costo": 1500},
}

def registrar_pedido(usuario):
    db = get_db()

    # Buscar usuario en la base de datos, ignorando mayúsculas/minúsculas
    usuario_data = db.usuarios.find_one({"nombre": {"$regex": f"^{usuario}$", "$options": "i"}})

    if not usuario_data:
        print(f"Usuario '{usuario}' no encontrado.")
        return

    print("\n=== Registrar Pedido ===")
    productos = []
    total = 0

    while True:  # Continuamos hasta que el usuario termine de registrar productos
        tipo = input("Tipo de salmón (Atlántico/Nórdico/Pacífico o Enter para terminar): ").strip().lower()

        # Si se deja en blanco, se termina el ciclo
        if tipo == "":
            break

        if tipo not in SALMONES:
            print("Tipo no válido, por favor ingrese uno de los siguientes: Atlántico, Nórdico, Pacífico.")
            continue

        # Manejo de la entrada de kilos
        try:
            kilos = float(input(f"Ingrese kilos de salmón {tipo}: "))
        except ValueError:
            print("Por favor, ingrese un número válido para los kilos.")
            continue

        subtotal = kilos * SALMONES[tipo]["precio"]
        total += subtotal
        productos.append({
            "tipo": tipo,
            "kilos": kilos,
            "precio_kilo": SALMONES[tipo]["precio"],
            "subtotal": subtotal
        })

    # Verificar si no se ingresaron productos
    if not productos:
        print("No se registró ningún producto.")
        return

    # Crear el pedido a insertar en la base de datos
    pedido = {
        "usuario": usuario_data["nombre"],
        "fecha": datetime.now(),
        "productos": productos,
        "total": total
    }

    # Insertar el pedido en la base de datos
    db.pedidos.insert_one(pedido)
    print("Pedido registrado con éxito.")

if __name__ == "__main__":
    usuario = input("Ingrese su nombre de usuario: ").strip().lower()
    registrar_pedido(usuario)
