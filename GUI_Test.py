import tkinter as tk


root = tk.Tk()
root.title('Menú Principal')

window_width = 400
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

try:
    photo = tk.PhotoImage(file='./assets/CoCTrackerIcon.png')
    root.iconphoto(False, photo)
except tk.TclError:
    print("icon file not found.")


# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()