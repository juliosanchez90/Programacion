import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# ======================
# CONFIGURACIÓN GENERAL
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO_VENTANA = "#F5F5F5"
COLOR_PANEL = "#820808"      # paneles (zona backend)
COLOR_BOTON = "#6A1B9A"
COLOR_BOTON_HOVER = "#8E24AA"
COLOR_UPBC2 = "#FFFFFF"

FUENTE_TITULO = ("Segoe UI", 18, "bold")
FUENTE_TEXTO = ("Segoe UI", 12)

# ======================
# VENTANA ASIGNACIÓN DE MESERO
# ======================
ventana = tk.Tk()
ventana.title("HardTable 1.0 - Asignación de mesero")
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
    text="Asignación de mesero",
    font=FUENTE_TITULO,
    bg=COLOR_UPBC2,
    fg="#333"
)
titulo.place(relx=0.5, y=20, anchor="n")

# ========= TÍTULO PANEL IZQUIERDO =========
lbl_meseros = tk.Label(
    frame,
    text="Lista de meseros",
    font=FUENTE_TEXTO,
    bg=COLOR_UPBC2,
    fg="#333"
)
lbl_meseros.place(x=70, y=105)

# ========= PANEL IZQUIERDO: LISTA DE MESEROS =========
panel_meseros = ctk.CTkFrame(
    frame,
    width=320,
    height=440,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_meseros.place(x=50, y=130)

# -------- ZONA BACKEND: lista de meseros (llenar desde SQL) --------
cols_meseros = ("id", "nombre")
tree_meseros = ttk.Treeview(
    panel_meseros,
    columns=cols_meseros,
    show="headings"
)
tree_meseros.heading("id", text="ID")
tree_meseros.heading("nombre", text="Nombre")

tree_meseros.column("id", width=60, anchor="center")
tree_meseros.column("nombre", width=260, anchor="w")

# colocamos dentro del panel, dejando margen rojo
tree_meseros.place(x=6, y=6, width=290, height=430)

scroll_meseros = ttk.Scrollbar(
    panel_meseros,
    orient="vertical",
    command=tree_meseros.yview
)
scroll_meseros.place(x=295, y=6, height=430)
tree_meseros.configure(yscrollcommand=scroll_meseros.set)

# ========= TÍTULO PANEL DERECHO =========
lbl_mesas = tk.Label(
    frame,
    text="Lista de mesas y sus meseros ya asignados",
    font=FUENTE_TEXTO,
    bg=COLOR_UPBC2,
    fg="#333"
)
lbl_mesas.place(x=430, y=105)

# ========= PANEL DERECHO: LISTA DE MESAS Y MESEROS ASIGNADOS =========
panel_mesas = ctk.CTkFrame(
    frame,
    width=590,
    height=440,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_mesas.place(x=400, y=130)

# -------- ZONA BACKEND: lista de mesas + mesero asignado --------
cols_mesas = ("mesa", "mesero")
tree_mesas = ttk.Treeview(
    panel_mesas,
    columns=cols_mesas,
    show="headings"
)
tree_mesas.heading("mesa", text="Mesa")
tree_mesas.heading("mesero", text="Mesero asignado")

tree_mesas.column("mesa", width=80, anchor="center")
tree_mesas.column("mesero", width=480, anchor="w")

tree_mesas.place(x=15, y=6, width=550, height=430)

scroll_mesas = ttk.Scrollbar(
    panel_mesas,
    orient="vertical",
    command=tree_mesas.yview
)
scroll_mesas.place(x=556, y=6, height=430)
tree_mesas.configure(yscrollcommand=scroll_mesas.set)

# ========= FUNCIÓN PARA CREAR BOTONES =========
def crear_boton(parent, text, x, y, cmd=None, w=180, h=45):
    btn = ctk.CTkButton(
        parent,
        text=text,
        font=("Segoe UI", 14, "bold"),
        fg_color=COLOR_BOTON,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        corner_radius=12,
        width=w,
        height=h,
        command=cmd
    )
    btn.place(x=x, y=y)
    return btn

# ----------- BOTONES INFERIORES ----------------------
crear_boton(frame, "Asignar", 120, 580)
crear_boton(frame, "Reasignar", 320, 580)
crear_boton(frame, "Quitar asignación", 520, 580, w=200)
crear_boton(frame, "Guardar", 750, 580)

ventana.mainloop()
