import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga productos desde el archivo de texto."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as file:
                    for linea in file:
                        datos = linea.strip().split(",")
                        if len(datos) == 4:
                            codigo, nombre, cantidad, precio = datos
                            self.productos.append(Producto(codigo, nombre, int(cantidad), float(precio)))
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda los productos en el archivo de texto."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(str(producto) + "\n")
        except (PermissionError, IOError) as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        """Agrega un nuevo producto y guarda en el archivo."""
        self.productos.append(Producto(codigo, nombre, cantidad, precio))
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, codigo):
        """Elimina un producto por código."""
        self.productos = [p for p in self.productos if p.codigo != codigo]
        self.guardar_en_archivo()
        print("Producto eliminado exitosamente.")

    def listar_productos(self):
        """Muestra todos los productos del inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(f"Código: {p.codigo}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Listar productos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(codigo, nombre, cantidad, precio)

        elif opcion == "2":
            codigo = input("Ingrese código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)

        elif opcion == "3":
            inventario.listar_productos()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
