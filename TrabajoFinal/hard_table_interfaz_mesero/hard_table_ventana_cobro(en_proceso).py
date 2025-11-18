import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# ======================
# CONFIGURACIÓN GENERAL
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO_VENTANA = "#F5F5F5"
COLOR_PANEL = "#820808"      # paneles (luego backend los usa)
COLOR_BOTON = "#6A1B9A"
COLOR_BOTON_HOVER = "#8E24AA"
COLOR_UPBC2 = "#FFFFFF"

FUENTE_TITULO = ("Segoe UI", 18, "bold")
FUENTE_TEXTO = ("Segoe UI", 12)

# ======================
# VENTANA CERRAR CUENTA / COBRO
# ======================
ventana = tk.Tk()
ventana.title("HardTable 1.0 - Cerrar cuenta / cobro")
ventana.geometry("1150x700")
ventana.configure(bg=COLOR_FONDO_VENTANA)
ventana.resizable(False, False)

# Centrar ventana
ventana.update_idletasks()
ancho = ventana.winfo_width()
alto = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
y = (ventana.winfo_screenheight() // 2) - (alto // 2)
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# ========= MARCO PRINCIPAL =========
frame = ctk.CTkFrame(
    ventana,
    corner_radius=20,
    fg_color=COLOR_UPBC2,
    width=1050,
    height=650
)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.pack_propagate(False)

# ========= TÍTULO =========
titulo = tk.Label(
    frame,
    text="Ventana de cerrar cuenta o cobro",
    font=FUENTE_TITULO,
    bg=COLOR_UPBC2,
    fg="#333"
)
titulo.place(relx=0.5, y=20, anchor="n")

# ========= BOTÓN SELECCIONAR MESA =========
btn_seleccionar_mesa = ctk.CTkButton(
    frame,
    text="Seleccionar mesa",
    font=("Segoe UI", 16, "bold"),
    fg_color=COLOR_BOTON,
    hover_color=COLOR_BOTON_HOVER,
    text_color="white",
    corner_radius=12,
    width=360,
    height=60
)
btn_seleccionar_mesa.place(x=80, y=80)

# ========= DISPLAY DE LA CUENTA =========
panel_cuenta = ctk.CTkFrame(
    frame,
    width=360,
    height=420,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_cuenta.place(x=60, y=160)

placeholder_cuenta = tk.Label(
    panel_cuenta,
    text="Display de la cuenta:\nqué se consumió y el total.",
    font=("Segoe UI", 11),
    bg=COLOR_PANEL,
    fg="white",
    justify="center"
)
placeholder_cuenta.place(relx=0.5, rely=0.5, anchor="center")

# ========= PANEL: DINERO QUE SE RECIBE =========
panel_recibe = ctk.CTkFrame(
    frame,
    width=360,
    height=80,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_recibe.place(x=480, y=200)

lbl_recibe = tk.Label(
    panel_recibe,
    text="Dinero que se recibe",
    font=("Segoe UI", 13, "bold"),
    bg=COLOR_PANEL,
    fg="white"
)
lbl_recibe.place(relx=0.5, rely=0.5, anchor="center")

# ========= PANEL: CAMBIO =========
panel_cambio = ctk.CTkFrame(
    frame,
    width=360,
    height=80,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_cambio.place(x=480, y=300)

lbl_cambio = tk.Label(
    panel_cambio,
    text="Cambio",
    font=("Segoe UI", 13, "bold"),
    bg=COLOR_PANEL,
    fg="white"
)
lbl_cambio.place(relx=0.5, rely=0.5, anchor="center")

# ========= BOTONES INFERIORES: COBRAR / FINALIZAR =========
btn_cobrar = ctk.CTkButton(
    frame,
    text="Cobrar",
    font=("Segoe UI", 14, "bold"),
    fg_color=COLOR_BOTON,
    hover_color=COLOR_BOTON_HOVER,
    text_color="white",
    corner_radius=12,
    width=260,
    height=50
)
btn_cobrar.place(x=480, y=500)

btn_finalizar = ctk.CTkButton(
    frame,
    text="Finalizar",
    font=("Segoe UI", 14, "bold"),
    fg_color=COLOR_BOTON,
    hover_color=COLOR_BOTON_HOVER,
    text_color="white",
    corner_radius=12,
    width=260,
    height=50
)
btn_finalizar.place(x=780, y=500)

ventana.mainloop()
