# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalles(self):
        return f"Vehículo de marca {self.marca}, modelo {self.modelo}"


# Clase derivada que demuestra herencia
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.tipo = tipo

    # Sobrescribiendo el método detalles para demostrar polimorfismo
    def detalles(self):
        return f"Moto {self.tipo} de marca {self.marca}, modelo {self.modelo}"


# Clase con encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para el nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter para la edad
    def get_edad(self):
        return self.__edad

    # Setter para la edad con validación
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo.")


# Polimorfismo con una función que acepta cualquier tipo de vehículo
def mostrar_detalles(vehiculo):
    print(vehiculo.detalles())


# Ejecución del programa
if __name__ == "__main__":
    # Instancia de la clase base
    vehiculo = Vehiculo("Toyota", "Corolla")

    # Instancia de la clase derivada
    moto = Moto("Yamaha", "MT-07", "Deportiva")

    # Uso de encapsulación
    persona = Persona("Andy", 21)
    print(f"Nombre: {persona.get_nombre()}, Edad: {persona.get_edad()}")

    # Cambiando atributos encapsulados
    persona.set_edad(25)
    print(f"Nombre: {persona.get_nombre()}, Edad actualizada: {persona.get_edad()}")

    # Uso de polimorfismo
    mostrar_detalles(vehiculo)  # Salida: Vehículo de marca Toyota, modelo Corolla
    mostrar_detalles(moto)  # Salida: Moto Deportiva de marca Yamaha, modelo MT-07
