from db.conexion import get_db

def iniciar_sesion():
    db = get_db()
    usuario = input("Ingrese su nombre de usuario: ").strip().lower()
    print(f"Buscando el usuario: {usuario}...")
    usuario_data = db.usuarios.find_one({"nombre": {"$regex": f"^{usuario}$", "$options": "i"}})

    if not usuario_data:
        print("Usuario no encontrado.")
        return None

    print(f"Usuario encontrado: {usuario_data['nombre']}, Rol: {usuario_data['rol']}")
    return usuario_data

def cerrar_sesion():
    print("Sesión cerrada.")
    exit()

def mostrar_menu_usuario(usuario_data):
    if usuario_data["rol"] == "vendedor":
        mostrar_menu_vendedor()
    elif usuario_data["rol"] == "administrador":
        mostrar_menu_administrador()
    else:
        print("Rol no válido.")

def mostrar_menu_vendedor():
    print("Menú Vendedor:")
    print("1. Registrar pedido de salmón")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        print("Registrar pedido (función aún no conectada)")
    elif opcion == '2':
        cerrar_sesion()
    else:
        print("Opción inválida.")

def mostrar_menu_administrador():
    print("Menú Administrador:")
    print("1. Ver pedidos")
    print("2. Editar stock")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        print("Ver pedidos (función aún no conectada)")
    elif opcion == '2':
        print("Editar stock (función aún no conectada)")
    elif opcion == '3':
        cerrar_sesion()
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    usuario_data = iniciar_sesion()
    if usuario_data:
        mostrar_menu_usuario(usuario_data)
