import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# ======================
# CONFIGURACIÓN GENERAL
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO_VENTANA = "#F5F5F5"
COLOR_PANEL = "#820808"      # color de cosas para que backend quite
COLOR_BOTON = "#6A1B9A"
COLOR_BOTON_HOVER = "#8E24AA"
COLOR_UPBC2 = "white"

FUENTE_TITULO = ("Segoe UI", 18, "bold")
FUENTE_TEXTO = ("Segoe UI", 12)


# ======================
# FUNCIÓN PARA CREAR BOTONES (REUTILIZABLE)
# ======================
def crear_boton(parent, text, x, y, cmd=None, w=220, h=40):
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


# ======================
# VENTANA PRINCIPAL DE MESERO
# ======================
ventana = tk.Tk()
ventana.title("HardTable 1.0 - Ventana de mesero")
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

# ========= TÍTULOS =========
titulo = tk.Label(
    frame,
    text="Ventana principal de mesero",
    font=FUENTE_TITULO,
    bg=COLOR_UPBC2,
    fg="#333"
)
titulo.place(relx=0.5, y=20, anchor="n")

subtitulo = tk.Label(
    frame,
    text="Layout de restaurante : área de servicio",
    font=("Segoe UI", 12, "italic"),
    bg=COLOR_UPBC2,
    fg="#555"
)
subtitulo.place(relx=0.5, y=55, anchor="n")

# ========= PANEL IZQUIERDO =========
lbl_meseros = tk.Label(
    frame,
    text="Lista de meseros con pedidos",
    font=FUENTE_TEXTO,
    bg=COLOR_UPBC2,
    fg="#333"
)
lbl_meseros.place(x=80, y=90)

panel_meseros = ctk.CTkFrame(
    frame,
    width=310,
    height=320,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_meseros.place(x=10, y=120)


cols_izq = ("Mesero", "pedido")

tree_izq = ttk.Treeview(
    panel_meseros,
    columns=cols_izq,
    show="headings"
)
tree_izq.heading("Mesero", text="Mesero")
tree_izq.heading("pedido", text="Pedido")

tree_izq.column("Mesero", width=60, anchor="center")
tree_izq.column("pedido", width=60, anchor="w")

tree_izq.place(x=20, y=20, width=260, height=280)

scroll_izq = ttk.Scrollbar(panel_meseros, orient="vertical", command=tree_izq.yview)
scroll_izq.place(x=270, y=20, height=280)
tree_izq.configure(yscrollcommand=scroll_izq.set)

# ========= PANEL DERECHO =========
panel_layout = ctk.CTkFrame(
    frame,
    width=640,
    height=400,
    fg_color=COLOR_PANEL,
    corner_radius=60
)
panel_layout.place(x=360, y=90)

placeholder_layout = tk.Label(
    panel_layout,
    text="Aquí se dibujará el layout\ndel área de servicio, suerte a los del backend xd",
    font=("Segoe UI", 12),
    bg=COLOR_PANEL,
    fg="white",
    justify="center"
)
placeholder_layout.place(relx=0.5, rely=0.5, anchor="center")

# ========= BOTONES INFERIORES (YA USANDO FUNCIÓN) =========
crear_boton(frame, "Crear pedido", 80, 450)
crear_boton(frame, "Cerrar cuenta", 80, 500)
crear_boton(frame, "Modificar pedido", 80, 550)

crear_boton(frame, "Asignación de mesero", 350, 500)
crear_boton(frame, "Generar reporte", 600, 500)

ventana.mainloop()
