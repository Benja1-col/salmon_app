from db.conexion import get_db

# Función para iniciar sesión
def iniciar_sesion():
    db = get_db()
    usuario = input("Ingrese su nombre de usuario: ").strip().lower()
    password = input("Ingrese su contraseña: ").strip()

    # Buscamos al usuario en la base de datos
    usuario_data = db.usuarios.find_one({"username": usuario})

    # Validación del usuario y contraseña
    if not usuario_data:
        print("Usuario no encontrado.")
        return None

    if usuario_data["password"] != password:
        print("Contraseña incorrecta.")
        return None

    # Si la autenticación es exitosa, mostramos un mensaje de bienvenida
    print(f"Bienvenido {usuario_data['username']} - Rol: {usuario_data['rol']}")
    return usuario_data

# Función para cerrar sesión
def cerrar_sesion():
    print("Sesión cerrada.")

# Función para verificar si el usuario tiene acceso de administrador
def es_admin(usuario_data):
    return usuario_data["rol"] == "admin"

# Función para verificar si el usuario tiene acceso de vendedor
def es_vendedor(usuario_data):
    return usuario_data["rol"] == "vendedor"

# Función para mostrar el menú dependiendo del rol del usuario
def mostrar_menu(usuario_data):
    if es_vendedor(usuario_data):
        mostrar_menu_vendedor()
    elif es_admin(usuario_data):
        mostrar_menu_administrador()
    else:
        print("Rol no válido.")

# Menú para el vendedor
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

# Menú para el administrador
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

# Función auxiliar para registrar pedidos
def registrar_pedido():
    print("Función para registrar pedido aún no implementada.")

# Función auxiliar para ver pedidos
def ver_pedidos():
    print("Función para ver pedidos aún no implementada.")

# Función auxiliar para editar stock
def editar_stock():
    print("Función para editar stock aún no implementada.")

# Función auxiliar para generar reporte de ganancias
def reporte_ganancias():
    print("Función para mostrar reporte de ganancias aún no implementada.")

if __name__ == "__main__":
    while True:
        usuario_data = iniciar_sesion()
        if usuario_data:
            mostrar_menu(usuario_data)
