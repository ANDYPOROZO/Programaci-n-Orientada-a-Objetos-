# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Tupla con (nombre autor, libro)
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro({self.titulo}, {self.autor}, {self.categoria}, {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros que ha prestado

    def __repr__(self):
        return f"Usuario({self.nombre}, {self.id_usuario})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = {}  # Diccionario de usuarios con id_usuario como clave

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]  # Obtén el objeto Usuario
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]
            print(f"El libro {libro.titulo} ha sido prestado a {usuario.nombre}")
            return True
        return False

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]  # Obtén el objeto Usuario
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"El libro {libro.titulo} ha sido devuelto por {usuario.nombre}")
                    return True
        return False

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio, None) == valor:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        return []


# Crear instancias de libros
libro1 = Libro("Python para Todos", ("Guido van Rossum", "Python para Todos"), "Programación", "1234567890")
libro2 = Libro("El Arte de la Guerra", ("Sun Tzu", "El Arte de la Guerra"), "Estrategia", "0987654321")

# Crear instancias de usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("María López", "U002")

# Crear instancia de biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("1234567890", "U001")

# Buscar libros por autor
resultados = biblioteca.buscar_libro("autor", ("Guido van Rossum", "Python para Todos"))
print("Libros encontrados por autor:", resultados)

# Listar libros prestados a un usuario
prestados = biblioteca.listar_libros_prestados("U001")
print("Libros prestados a Juan Pérez:", prestados)

# Devolver un libro
biblioteca.devolver_libro("1234567890", "U001")
