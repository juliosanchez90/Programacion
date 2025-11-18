import tkinter as tk
from tkinter import ttk, simpledialog

CANVAS_W, CANVAS_H = 900, 540
GRID_SIZE = 24  # pon 0 si no quieres snap a la grilla

def snap(v, g=GRID_SIZE):
    return round(v / g) * g if g else v

class Mesa:
    def __init__(self, x, y, horizontal=True, numero=""):
        self.x, self.y = x, y               # centro
        self.horizontal = horizontal
        self.numero = numero
        self.ancho_h, self.alto_h = 100, 60 # tamaño horizontal
        self.ancho_v, self.alto_v = 60, 100 # tamaño vertical
        self.tag = None

    @property
    def size(self):
        return (self.ancho_h, self.alto_h) if self.horizontal else (self.ancho_v, self.alto_v)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Layout Mesas (simple)")
        self.geometry(f"{CANVAS_W+180}x{CANVAS_H+10}")
        self.mesas = []
        self.seleccion = None
        self.drag = None
        self.contador = 1

        self._ui()
        self._binds()
        self._grid()

    def _ui(self):
        side = ttk.Frame(self, padding=8)
        side.pack(side="left", fill="y")

        ttk.Button(side, text="Agregar mesa", command=self.agregar_mesa).pack(fill="x", pady=4)

        ttk.Label(side, text="Siguiente número").pack(anchor="w", pady=(8,2))
        self.var_next = tk.IntVar(value=self.contador)
        ttk.Spinbox(side, from_=1, to=9999, textvariable=self.var_next, width=6).pack(anchor="w")

        ttk.Separator(side).pack(fill="x", pady=8)
        ttk.Label(side, text="Atajos:", foreground="#666").pack(anchor="w")
        ttk.Label(
            side,
            text="Arrastrar: mover\nDoble clic: rotar\nR: rotar\nSupr: borrar\nClic derecho: número",
            foreground="#666", justify="left"
        ).pack(anchor="w")

        self.canvas = tk.Canvas(self, width=CANVAS_W, height=CANVAS_H, bg="#f7f9fc", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

    def _binds(self):
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Double-1>", self.on_double)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.bind("<Delete>", self.borrar)
        self.bind("<Key-r>", self.rotar)
        self.bind("<Key-R>", self.rotar)

    def _grid(self):
        self.canvas.delete("grid")
        if GRID_SIZE:
            for x in range(0, CANVAS_W, GRID_SIZE):
                self.canvas.create_line(x, 0, x, CANVAS_H, fill="#e6ebf2", tags="grid")
            for y in range(0, CANVAS_H, GRID_SIZE):
                self.canvas.create_line(0, y, CANVAS_W, y, fill="#e6ebf2", tags="grid")

    # ----- Mesas -----
    def agregar_mesa(self):
        x, y = snap(CANVAS_W//2), snap(CANVAS_H//2)
        numero = str(self.var_next.get())
        self.var_next.set(self.var_next.get()+1)
        mesa = Mesa(x, y, horizontal=True, numero=numero)
        self.mesas.append(mesa)
        self.dibujar_mesa(len(self.mesas)-1, select=True)

    def dibujar_mesa(self, idx, select=False):
        m = self.mesas[idx]
        if m.tag:
            self.canvas.delete(m.tag)
        tag = f"mesa:{idx}"
        m.tag = tag
        w, h = m.size
        x0, y0, x1, y1 = m.x - w//2, m.y - h//2, m.x + w//2, m.y + h//2

        self.canvas.create_rectangle(x0, y0, x1, y1, fill="#ffffff", outline="#444", width=2, tags=(tag, "mesa"))
        self.canvas.create_text(m.x, m.y, text=m.numero, font=("Segoe UI", 12, "bold"),
                                fill="#111", tags=(tag, "mesa"))

        # borde de selección
        if select:
            self.seleccion = idx
            self.canvas.create_rectangle(x0-4, y0-4, x1+4, y1+4, outline="#2563eb", width=2, dash=(3,2),
                                         tags=(tag, "sel"))
        else:
            self.canvas.dtag(tag, "sel")

    def redibujar_todo(self):
        self.canvas.delete("mesa")
        for i in range(len(self.mesas)):
            self.dibujar_mesa(i, select=(i == self.seleccion))

    # ----- Utilidades selección -----
    def pick_idx(self, event):
        item = self.canvas.find_withtag("current")
        if not item:
            return None
        for t in self.canvas.gettags(item):
            if t.startswith("mesa:"):
                return int(t.split(":")[1])
        return None

    # ----- Eventos -----
    def on_press(self, event):
        # da foco al canvas para que reciba las teclas
        self.canvas.focus_set()

        idx = self.pick_idx(event)
        self.seleccion = idx
        if idx is not None:
            m = self.mesas[idx]
            self.drag = (event.x, event.y, m.x, m.y)
        else:
            self.drag = None
        self.redibujar_todo()

    def on_drag(self, event):
        if self.seleccion is None or self.drag is None:
            return
        sx, sy, ox, oy = self.drag
        dx, dy = event.x - sx, event.y - sy
        m = self.mesas[self.seleccion]
        m.x, m.y = ox + dx, oy + dy
        self.dibujar_mesa(self.seleccion, select=True)

    def on_release(self, event):
        if self.seleccion is not None and GRID_SIZE:
            m = self.mesas[self.seleccion]
            m.x, m.y = snap(m.x), snap(m.y)
            self.dibujar_mesa(self.seleccion, select=True)
        self.drag = None

    def on_double(self, event):
        idx = self.pick_idx(event)
        if idx is None:
            return
        self.mesas[idx].horizontal = not self.mesas[idx].horizontal
        self.seleccion = idx
        self.dibujar_mesa(idx, select=True)

    def on_right_click(self, event):
        idx = self.pick_idx(event)
        if idx is None:
            return
        m = self.mesas[idx]
        nuevo = simpledialog.askstring("Número de mesa", "Número:", initialvalue=m.numero, parent=self)
        if nuevo is None:
            return
        m.numero = nuevo.strip()
        self.seleccion = idx
        self.dibujar_mesa(idx, select=True)

    def rotar(self, event=None):
        """Rotar la mesa seleccionada (atajo con tecla R)."""
        if self.seleccion is None:
            return "break"
        m = self.mesas[self.seleccion]
        m.horizontal = not m.horizontal
        self.dibujar_mesa(self.seleccion, select=True)
        return "break"

    def borrar(self, event=None):
        if self.seleccion is None:
            return "break"
        self.canvas.delete(self.mesas[self.seleccion].tag)
        del self.mesas[self.seleccion]
        self.seleccion = None
        self.redibujar_todo()
        return "break"

if __name__ == "__main__":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
    App().mainloop()
