from tkinter import * 
from FuncionesValidacion import *
from ConexionBD import *

#ventana
ventana = Tk()
ventana.title("Formulario de contacto para ISAUI")
ventana.geometry("1366x768")
ventana.attributes("-fullscreen", True) #se puede quitar y funciona correctamente la selección de la resolución 
ventana.configure(bg="#d7cfbf")
ventana.resizable(False, False)

variable = IntVar()

def getSeleccionCarrera():
    carrera = variable.get()
    return carrera

def getEntradasUsuario():
        apellido = entry_apellido.get().strip()
        nombre = entry_nombre.get().strip() 
        dni = entry_dni.get().strip()
        telefono = entry_telefono.get().strip()
        correo = entry_correo.get().strip()
        domicilio= entry_domicilio.get().strip()
        ciudad= entry_ciudad.get().strip()
        instagram = entry_instagram.get().strip()
        return apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram

def limpiar_campos(entries):
    for entry in entries:
        entry.delete(0, END)

def guardar_datos():

    carrera = getSeleccionCarrera()
    entries = [entry_apellido, entry_nombre, entry_dni, entry_telefono, entry_correo, entry_domicilio, entry_ciudad, entry_instagram]
    if not validar_campos_obligatorios(entries):
        return  #Detener si los campos están vacíos
    
    apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram = getEntradasUsuario()
        
    #validaciones del archivo FuncionesValidacion
    if not verificar_correo(correo):
        return 
    if not validar_dni(dni):
        return  
    if not validar_telefono(telefono):
        return   
    if (messagebox.askyesno("Confirmar", "¿Desea guardar los datos?")):
        insertar_persona(apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram, carrera)
        limpiar_campos(entries)
    else:
        messagebox.showinfo("Cancelado", "No se guardaron los datos.")
    
def procesar_formulario():
    apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram = getEntradasUsuario()
    
    if (apellido, nombre, dni):  #Simple validación de que algunos campos no estén vacíos
        insertar_persona(apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram)
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

#Función para el botón "Volver"
def volver():
    ventana.destroy()  #Cierra la ventana actual

#marco
frame = LabelFrame(ventana, text="Seleccione la carrera", bg="white", font=('Calibri', 20), borderwidth=5)
frame.grid(row=0, column=0,padx=60, pady=50, columnspan=8, sticky="ew")

frame_datos = LabelFrame(ventana, text="Ingrese sus datos:", bg="#cac5bc", font=('Calibri', 20), borderwidth=5)
frame_datos.grid(row=1,padx=60, column=0,columnspan=8, pady=30, sticky="nsew")

#Para que ambos frames tengan el mismo ancho


#etiquetas 
label_apellido = Label(frame_datos, text="Apellido: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_apellido.grid(row=2, column=0, pady=10, ipadx=100)

label_nombre = Label(frame_datos, text="Nombre: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_nombre.grid(row=3, column=0, pady=10, ipadx=100)

label_dni = Label(frame_datos, text="DNI: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_dni.grid(row=4, column=0, pady=10, ipadx=100,)

label_telefono = Label(frame_datos, text="Teléfono: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_telefono.grid(row=5, column=0, pady=10, ipadx=100)

label_domicilio = Label(frame_datos, text="Domicilio: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_domicilio.grid(row=6, column=0, pady=10, ipadx=100)

label_ciudad = Label(frame_datos, text="Ciudad: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_ciudad.grid(row=7, column=0, pady=10, ipadx=100)

label_correo = Label(frame_datos, text="Correo: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_correo.grid(row=8, column=0, pady=10, ipadx=100)

label_instagram = Label(frame_datos, text="Instagram: ", bg="#cac5bc", fg="black", font=('Calibri', 15))
label_instagram.grid(row=9, column=0, pady=10, ipadx=100)

#entradas
entry_apellido = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_apellido.grid(row=2, column=1, ipadx=330, pady=10,columnspan=5)

entry_nombre = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_nombre.grid(row=3, column=1, ipadx=330,pady=10, columnspan=5)

entry_dni = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_dni.grid(row=4, column=1, ipadx=330,pady=10, columnspan=5)

entry_telefono = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_telefono.grid(row=5, column=1, ipadx=330,pady=10, columnspan=5)

entry_domicilio = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_domicilio.grid(row=6, column=1, ipadx=330,pady=10, columnspan=5)

entry_ciudad = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_ciudad.grid(row=7, column=1, ipadx=330,pady=10, columnspan=5)

entry_correo = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_correo.grid(row=8, column=1, ipadx=330,pady=10, columnspan=5)

entry_instagram = Entry(frame_datos, bg="white", font=('Calibri', 15))
entry_instagram.grid(row=9, column=1, ipadx=330,pady=10, columnspan=5)

#radio botones
btn_software = Radiobutton(frame, text="Desarrollo de Software", variable=variable, value=1, borderwidth=2, bg="white", font=('Calibri', 13))
btn_software.grid(row=1, column=3, padx=10, pady=10)

btn_enfermeria = Radiobutton(frame, text="Enfermería", variable=variable, value=2, borderwidth=2, bg="white", font=('Calibri', 13))
btn_enfermeria.grid(row=1, column=4, padx=10, pady=10)

btn_disenio = Radiobutton(frame, text="Diseño de Espacios", variable=variable, value=3, borderwidth=2, bg="white", font=('Calibri', 13))
btn_disenio.grid(row=1, column=5, padx=10, pady=10)

btn_trekking = Radiobutton(frame, text="Guía de Trekking y Guía de montaña", variable=variable, value=4, borderwidth=2, bg="white", font=('Calibri', 13))
btn_trekking.grid(row=1, column=8, padx=10, pady=10)

btn_guia = Radiobutton(frame, text="Guía en Turismo", variable=variable, value=5, borderwidth=2, bg="white", font=('Calibri', 13))
btn_guia.grid(row=1, column=6, padx=10, pady=10)

btn_guia_turismo_hoteleria = Radiobutton(frame, text="Guía de Turismo y Hotelería", variable=variable, value=6, borderwidth=2, bg="white", font=('Calibri', 13))
btn_guia_turismo_hoteleria.grid(row=1, column=7, padx=10, pady=10)

#botón Guardar
btn_guardar = Button(frame_datos, text="Guardar", borderwidth=2, bg="#589cf9", font=('Calibri', 15), command=guardar_datos)
btn_guardar.grid(row=10, column=2, padx=10, pady=10, ipadx=20, sticky="ew")

#botón Volver
btn_volver = Button(frame_datos, text="Volver", borderwidth=2, bg="#ffffff", font=('Calibri', 15), command=volver)
btn_volver.grid(row=10, column=4, padx=10, pady=10, ipadx=20, sticky="ew")

ventana.mainloop()