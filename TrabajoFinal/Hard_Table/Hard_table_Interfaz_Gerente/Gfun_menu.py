import tkinter as tk
import customtkinter as ctk

# Colores iguales a los del gerente
COLOR_PANEL_ROJO = "#A50000"
COLOR_PANEL_MORADO = "#8A2BE2"
COLOR_BOTON_HOVER = "#9C37FF"


def panel_modificar_menu(panel):
    """
    Dibuja en 'panel' la interfaz de MODIFICAR MENÚ.
    El backend luego podrá leer/escribir en los Entry y
    llenar la lista de productos.
    """

    # 1) Limpiar todo lo que hubiera antes en el panel
    for widget in panel.winfo_children():
        widget.destroy()

    # ============================
    # SECCIÓN: CREAR NUEVO PRODUCTO
    # ============================
    marco_crear = tk.LabelFrame(
        panel,
        text="Crear nuevo producto",
        font=("Segoe UI", 16, "bold"),
        bg=COLOR_PANEL_ROJO,
        fg="white",
        bd=2,
        relief="solid",
        labelanchor="n"
    )
    marco_crear.place(x=40, y=40, width=380, height=260)

    # Labels y Entries
    etiquetas = ["producto:", "precio:", "categoría:", "disponible:"]
    entries_crear = {}
    y_pos = 20

    for texto in etiquetas:
        lbl = tk.Label(
            marco_crear,
            text=texto,
            font=("Segoe UI", 14),
            bg=COLOR_PANEL_ROJO,
            fg="white"
        )
        lbl.place(x=20, y=y_pos)

        entry = ctk.CTkEntry(
            marco_crear,
            width=200,
            height=28,
            fg_color="white",
            text_color="black"
        )
        entry.place(x=130, y=y_pos)

        entries_crear[texto] = entry
        y_pos += 40

    # Botones limpiar / crear
    btn_limpiar = ctk.CTkButton(
        marco_crear,
        text="limpiar",
        font=("Segoe UI", 14, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=110,
        height=40,
        corner_radius=8,
        # backend luego puede poner aquí la lógica
        #command=lambda: [e.delete(0, "end") for e in entries_crear.values()]
    )
    btn_limpiar.place(x=60, y=180)

    btn_crear = ctk.CTkButton(
        marco_crear,
        text="crear",
        font=("Segoe UI", 14, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=110,
        height=40,
        corner_radius=8,
        #command=lambda: print("Crear producto:", {k: e.get() for k, e in entries_crear.items()})
    )
    btn_crear.place(x=200, y=180)

    # ============================
    # SECCIÓN: LISTA DE PRODUCTOS
    # ============================
    lbl_lista = tk.Label(
        panel,
        text="Lista de productos",
        font=("Segoe UI", 16, "bold"),
        bg=COLOR_PANEL_ROJO,
        fg="white"
    )
    lbl_lista.place(x=470, y=40)

    # Listbox donde luego el backend cargará datos desde SQL
    marco_lista = tk.Frame(
        panel,
        bg=COLOR_PANEL_ROJO,
        bd=1,
        relief="solid"
    )
    marco_lista.place(x=470, y=70, width=330, height=260)

    listbox_productos = tk.Listbox(
        marco_lista,
        font=("Segoe UI", 11),
        bg="white",
        fg="black",
        selectbackground="#D5B0FF",
        activestyle="none"
    )
    listbox_productos.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(marco_lista, orient="vertical", command=listbox_productos.yview)
    scrollbar.pack(side="right", fill="y")
    listbox_productos.config(yscrollcommand=scrollbar.set)

    # ============================
    # BOTONES DE FILTRO / ORDEN (derecha abajo)
    # ============================
    btn_precio = ctk.CTkButton(
        panel,
        text="$",
        font=("Segoe UI", 13, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=50,
        height=35,
        corner_radius=8
    )
    btn_precio.place(x=470, y=340)

    btn_nombre = ctk.CTkButton(
        panel,
        text="Nom",
        font=("Segoe UI", 13, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=70,
        height=35,
        corner_radius=8
    )
    btn_nombre.place(x=530, y=340)

    btn_cls = ctk.CTkButton(
        panel,
        text="Cls",
        font=("Segoe UI", 13, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=70,
        height=35,
        corner_radius=8
    )
    btn_cls.place(x=610, y=340)

    btn_est = ctk.CTkButton(
        panel,
        text="Est",
        font=("Segoe UI", 13, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=70,
        height=35,
        corner_radius=8
    )
    btn_est.place(x=470, y=385)

    # ============================
    # SECCIÓN: ESTADO PRODUCTO
    # ============================
    lbl_estado = tk.Label(
        panel,
        text="Estado producto",
        font=("Segoe UI", 14, "bold"),
        bg=COLOR_PANEL_ROJO,
        fg="white"
    )
    lbl_estado.place(x=40, y=320)

    lbl_id_estado = tk.Label(
        panel,
        text="ID :",
        font=("Segoe UI", 13),
        bg=COLOR_PANEL_ROJO,
        fg="white"
    )
    lbl_id_estado.place(x=40, y=350)

    entry_estado_id = ctk.CTkEntry(
        panel,
        width=80,
        height=28,
        fg_color="white",
        text_color="black"
    )
    entry_estado_id.place(x=80, y=352)

    btn_onoff = ctk.CTkButton(
        panel,
        text="On/Off",
        font=("Segoe UI", 13, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=90,
        height=32,
        corner_radius=8
    )
    btn_onoff.place(x=180, y=348)

    # ============================
    # SECCIÓN: ELIMINAR PRODUCTO
    # ============================
    marco_eliminar = tk.LabelFrame(
        panel,
        text="ELIMINAR PRODUCTO",
        font=("Segoe UI", 14, "bold"),
        bg=COLOR_PANEL_ROJO,
        fg="white",
        bd=2,
        relief="solid",
        labelanchor="n"
    )
    marco_eliminar.place(x=40, y=390, width=320, height=110)

    lbl_id_del = tk.Label(
        marco_eliminar,
        text="ID :",
        font=("Segoe UI", 13),
        bg=COLOR_PANEL_ROJO,
        fg="white"
    )
    lbl_id_del.place(x=20, y=40)

    entry_del_id = ctk.CTkEntry(
        marco_eliminar,
        width=80,
        height=28,
        fg_color="white",
        text_color="black"
    )
    entry_del_id.place(x=60, y=40)

    btn_delete = ctk.CTkButton(
        marco_eliminar,
        text="DELETE",
        font=("Segoe UI", 13, "bold"),
        fg_color=COLOR_PANEL_MORADO,
        hover_color=COLOR_BOTON_HOVER,
        text_color="white",
        width=100,
        height=32,
        corner_radius=8
    )
    btn_delete.place(x=160, y=38)
