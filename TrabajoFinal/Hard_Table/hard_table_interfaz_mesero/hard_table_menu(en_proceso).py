import tkinter as tk
import customtkinter as ctk

# ======================
# CONFIGURACIÓN GENERAL
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO_VENTANA = "#F5F5F5"
COLOR_PANEL = "#820808"      # color de paneles (luego backend)
COLOR_BOTON = "#6A1B9A"
COLOR_BOTON_HOVER = "#8E24AA"
COLOR_UPBC2 = "#FFFFFF"

FUENTE_TITULO = ("Segoe UI", 22, "bold")
FUENTE_TEXTO = ("Segoe UI", 14)

# ======================
# VENTANA MENÚ PRINCIPAL
# ======================
ventana = tk.Tk()
ventana.title("HardTable - Menú Principal")
ventana.geometry("1150x700")
ventana.configure(bg=COLOR_FONDO_VENTANA)
ventana.resizable(False, False)

# Centrar ventana
ventana.update_idletasks()
w = ventana.winfo_width()
h = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (w // 2)
y = (ventana.winfo_screenheight() // 2) - (h // 2)
ventana.geometry(f"{w}x{h}+{x}+{y}")

# ========= MARCO PRINCIPAL =========
frame = ctk.CTkFrame(
    ventana,
    corner_radius=20,
    fg_color=COLOR_UPBC2,
    width=1500,
    height=720
)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.pack_propagate(False)

# ========= TÍTULO =========
titulo = tk.Label(
    frame,
    text="Menú Hard Table",
    font=FUENTE_TITULO,
    bg=COLOR_UPBC2,
    fg="#333"
)
titulo.pack(pady=(20, 30))

# ========= BOTONES =========
btn_admin = ctk.CTkButton(
    frame,
    text="Administrador",
    font=("Segoe UI", 16, "bold"),
    fg_color=COLOR_BOTON,
    hover_color=COLOR_BOTON_HOVER,
    text_color="white",
    corner_radius=12,
    width=300,
    height=60
)
btn_admin.place(x=200,y=100)

btn_mesero = ctk.CTkButton(
    frame,
    text="Mesero",
    font=("Segoe UI", 16, "bold"),
    fg_color=COLOR_BOTON,
    hover_color=COLOR_BOTON_HOVER,
    text_color="white",
    corner_radius=12,
    width=300,
    height=60
)
btn_mesero.place(x=200,y=170)

btn_cocina = ctk.CTkButton(
    frame,
    text="Cocina",
    font=("Segoe UI", 16, "bold"),
    fg_color=COLOR_BOTON,
    hover_color=COLOR_BOTON_HOVER,
    text_color="white",
    corner_radius=12,
    width=300,
    height=60
)
btn_cocina.place(x=200,y=240)

ventana.mainloop()
