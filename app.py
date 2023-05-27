import tkinter as tk

from gui.menu import VentanaPrincipal

class Programa:
    def __init__(self):
        self.root = tk.Tk()
        self.menu = VentanaPrincipal(self.root)

    def main(self):
        self.menu.almacen_citas.cargar_citas()
        self.menu.almacen_clientes.cargar_clientes()
        self.menu.almacen_mascotas.cargar_mascotas()
        self.root.mainloop()

if __name__ == "__main__":
    Programa().main()