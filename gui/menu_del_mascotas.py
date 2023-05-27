import abc
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from clases.almacen_mascotas import AlmacenMascotas

class MenuDelMascotas(tk.Toplevel):
    def __init__(self, master, almacen_mascotas):
        self.almacen_mascotas = almacen_mascotas
        super().__init__(master)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close) 
        self.minsize(200, 100)
        self.geometry("200x100+675+100")
        self.maxsize(200, 100)
        self.print_del_mascota = ttk.Label(self, text="ID DE MASCOTA:")
        self.input_del_mascota = ttk.Entry(self)
        self.boton_del_mascota = ttk.Button(self, text="BORRAR MASCOTA", command=self.tratar_del_mascotas)
    
    def visualizar_menu_principal(self):
        self.destroy
        self.withdraw()
        self.master.deiconify()
    
    def mostrar_menu(self):
        self.deiconify()
        self.print_del_mascota.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_del_mascota.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_mascota.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

    def tratar_del_mascotas(self):
        dato_borrar_mascota = self.input_del_mascota.get() 
        if (self.almacen_mascotas.del_mascota(dato_borrar_mascota)):
            mascota_cancel = messagebox.showinfo(message="MASCOTA ELIMINADA CON ÉXITO")
        else:
            mascota_not_found = messagebox.showinfo(message="MASCOTA NO ENCONTRADA EN EL SISTEMA")

    def on_close(self):
        self.withdraw()
        self.master.deiconify()
