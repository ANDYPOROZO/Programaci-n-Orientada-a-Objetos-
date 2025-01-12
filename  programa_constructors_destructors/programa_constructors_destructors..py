# Definimos la clase Libro
class Libro:
    # Constructor (__init__) que inicializa el título y autor del libro
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Asigna el título a un atributo del objeto
        self.autor = autor  # Asigna el autor a un atributo del objeto
        print(f"El libro '{self.titulo}' de {self.autor} ha sido creado.")  # Imprime mensaje al crear el libro

    # Destructor (__del__) que se llama cuando el objeto es destruido
    def __del__(self):
        print(f"El libro '{self.titulo}' de {self.autor} ha sido destruido.")  # Imprime mensaje al destruir el libro


# Creamos objetos de la clase Libro
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")  # Crear el primer libro
libro2 = Libro("1984", "George Orwell")  # Crear el segundo libro

# Al finalizar el programa, los objetos se destruyen y se imprime el mensaje del destructor

