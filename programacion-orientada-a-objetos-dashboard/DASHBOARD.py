import os
import subprocess


def mostrar_codigo(ruta_script):
    """
    Función para leer y mostrar el código de un script dado.
    Parámetro:
        ruta_script (str): Ruta del archivo Python a leer.
    Retorna:
        str: Contenido del archivo o None si hay un error.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python desde la terminal y guarda un historial.
    """
    try:
        with open("historial.txt", "a") as historial:
            historial.write(f"Ejecutado: {ruta_script}\n")

        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """
    Muestra el menú principal para seleccionar unidades y scripts.
    """
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Mis Proyectos'  # Nueva unidad personalizada
    }

    while True:
        print("\n🚀 Bienvenido al Panel de Gestión de Proyectos 🚀")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("8 - Ejecutar un script personalizado")
        print("0 - Salir")

        eleccion_unidad = input("Elige una opción o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad == '8':
            ejecutar_script_personalizado()
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Intenta de nuevo.")


def ejecutar_script_personalizado():
    """
    Permite ejecutar un script ingresando la ruta manualmente.
    """
    ruta = input("Ingresa la ruta completa del script que deseas ejecutar: ")
    if os.path.exists(ruta) and ruta.endswith('.py'):
        ejecutar_codigo(ruta)
    else:
        print("Ruta inválida o el archivo no es un script Python.")


def mostrar_sub_menu(ruta_unidad):
    """
    Muestra las subcarpetas dentro de la unidad seleccionada.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Intenta de nuevo.")


def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts en la subcarpeta seleccionada y permite ejecutarlos.
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()


