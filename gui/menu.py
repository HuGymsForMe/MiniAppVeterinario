import time
import os
import tkinter as tk

from tkinter import *
from tkinter import messagebox, ttk

from clases.almacen_citas import AlmacenCitas
from clases.almacen_clientes import AlmacenClientes
from clases.almacen_mascotas import AlmacenMascotas

from gui.menu_add_citas import MenuAddCitas
from gui.menu_del_citas import MenuDelCitas
from gui.menu_add_clientes import MenuAddClientes
from gui.menu_add_mascotas import MenuAddMascotas
from gui.menu_del_mascotas import MenuDelMascotas


class VentanaPrincipal:
    def __init__(self, master):
        '''DE PRIMERAS INCLUÍ LA OPCIÓN DE BORRAR CLIENTES (QUE A SU VEZ BORRARÍA LAS CITAS Y LAS MASCOTAS DE ESE CLIENTE) 
        PERO LA ACABE VIENDO INNECESARIA Y DEMASIADO ENGORROSA, ADEMÁS QUE LA FUNCIÓN DE BORRADO ES MUCHO MAS SENCILLA
        CON LA SENTENCIA SQL 'ON DELETE CASCADE' '''
        self.SOBREESCRIBIR = "yes"
        self.master = master
        self.master.configure(background="#D5F5E3")
        self.RUTA_IMAGEN = os.path.abspath('../Ej 01-06-2023 (PYTHON)/img/perro.png')
        self.imagen_perro = PhotoImage(file=self.RUTA_IMAGEN)
        #CITAS
        self.almacen_citas = AlmacenCitas(self)
        self.hija1 = MenuAddCitas(self.master, self.almacen_citas)
        self.hija2 = MenuDelCitas(self.master, self.almacen_citas)
        #CLIENTES
        self.almacen_clientes = AlmacenClientes(self)
        self.hija3 = MenuAddClientes(self.master, self.almacen_clientes)
        #MASCOTAS
        self.almacen_mascotas = AlmacenMascotas(self)
        self.hija4 = MenuAddMascotas(self.master, self.almacen_mascotas)
        self.hija5 = MenuDelMascotas(self.master, self.almacen_mascotas)
        self.master.deiconify()
        self.master.minsize(600, 600)
        self.master.geometry("600x600+850+100")
        self.master.maxsize(600, 600)
        self.master.title("APLICACIÓN VETERINARIO")
        self._title_veterinario = ttk.Label(self.master, text="OPCIONES", font=("Helvetica", 14), background="#D5F5E3")
        self._imagen_veterinario = ttk.Label(self.master, image=self.imagen_perro, background="#D5F5E3")
        self._boton_citas = ttk.Button(self.master, text="AÑADIR CITA", command=self.abrir_menu_add_citas)
        self._boton_del_citas = ttk.Button(self.master, text="BORRAR CITA", command=self.abrir_menu_del_citas)
        self._boton_clientes = ttk.Button(self.master, text="AÑADIR CLIENTE", command=self.abrir_menu_add_clientes)
        self._boton_mascotas = ttk.Button(self.master, text="AÑADIR MASCOTA", command=self.abrir_menu_add_mascotas)
        self._boton_del_mascotas = ttk.Button(self.master, text="BORRAR MASCOTA", command=self.abrir_menu_del_mascotas)
        self._boton_sobreescribir = ttk.Button(self.master, text="GUARDAR LOS DATOS", command=self.sobreescribir_datos)
        self._boton_sobreescribir_salir = ttk.Button(self.master, text="SALIR Y GUARDAR", command=self.mostrar_ulitmo_aviso)
        self._title_veterinario.pack(side=TOP, padx=20, pady=5)
        self._imagen_veterinario.pack(side=TOP, padx=20)
        self._boton_citas.pack(side=TOP, fill=BOTH, expand=True, 
                                padx=10, pady=5)
        self._boton_del_citas.pack(side=TOP, fill=BOTH, expand=True, 
                                padx=10, pady=5)
        self._boton_clientes.pack(side=TOP, fill=BOTH, expand=True, 
                                padx=10, pady=5)
        self._boton_mascotas.pack(side=TOP, fill=BOTH, expand=True, 
                                padx=10, pady=5)
        self._boton_del_mascotas.pack(side=TOP, fill=BOTH, expand=True, 
                                padx=10, pady=5)
        self._boton_sobreescribir.pack(side=TOP, fill=BOTH, expand=True, 
                                padx=10, pady=5)
        self._boton_sobreescribir_salir.pack(side=TOP, fill=BOTH, expand=True, 
                                padx=10, pady=5)

    def ocultar_menu(self):
        self.master.withdraw()

    def abrir_menu_add_citas(self):
        self.ocultar_menu()
        self.hija1.mostrar_menu()
    
    def abrir_menu_del_citas(self):
        self.ocultar_menu()
        self.hija2.mostrar_menu()
    
    def abrir_menu_add_clientes(self):
        self.ocultar_menu()
        self.hija3.mostrar_menu()
    
    def abrir_menu_add_mascotas(self):
        self.ocultar_menu()
        self.hija4.mostrar_menu()
    
    def abrir_menu_del_mascotas(self):
        self.ocultar_menu()
        self.hija5.mostrar_menu()

    def sobreescribir_datos(self):
        self.almacen_citas.sobreescribir_citas()
        self.almacen_clientes.sobreescribir_clientes()
        self.almacen_mascotas.sobreescribir_mascotas()

    def mostrar_ulitmo_aviso(self):
        advertencia = messagebox.askyesnocancel(message="¿DESEA SALIR Y SOBREESCRIBIR LOS CAMBIOS REALIZADOS?")
        if self.SOBREESCRIBIR:
            self.almacen_citas.sobreescribir_citas()
            self.almacen_clientes.sobreescribir_clientes()
            self.almacen_mascotas.sobreescribir_mascotas()
            self.master.destroy()

    
        