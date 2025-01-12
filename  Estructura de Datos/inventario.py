from producto import Producto

class Inventario:
    def __init__(self):
        """Inicializa una lista vacía de productos."""
        self.productos = []

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Añade un nuevo producto si el ID es único."""
        if any(prod.get_id() == id_producto for prod in self.productos):
            print("Error: El ID ya existe.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID."""
        self.productos = [prod for prod in self.productos if prod.get_id() != id_producto]
        print("Producto eliminado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o el precio de un producto por ID."""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre."""
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos.")

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos:
                print(prod)
