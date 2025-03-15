import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Datos")  # Título de la ventana
root.geometry("400x300")  # Tamaño de la ventana

# Función para agregar un dato a la lista
def agregar():
    dato = entry.get()  # Obtener el texto ingresado
    if dato:  # Verificar que no esté vacío
        listbox.insert(tk.END, dato)  # Agregar el dato a la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato válido")  # Mensaje de advertencia

# Función para limpiar la lista de datos
def limpiar():
    listbox.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Crear y posicionar los elementos de la interfaz
label = tk.Label(root, text="Ingrese un dato:")  # Etiqueta
label.pack(pady=5)

entry = tk.Entry(root)  # Campo de entrada de texto
entry.pack(pady=5)

boton_agregar = tk.Button(root, text="Agregar", command=agregar)  # Botón para agregar datos
boton_agregar.pack(pady=5)

listbox = tk.Listbox(root)  # Lista para mostrar los datos ingresados
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar)  # Botón para limpiar la lista
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
root.mainloop()
