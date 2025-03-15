import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame superior para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Treeview para mostrar eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame de entrada de datos
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

# Widgets de entrada
tk.Label(frame_inputs, text="Fecha:").grid(row=0, column=0)
calendario = DateEntry(frame_inputs)
calendario.grid(row=0, column=1)

tk.Label(frame_inputs, text="Hora:").grid(row=1, column=0)
hora_entry = tk.Entry(frame_inputs)
hora_entry.grid(row=1, column=1)

tk.Label(frame_inputs, text="Descripción:").grid(row=2, column=0)
desc_entry = tk.Entry(frame_inputs)
desc_entry.grid(row=2, column=1)

# Botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)


def agregar_evento():
    fecha = calendario.get()
    hora = hora_entry.get()
    descripcion = desc_entry.get()

    if not fecha or not hora or not descripcion:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    tree.insert("", "end", values=(fecha, hora, descripcion))
    hora_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)


def eliminar_evento():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showerror("Error", "Selecciona un evento para eliminar")
        return

    if messagebox.askyesno("Confirmación", "¿Seguro que quieres eliminar este evento?"):
        tree.delete(seleccion)


tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=10)
tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).pack(side="left", padx=10)
tk.Button(frame_botones, text="Salir", command=root.quit).pack(side="left", padx=10)

root.mainloop()
