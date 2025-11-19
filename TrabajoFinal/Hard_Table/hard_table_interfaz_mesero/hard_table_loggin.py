import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os

#VENTANA PRINCIPIAL
ventana = tk.Tk()
ventana.title("HardTable 1.0 - Iniciar Sesión")
ventana.geometry("480x350")
ventana.resizable(False, False)
ventana.configure(bg="#F5F5F5")

ventana.update_idletasks()
ancho = ventana.winfo_width()
alto = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
y = (ventana.winfo_screenheight() // 2) - (alto // 2)
ventana.geometry(f"+{x}+{y}")
#icono = tk.PhotoImage(file="recursos/logo2.png")
#ventana.iconphoto(False, icono)
#ASDASD



#MARCO PRINCIPAL INICIO SESION
frame = ctk.CTkFrame(
    ventana,
    corner_radius=20,    # ← esquinas redondeadas del marco
    fg_color="white",
    width=400, height=360
)
frame.place(relx=0.5, rely=0.5, anchor="center")


titulo = tk.Label(frame, text="Hard Table", font=("Segoe UI", 18, "bold"), bg="white", fg="#333")
titulo.pack(pady=(20, 10))

# #ETIQUETAS
usuario_label = tk.Label(frame, text="Usuario", font=("Segoe UI", 12), bg="white", fg="#555")
usuario_label.pack(anchor="w", padx=40, pady=(10, 0))
usuario_entry = ttk.Entry(frame, font=("Segoe UI", 12))
usuario_entry.pack(padx=40, fill="x", pady=5)

contrasena_label = tk.Label(frame, text="Contraseña", font=("Segoe UI", 12), bg="white", fg="#555")
contrasena_label.pack(anchor="w", padx=40, pady=(10, 0))
contrasena_entry = ttk.Entry(frame, font=("Segoe UI", 12), show="*")
contrasena_entry.pack(padx=40, fill="x", pady=5)

# BOTON PA ENTRAR
def iniciar_sesion():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    print(f"Usuario: {usuario}, Contraseña: {contrasena}")

boton = ctk.CTkButton(
    frame,
    text="Entrar",
    font=("Segoe UI", 18, "bold"),
    fg_color="#6A1B9A",        # color púrpura principal
    hover_color="#8E24AA",     # color al pasar el mouse
    text_color="white",
    corner_radius=12,          # ← esquinas redondeadas del botón
    height=36,
    width=240,
    command=iniciar_sesion,
)
boton.pack(pady=(15, 15), ipadx=1, ipady=5)



ventana.mainloop()
