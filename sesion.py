from db.conexion import get_db

def iniciar_sesion():
    db = get_db()
    usuario = input("Ingrese su nombre de usuario: ").strip().lower()
    password = input("Ingrese su contraseña: ").strip()

    usuario_data = db.usuarios.find_one({"username": usuario})

    if not usuario_data:
        print(" Usuario no encontrado.")
        return None

    if usuario_data["password"] != password:
        print("Contraseña incorrecta.")
        return None

    print(f"Bienvenido {usuario_data['username']} - Rol: {usuario_data['rol']}")
    return usuario_data

def cerrar_sesion():
    print("Sesión cerrada.")

def mostrar_menu_usuario(usuario_data):
    if usuario_data["rol"] == "vendedor":
        mostrar_menu_vendedor()
    elif usuario_data["rol"] == "admin":
        mostrar_menu_administrador()
    else:
        print("Rol no válido.")

def mostrar_menu_vendedor():
    while True:
        print("\n--- Menú Vendedor ---")
        print("1. Registrar pedido de salmón")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_pedido()
        elif opcion == '2':
            cerrar_sesion()
            break
        else:
            print("Opción inválida.")

def mostrar_menu_administrador():
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
            cerrar_sesion()
            break
        else:
            print("Opción inválida.")

# Funciones auxiliares
def registrar_pedido():
    print("Función para registrar pedido aún no implementada.")

def ver_pedidos():
    print("Función para ver pedidos aún no implementada.")

def editar_stock():
    print("Función para editar stock aún no implementada.")

def reporte_ganancias():
    print("Función para mostrar reporte de ganancias aún no implementada.")

if __name__ == "__main__":
    while True:
        usuario_data = iniciar_sesion()
        if usuario_data:
            mostrar_menu_usuario(usuario_data)
