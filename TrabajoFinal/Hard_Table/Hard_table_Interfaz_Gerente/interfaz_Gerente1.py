import tkinter as tk
import customtkinter as ctk
from Gfun_alta_personal import alta
from Gfun_menu import panel_modificar_menu
# ======================
# CONFIG GENERAL
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO = "#F5F5F5"
COLOR_PANEL_ROJO = "#A50000"       # rojo para panel lateral y panel grande
COLOR_PANEL_MORADO = "#8A2BE2"     # morado botones
COLOR_BOTON_HOVER = "#9C37FF"
COLOR_TEXTO = "white"

FUENTE_TITULO = ("Segoe UI", 20, "bold")
FUENTE_BOTON = ("Segoe UI", 16, "bold")
FUENTE_NORMAL = ("Segoe UI", 12)

# ======================
# VENTANA GERENTE
# ======================
ventana = tk.Tk()
ventana.title("HardTable - Gerente")
ventana.geometry("1200x700")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(False, False)

# Centrar ventana
ventana.update_idletasks()
w = ventana.winfo_width()
h = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (w // 2)
y = (ventana.winfo_screenheight() // 2) - (h // 2)
ventana.geometry(f"{w}x{h}+{x}+{y}")

# ===================================================
# PANEL IZQUIERDO (LATERAL ROJO)
# ===================================================
panel_lateral = tk.Frame(
    ventana,
    bg=COLOR_PANEL_ROJO,
    width=330,
    height=700
)
panel_lateral.place(x=0, y=0)

# Título del panel
titulo = tk.Label(
    panel_lateral,
    text="Gerente Hard Table",
    font=("Segoe UI", 18, "bold"),
    bg=COLOR_PANEL_ROJO,
    fg="white"
)
titulo.place(relx=0.5, y=40, anchor="center")

# ===================================================
# PANEL PRINCIPAL (ROJO)  ⬅️ LO SUBIMOS ARRIBA
# ===================================================
panel_principal = ctk.CTkFrame(
    ventana,
    width=820,
    height=520,
    corner_radius=30,
    bg_color=COLOR_PANEL_ROJO,
    fg_color=COLOR_PANEL_ROJO
)
panel_principal.place(x=360, y=80)

texto_principal = ctk.CTkLabel(
    panel_principal,
    text="🍒😘",
    font=("Segoe UI", 16),
    text_color="white",
    fg_color="transparent"
)
texto_principal.place(relx=0.5, rely=0.5, anchor="center")

# ===================================================
# BOTONES LATERALES (MORADOS)
# ===================================================
def crear_boton(text, y, cmd=None):
    btn = ctk.CTkButton(
        panel_lateral,
        text=text,
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        font=FUENTE_BOTON,
        corner_radius=8,
        width=280,
        height=70,
        command=cmd   # ✅ ahora sí usa el comando
    )
    btn.place(x=25, y=y)
    return btn

# Botones
crear_boton("Alta\nPersonal", 100, cmd=lambda: alta(panel_principal))
crear_boton("Modificar menú", 200, cmd=lambda: panel_modificar_menu(panel_principal))
crear_boton("LayOut", 300)
crear_boton("Lista de empleados", 400)
crear_boton("Baja\nPersonal", 500)

# ===================================================
# BOTÓN SALIR (ABAJO DERECHA)
# ===================================================
btn_salir = ctk.CTkButton(
    ventana,
    text="Salir",
    font=FUENTE_BOTON,
    fg_color=COLOR_PANEL_MORADO,
    hover_color=COLOR_BOTON_HOVER,
    text_color="white",
    corner_radius=10,
    width=200,
    height=60,
    command=ventana.destroy
)
btn_salir.place(x=880, y=620)

ventana.mainloop()
