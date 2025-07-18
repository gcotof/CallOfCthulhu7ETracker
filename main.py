import tkinter as tk

def abrir_ventana_jugador():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Stats del Jugador")
    nueva_ventana.geometry("300x400")
    nueva_ventana.resizable(False, False)

    label = tk.Label(nueva_ventana, text="Placeholder Añadir Stats Jugador")
    label.pack(pady=20)




#Configuración de ventana principal
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

# Etiqueta de bienvenida
message = tk.Label(root, text="Hello, World!")
message.pack(pady=10)

# Botón para abrir nueva ventana
boton_nueva_ventana = tk.Button(root, text="Añadir Jugador", command=abrir_ventana_jugador)
boton_nueva_ventana.pack(pady=20)

# Mantener ventana principal abierta
root.mainloop()