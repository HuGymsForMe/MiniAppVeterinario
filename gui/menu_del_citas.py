import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from clases.almacen_citas import AlmacenCitas

class MenuDelCitas(tk.Toplevel):
    def __init__(self, master, almacen_citas):
        self.almacen_citas = almacen_citas
        super().__init__(master)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close) 
        self.title("BORRAR CITA")
        self.minsize(200, 100)
        self.geometry("200x100+675+100")
        self.maxsize(200, 100)
        self.print_del_citas = ttk.Label(self, text="ID DE CITA:")
        self.input_del_citas = ttk.Entry(self)
        self.boton_del_citas = ttk.Button(self, text="BORRAR CITA", command=self.tratar_del_citas)

    def visualizar_menu_principal(self):
        self.destroy
        self.withdraw()
        self.master.deiconify()

    def mostrar_menu(self):
        self.deiconify()
        self.print_del_citas.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_del_citas.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_citas.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def tratar_del_citas(self):
        dato_borrar_cita = self.input_del_citas.get()
        if (self.almacen_citas.del_citas(dato_borrar_cita)):
            cita_cancel = messagebox.showinfo(message="CITA CANCELADA")
        else:
            cita_not_found = messagebox.showinfo(message="CITA NO ENCONTRADA EN EL SISTEMA")

    def on_close(self):
        self.withdraw()
        self.master.deiconify()
