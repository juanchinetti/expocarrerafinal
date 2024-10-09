import tkinter as tk
from tkinter import ttk

#Función para el botón "Volver"
def volver():
    root.destroy()  #Cierra la ventana actual

root = tk.Tk()
root.title("Listado de personas")

style = ttk.Style()  #crear objeto ttk.Style
style.configure("BigFont.TRadiobutton", font=("Helvetica", 14))  #configurar estilo de fuente

label_seleccionar_carrera = ttk.Label(root, bg="grey",text="Seleccionar carrera para filtrar", font=("Calibri", 20, "bold"))
label_seleccionar_carrera.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

frame_superior = tk.Frame(root, bg="grey")
frame_superior.grid(row=1, column=0, sticky="nsew")

frame_inferior = tk.Frame(root, bg="grey")
frame_inferior.grid(row=2, column=0, sticky="nsew")

#Configurar el tamaño de las filas y columnas
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)  #Nueva fila para el botón Volver
root.columnconfigure(0, weight=1)

#botones
variable_de_filtro_carrera = tk.StringVar()

frame_superior.rowconfigure(0, weight=1)
frame_superior.rowconfigure(1, weight=1)
frame_superior.columnconfigure(0, weight=1)
frame_superior.columnconfigure(1, weight=1)
frame_superior.columnconfigure(2, weight=1)

#Añadir radiobuttons de carreras
for i, carrera in enumerate(["Guía de Turismo", "Técnico en Turismo", "Trekking", "Software", "Enfermería", "Espacio"]):
    filtro_carrera = ttk.Radiobutton(frame_superior, text=carrera, variable=variable_de_filtro_carrera, value=carrera, style="BigFont.TRadiobutton")
    row = i // 3  #calcular fila
    col = i % 3  #calcular columna
    filtro_carrera.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)  #configuración de grid

#Tabla Treeview
# Configurar el árbol
arbol = ttk.Treeview(frame_inferior, columns=("apellido", "nombre", "dni", "carrera"), show="headings")
arbol.grid(row=0, column=0, sticky="nsew")

arbol.heading("apellido", text="Apellido")
arbol.heading("nombre", text="Nombre")
arbol.heading("dni", text="DNI")
arbol.heading("carrera", text="Carrera")

arbol.insert("", "end", values=("Pérez", "Juan", "12345678", "Software"))
arbol.insert("", "end", values=("González", "María", "87654321", "Enfermería"))
arbol.insert("", "end", values=("Rodríguez", "Pedro", "34567890", "Técnico en Turismo"))

# Permitir que el Treeview se expanda
frame_inferior.rowconfigure(0, weight=1)
frame_inferior.columnconfigure(0, weight=1)

#Botón registrar
btn_volver = tk.Button(root, text="Registro", bg="lightgray", font=("Calibri", 15))
btn_volver.grid(row=3, column=0, padx=(200,600), pady=20, ipadx=40)

#Botón Volver
btn_volver = tk.Button(root, text="Volver", bg="lightgray", font=("Calibri", 15), command=volver)
btn_volver.grid(row=3, column=0, padx=(500,100), pady=20, ipadx=40)  #Configuración del botón

root.mainloop()