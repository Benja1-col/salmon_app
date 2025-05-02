from ventas import registrar_pedido

def mostrar_menu_vendedor():
    print("Menú Vendedor:")
    print("1. Registrar pedido de salmón")
    print("2. Salir")
    
    opcion = input("Seleccione una opción: ")
    print(f"Opción seleccionada: {opcion}")  # Para ver qué opción seleccionas

    if opcion == '1':
        usuario = input("Ingrese su nombre: ")
        print(f"Usuario ingresado: {usuario}")  # Para ver el nombre ingresado
        registrar_pedido(usuario)
    elif opcion == '2':
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida, intente nuevamente.")

def main():
    print("Bienvenido al sistema de gestión de pedidos de salmón")
    rol = input("Ingrese su rol (vendedor/administrador): ").strip().lower()
    print(f"Rol seleccionado: {rol}")  # Para confirmar que el rol fue ingresado correctamente

    if rol == "vendedor":
        mostrar_menu_vendedor()
    elif rol == "administrador":
        print("Funcionalidad de administrador aún no implementada.")
    else:
        print("Rol no válido.")

if __name__ == "__main__":
    main()
