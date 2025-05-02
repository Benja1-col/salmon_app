from db.conexion import get_db
from datetime import datetime
from collections import defaultdict

SALMONES = {
    "atlántico": {"precio": 5000, "costo": 3000},
    "nórdico": {"precio": 7000, "costo": 4500},
    "pacífico": {"precio": 3000, "costo": 1500},
}

# Función para ver todos los pedidos
def ver_pedidos():
    db = get_db()
    pedidos = db.pedidos.find()

    print("\n=== Lista de Pedidos ===")
    for pedido in pedidos:
        print(f"\nUsuario: {pedido['usuario']}")
        print(f"Fecha: {pedido['fecha']}")
        print("Productos:")
        for producto in pedido['productos']:
            print(f" - {producto['tipo'].capitalize()} | Kilos: {producto['kilos']} | Precio/Kg: ${producto['precio_kilo']} | Subtotal: ${producto['subtotal']}")
        print(f"Total pedido: ${pedido['total']}")
    print("=== Fin de la lista ===\n")

# Función para generar reporte de ganancias
def reporte_ganancias():
    db = get_db()
    pedidos = db.pedidos.find()

    # Inicializar acumuladores
    ganancias = defaultdict(lambda: {"ventas": 0, "costos": 0})

    for pedido in pedidos:
        for producto in pedido["productos"]:
            tipo = producto["tipo"]
            kilos = producto["kilos"]
            precio = SALMONES[tipo]["precio"]
            costo = SALMONES[tipo]["costo"]

            ganancias[tipo]["ventas"] += kilos * precio
            ganancias[tipo]["costos"] += kilos * costo

    print("\n=== Reporte de Ganancias ===")
    for tipo, valores in ganancias.items():
        ganancia = valores["ventas"] - valores["costos"]
        print(f"{tipo.capitalize()}: Ventas=${valores['ventas']} | Costos=${valores['costos']} | Ganancia=${ganancia}")
    print("=== Fin del reporte ===\n")

# Función para editar stock
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
    result = db.salmones.update_one(
        {"tipo": tipo},
        {"$set": {"stock": nuevo_stock, "disponible": disponible}},  # Actualizamos kilos y disponibilidad
        upsert=True  # Si no existe, lo crea
    )
    
    if result.matched_count > 0:
        print(f"Stock actualizado para {tipo}.")
    else:
        print(f"No se pudo actualizar el stock para {tipo}.")

# Menú principal de administración
def menu_administrador():
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Ver pedidos")
        print("2. Editar stock")
        print("3. Ver reporte de ganancias")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ver_pedidos()
        elif opcion == '2':
            editar_stock()
        elif opcion == '3':
            reporte_ganancias()
        elif opcion == '4':
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_administrador()
