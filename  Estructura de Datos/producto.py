class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor para inicializar un producto."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Representación en cadena del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    # Getters y Setters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
