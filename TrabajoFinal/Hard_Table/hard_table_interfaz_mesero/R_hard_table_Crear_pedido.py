import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# ======================
# CONFIGURACIÓN GENERAL
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO_VENTANA = "#F5F5F5"
COLOR_PANEL = "#820808"      # paneles backend
COLOR_BOTON = "#6A1B9A"
COLOR_BOTON_HOVER = "#8E24AA"
COLOR_UPBC2 = "#FFFFFF"

FUENTE_TITULO = ("Segoe UI", 18, "bold")
FUENTE_TEXTO = ("Segoe UI", 12)

# -------------------------------------------------
# FUNCIÓN GLOBAL PARA CREAR BOTONES
# -------------------------------------------------
def crear_boton(parent, text, x, y, w=130, h=40, cmd=None):
    btn = ctk.CTkButton(
        parent,
        text=text,
        font=("Segoe UI", 14, "bold"),
        fg_color=COLOR_BOTON,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        corner_radius=10,
        width=w,
        height=h,
        command=cmd
    )
    btn.place(x=x, y=y)
    return btn


# ======================
# VENTANA CREAR PEDIDO
# ======================
ventana = tk.Tk()
ventana.title("HardTable 1.0 - Crear pedido")
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
    text="Crear orden",
    font=FUENTE_TITULO,
    bg=COLOR_UPBC2,
    fg="#333"
)
titulo.place(relx=0.5, y=20, anchor="n")

subtitulo = tk.Label(
    frame,
    text="aqui poner el numero de mesa.",
    font=("Segoe UI", 13, "italic"),
    bg=COLOR_UPBC2,
    fg="#555"
)
subtitulo.place(relx=0.5, y=55, anchor="n")

# ========= PANEL IZQUIERDO (MENÚ) =========
lbl_menu = tk.Label(
    frame,
    text="Lista de menú.",
    font=FUENTE_TEXTO,
    bg=COLOR_UPBC2,
    fg="#333"
)
lbl_menu.place(x=80, y=100)

panel_menu = ctk.CTkFrame(
    frame,
    width=330,
    height=400,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_menu.place(x=20, y=130)

# TreeView izquierdo
cols_izq = ("disponible", "producto", "precio")

tree_izq = ttk.Treeview(
    panel_menu,
    columns=cols_izq,
    show="headings"
)
tree_izq.heading("disponible", text="Disponible")
tree_izq.heading("producto", text="Producto")
tree_izq.heading("precio", text="Precio")

tree_izq.column("disponible", width=60, anchor="center")
tree_izq.column("producto", width=140, anchor="w")
tree_izq.column("precio", width=50, anchor="center")

tree_izq.place(x=10, y=10, width=300, height=380)

scroll_izq = ttk.Scrollbar(panel_menu, orient="vertical", command=tree_izq.yview)
scroll_izq.place(x=300, y=10, height=380)
tree_izq.configure(yscrollcommand=scroll_izq.set)



# ========= PANEL CENTRAL (Cuenta / Producto agregado) =========
panel_info = ctk.CTkFrame(
    frame,
    width=520,
    height=400,
    fg_color=COLOR_PANEL,
    corner_radius=10
)
panel_info.place(x=360, y=130)

cols_der = ("cantidad", "producto")

tree_der = ttk.Treeview(
    panel_info,
    columns=cols_der,
    show="headings"
)
tree_der.heading("cantidad", text="Cantidad")
tree_der.heading("producto", text="Producto")

tree_der.column("cantidad", width=40, anchor="center")
tree_der.column("producto", width=140, anchor="w")

tree_der.place(x=10, y=10, width=250, height=380)

scroll_der = ttk.Scrollbar(panel_info, orient="vertical", command=tree_der.yview)
scroll_der.place(x=260, y=10, height=380)
tree_der.configure(yscrollcommand=scroll_der.set)

# ==== TEXTBOX DE NOTAS (grande) ====
txt_notas = ctk.CTkTextbox(
    panel_info,
    width=225,      # equivalente aproximado al width=25 de tk.Text
    height=260,     # equivalente aproximado al height=10
    corner_radius=10,
    border_width=2,
    border_color="#6A1B9A",
    fg_color="white",
    text_color="black",
    font=("Segoe UI", 12)
)
txt_notas.place(x=285, y=35)
lbl_notas = ctk.CTkLabel(
    panel_info,
    text="Notas del pedido:",
    font=FUENTE_TEXTO,
    text_color="white",      # color del texto dentro del panel rojo
    fg_color="transparent"   # para que el fondo se funda con el CTkFrame
)
lbl_notas.place(x=285, y=5)
lbl_total = ctk.CTkLabel(
    panel_info,
    text="Total:",
    font=FUENTE_TEXTO,
    text_color="white",      # color del texto dentro del panel rojo
    fg_color="transparent"   # para que el fondo se funda con el CTkFrame
)
lbl_total.place(x=285,y=300 )

lbl_numeros = ctk.CTkLabel(
    panel_info,
    text="????",
    font=FUENTE_TEXTO,
    text_color="white",      # color del texto dentro del panel rojo
    fg_color="transparent"   # para que el fondo se funda con el CTkFrame
)
lbl_numeros.place(x=330,y=300 )
# ===== BOTONES DERECHA =====

crear_boton(frame, "Confirmar\npedido", 900, 470, w=120, h=60)
# ===== BOTONES IZQUIERDOS =====
crear_boton(frame, "Agregar", 50, 550)
crear_boton(frame, "Quitar", 190, 550)

ventana.mainloop()
