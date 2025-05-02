from db.conexion import get_db

# Definición de los precios y costos por tipo de salmón
SALMONES = {
    "atlántico": {"precio": 5000, "costo": 3000},
    "nórdico": {"precio": 7000, "costo": 4500},
    "pacífico": {"precio": 3000, "costo": 1500},
}

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


def reporte_ganancias():
    db = get_db()
    pedidos = db.pedidos.find()

    # Inicializar acumuladores
    ganancias = {
        "atlántico": {"ventas": 0, "costos": 0},
        "nórdico": {"ventas": 0, "costos": 0},
        "pacífico": {"ventas": 0, "costos": 0},
    }

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


if __name__ == "__main__":
    ver_pedidos()
    reporte_ganancias()
