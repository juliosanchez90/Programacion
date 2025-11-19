import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# ======================
# CONFIGURACIÓN GENERAL
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO_VENTANA = "#F5F5F5"
COLOR_PANEL = "#820808"      # paneles que luego usará el backend
COLOR_BOTON = "#6A1B9A"
COLOR_BOTON_HOVER = "#8E24AA"
COLOR_UPBC2 = "#FFFFFF"

FUENTE_TITULO = ("Segoe UI", 18, "bold")
FUENTE_TEXTO = ("Segoe UI", 12)

# -------------------------------------------------
# FUNCIÓN GLOBAL PARA CREAR BOTONES
# -------------------------------------------------
def crear_boton(parent, text, x, y, w=200, h=55, cmd=None):
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
# VENTANA MODIFICACIÓN
# ======================
ventana = tk.Tk()
ventana.title("HardTable 1.0 - Modificación de pedidos")
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
tk.Label(
    frame,
    text="Ventana de modificación de pedidos.",
    font=FUENTE_TITULO,
    bg=COLOR_UPBC2,
    fg="#333"
).place(relx=0.5, y=20, anchor="n")

# ========= PANEL IZQUIERDO =========
tk.Label(
    frame,
    text="Detalles de pedido",
    font=FUENTE_TEXTO,
    bg=COLOR_UPBC2,
    fg="#333"
).place(x=160, y=150)

panel_detalles = ctk.CTkFrame(
    frame,
    width=360,
    height=380,
    fg_color=COLOR_PANEL,
    corner_radius=20
)
panel_detalles.place(x=60, y=180)

# ----- TREEVIEW IZQUIERDO (Producto / Cantidad) -----
cols = ("producto", "cantidad")

tree_izq = ttk.Treeview(
    panel_detalles,
    columns=cols,
    show="headings"
)
tree_izq.heading("producto", text="Producto")
tree_izq.heading("cantidad", text="Cantidad")

tree_izq.column("producto", width=220, anchor="w")
tree_izq.column("cantidad", width=80, anchor="center")

# Lo centramos dejando margen para ver el rojo del frame
tree_izq.place(x=10, y=10, width=320, height=340)

scroll_izq = ttk.Scrollbar(
    panel_detalles,
    orient="vertical",
    command=tree_izq.yview
)
scroll_izq.place(x=330, y=10, height=340)

tree_izq.configure(yscrollcommand=scroll_izq.set)

# ZONA BACKEND:
# Aquí el backend llenará la tabla izquierda desde SQL
# tree_izq.insert("", "end", values=("Taco", 3))


# ========= PANEL DERECHO =========
tk.Label(
    frame,
    text="Pedido modificado",
    font=FUENTE_TEXTO,
    bg=COLOR_UPBC2,
    fg="#333"
).place(x=750, y=150)

panel_detalles_mod = ctk.CTkFrame(
    frame,
    width=360,
    height=380,
    fg_color=COLOR_PANEL,
    corner_radius=20
)
panel_detalles_mod.place(x=650, y=180)

# ----- TREEVIEW DERECHO (Producto / Cantidad) -----
tree_der = ttk.Treeview(
    panel_detalles_mod,
    columns=cols,
    show="headings"
)
tree_der.heading("producto", text="Producto")
tree_der.heading("cantidad", text="Cantidad")

tree_der.column("producto", width=220, anchor="w")
tree_der.column("cantidad", width=80, anchor="center")

tree_der.place(x=10, y=10, width=320, height=340)

scroll_der = ttk.Scrollbar(
    panel_detalles_mod,
    orient="vertical",
    command=tree_der.yview
)
scroll_der.place(x=330, y=10, height=340)

tree_der.configure(yscrollcommand=scroll_der.set)

# ZONA BACKEND:
# Aquí el backend pondrá los productos ya modificados
# tree_der.insert("", "end", values=("Taco", 5))

# ========= BOTONES ==========================
crear_boton(frame, "Seleccionar mesa", 80, 80, w=320, h=60)
crear_boton(frame, "Agregar", 430, 230)
crear_boton(frame, "Quitar", 430, 310)
crear_boton(frame, "Nota", 430, 390)
crear_boton(frame, "Guardar cambios", 780, 580, w=220, h=45)

ventana.mainloop()
