import tkinter as tk
from tkinter import simpledialog, messagebox

# Diccionario para guardar las ventanas de cada personaje
ventanas_personajes = {}

# --- Función para abrir o enfocar una ventana de personaje ---
def abrir_o_enfocar_ventana(nombre):
    if nombre in ventanas_personajes:
        # Si ya existe, simplemente enfocar
        ventana = ventanas_personajes[nombre]
        ventana.deiconify()  # Mostrar si estaba minimizada
        ventana.lift()       # Traer al frente
        ventana.focus_force()
    else:
        # Crear una nueva ventana
        nueva = tk.Toplevel(root)
        nueva.title(nombre)
        nueva.geometry("300x400")
        nueva.resizable(False, False)

        # Evento al cerrar: esconder la ventana, no destruir
        def al_cerrar():
            nueva.withdraw()  # Esconder la ventana
        nueva.protocol("WM_DELETE_WINDOW", al_cerrar)

        # Agrega widgets en la ventana de personaje
        label = tk.Label(nueva, text=f"Stats de {nombre}")
        label.pack(pady=20)

        # Guardar en el diccionario
        ventanas_personajes[nombre] = nueva

# --- Acción cuando se presiona el botón 'Añadir Jugador' ---
def accion_añadir_jugador():
    nombre = simpledialog.askstring("Nombre del jugador", "Ingrese el nombre del jugador:")
    if not nombre:
        return  # Si se cancela o deja vacío

    if nombre in ventanas_personajes:
        abrir_o_enfocar_ventana(nombre)
    else:
        abrir_o_enfocar_ventana(nombre)
        lista_personajes.insert(tk.END, nombre)  # Agregar a la lista visual

# --- Acción cuando se selecciona un nombre en la lista ---
def accion_seleccionar(event):
    seleccion = lista_personajes.curselection()
    if seleccion:
        nombre = lista_personajes.get(seleccion[0])
        abrir_o_enfocar_ventana(nombre)

# --- Configuración de la ventana principal ---
root = tk.Tk()
root.title('Menú Principal')

window_width = 400
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

try:
    photo = tk.PhotoImage(file='./assets/CoCTrackerIcon.png')
    root.iconphoto(False, photo)
except tk.TclError:
    print("icon file not found.")

# Título principal
titulo = tk.Label(root, text="Personajes registrados", font=("Helvetica", 14))
titulo.pack(pady=10)

# Lista de personajes
lista_personajes = tk.Listbox(root)
lista_personajes.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
lista_personajes.bind('<<ListboxSelect>>', accion_seleccionar)

# Botón para añadir jugador
boton_nuevo = tk.Button(root, text="Añadir Jugador", command=accion_añadir_jugador)
boton_nuevo.pack(pady=10)

# Ejecutar aplicación
root.mainloop()