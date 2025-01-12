from inventario import Inventario

def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto")
    print("5. Mostrar Inventario")
    print("6. Salir")

# Instancia del Inventario
inventario = Inventario()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_producto = input("Ingrese ID: ")
        nombre = input("Ingrese nombre: ")
        cantidad = int(input("Ingrese cantidad: "))
        precio = float(input("Ingrese precio: "))
        inventario.agregar_producto(id_producto, nombre, cantidad, precio)

    elif opcion == "2":
        id_producto = input("Ingrese ID del producto a eliminar: ")
        inventario.eliminar_producto(id_producto)

    elif opcion == "3":
        id_producto = input("Ingrese ID del producto a actualizar: ")
        cantidad = input("Nueva cantidad (dejar vacío para no modificar): ")
        precio = input("Nuevo precio (dejar vacío para no modificar): ")

        cantidad = int(cantidad) if cantidad else None
        precio = float(precio) if precio else None

        inventario.actualizar_producto(id_producto, cantidad, precio)

    elif opcion == "4":
        nombre = input("Ingrese nombre del producto a buscar: ")
        inventario.buscar_producto(nombre)

    elif opcion == "5":
        inventario.mostrar_inventario()

    elif opcion == "6":
        print("Saliendo del sistema.")
        break

    else:
        print("Opción no válida, intente de nuevo.")
