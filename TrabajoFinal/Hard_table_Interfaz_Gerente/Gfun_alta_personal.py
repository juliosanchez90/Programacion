import tkinter as tk
import customtkinter as ctk

COLOR_PANEL_ROJO = "#A50000"
COLOR_PANEL_MORADO = "#8A2BE2"
COLOR_BOTON_HOVER = "#9C37FF"

def alta(panel):

    # limpiar panel antes de dibujar
    for widget in panel.winfo_children():
        widget.destroy()

    # Título del formulario
    titulo = tk.Label(
        panel,
        text="Alta de usuario",
        font=("Segoe UI", 20, "bold"),
        bg=COLOR_PANEL_ROJO,
        fg="white"
    )
    titulo.place(relx=0.5, y=40, anchor="center")

    # Campos del formulario
    campos = ["Nombre:", "Rol:", "Usuario:", "Contraseña:"]
    entries = {}
    y_pos = 120

    for campo in campos:
        lbl = tk.Label(
            panel,
            text=campo,
            font=("Segoe UI", 16),
            bg=COLOR_PANEL_ROJO,
            fg="white"
        )
        lbl.place(x=200, y=y_pos)

        entry = ctk.CTkEntry(
            panel,
            width=250,
            height=32,
            fg_color="white",
            text_color="black"
        )
        entry.place(x=330, y=y_pos)

        entries[campo] = entry
        y_pos += 70

    # Botón limpiar
    btn_limpiar = ctk.CTkButton(
        panel,
        text="Limpiar\ncampos",
        font=("Segoe UI", 14, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=150,
        height=60,
        corner_radius=10,
        command=lambda: [e.delete(0, "end") for e in entries.values()]
    )
    btn_limpiar.place(x=350, y=420)

    # Botón crear
    btn_crear = ctk.CTkButton(
        panel,
        text="crear",
        font=("Segoe UI", 14, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=150,
        height=60,
        corner_radius=10,
        #command=lambda: print({k: e.get() for k, e in entries.items()})
    )
    btn_crear.place(x=520, y=420)
