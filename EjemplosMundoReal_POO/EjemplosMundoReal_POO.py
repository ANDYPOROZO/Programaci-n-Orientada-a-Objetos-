# sistema_reservas.py

class Cliente:
    """
    Representa un cliente que reserva una habitación en el hotel.
    """
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"


class Habitacion:
    """
    Representa una habitación del hotel.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} - {self.tipo} - {estado} - ${self.precio}"


class Reserva:
    """
    Representa una reserva realizada por un cliente.
    """
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion
        self.confirmada = False

    def confirmar(self):
        if not self.habitacion.ocupada:
            self.habitacion.ocupada = True
            self.confirmada = True
            return f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}."
        else:
            return "La habitación ya está ocupada."

    def __str__(self):
        estado = "Confirmada" if self.confirmada else "Pendiente"
        return f"Reserva: {self.cliente.nombre} - Habitación {self.habitacion.numero} - {estado}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear clientes
    cliente1 = Cliente("Andy", "andy@example.com")
    cliente2 = Cliente("Ale", "ale@example.com")

    # Crear habitaciones
    habitacion1 = Habitacion(101, "Simple", 50)
    habitacion2 = Habitacion(102, "Doble", 80)

    # Crear reservas
    reserva1 = Reserva(cliente1, habitacion1)
    reserva2 = Reserva(cliente2, habitacion2)

    print(habitacion1)
    print(reserva1.confirmar())
    print(habitacion1)

    print(reserva2)
    print(reserva2.confirmar())
    print(habitacion2)
