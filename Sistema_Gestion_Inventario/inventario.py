import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("❌ El producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("✅ Producto agregado con éxito.")
            self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✅ Producto eliminado.")
            self.guardar_en_archivo()
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("✅ Producto actualizado.")
            self.guardar_en_archivo()
        else:
            print("❌ Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("❌ Producto no encontrado.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("📦 El inventario está vacío.")

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as file:
            json.dump({k: vars(v) for k, v in self.productos.items()}, file)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as file:
                data = json.load(file)
                self.productos = {k: Producto(**v) for k, v in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


def menu():
    inventario = Inventario()

    while True:
        print("\n📦 Menú de Gestión de Inventario")
        print("1️⃣ Agregar producto")
        print("2️⃣ Eliminar producto")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Buscar producto")
        print("5️⃣ Mostrar inventario")
        print("6️⃣ Salir")

        opcion = input("🔹 Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("🔹 ID del producto: ")
            nombre = input("🔹 Nombre del producto: ")
            cantidad = int(input("🔹 Cantidad: "))
            precio = float(input("🔹 Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("🔹 ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("🔹 ID del producto a actualizar: ")
            cantidad = input("🔹 Nueva cantidad (Enter para no cambiar): ")
            precio = input("🔹 Nuevo precio (Enter para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("🔹 Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
