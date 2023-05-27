import abc
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from clases.validator import Validator
from clases.almacen_clientes import AlmacenClientes

class MenuAddClientes(tk.Toplevel):
    def __init__(self, master, almacen_clientes):
        self.almacen_clientes = almacen_clientes
        self.validador = Validator()
        super().__init__(master)
        self.withdraw()
        self.title("AÑADIR CLIENTE")
        self.minsize(350, 320)
        self.geometry("350x320+600+100")
        self.maxsize(350, 320)
        self.protocol("WM_DELETE_WINDOW", self.on_close) 
        self.MESSAGEBOX = "yes"
        #VALORES PLACEHOLDERS
        self.PLACEHOLDER_DNI = "Ej: 00000000B"
        self.PLACEHOLDER_NOMBRE = "Nombre:"
        self.PLACEHOLDER_APELLIDOS = "Apellidos:"
        self.PLACEHOLDER_TELEFONO = "Nº Teléfono:"
        self.print_dni = ttk.Label(self, text="DNI: ", font=("Helvetica", 12))
        self.print_nombre = ttk.Label(self, text="NOMBRE: ", font=("Helvetica", 12))
        self.print_apellidos = ttk.Label(self, text="APELLIDOS: ", font=("Helvetica", 12))
        self.print_telefono = ttk.Label(self, text="TELEFONO: ", font=("Helvetica", 12))
        self.input_dni = ttk.Entry(self, foreground="gray")
        self.input_dni.insert(0, self.PLACEHOLDER_DNI)
        self.input_dni.bind('<FocusIn>', self.clear_placeholder_input_dni)
        self.input_dni.bind('<FocusOut>', self.set_placeholder_input_dni)
        self.input_nombre = ttk.Entry(self, foreground="gray")
        self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
        self.input_nombre.bind('<FocusIn>', self.clear_placeholder_input_nombre)
        self.input_nombre.bind('<FocusOut>', self.set_placeholder_input_nombre)
        self.input_apellidos = ttk.Entry(self, foreground="gray")
        self.input_apellidos.insert(0, self.PLACEHOLDER_APELLIDOS)
        self.input_apellidos.bind('<FocusIn>', self.clear_placeholder_input_apellidos)
        self.input_apellidos.bind('<FocusOut>', self.set_placeholder_input_apellidos)
        self.input_telefono = ttk.Entry(self, foreground="gray")
        self.input_telefono.insert(0, self.PLACEHOLDER_TELEFONO)
        self.input_telefono.bind('<FocusIn>', self.clear_placeholder_input_telefono)
        self.input_telefono.bind('<FocusOut>', self.set_placeholder_input_telefono)
        self.boton_guardar_clientes = ttk.Button(self, text="AÑADIR CLIENTE", command=self.comprobar_clientes)
    
    def visualizar_menu_principal(self):
        self.destroy
        self.withdraw()
        self.master.deiconify()

    def mostrar_menu(self):
        self.deiconify() #VISUALIZAMOS LA PANTALLA DE CLIENTES
        self.print_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_apellidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_apellidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_guardar_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def recoger_datos_clientes(self):
        dato_dni = self.input_dni.get().upper()
        dato_nombre = self.input_nombre.get().upper()
        dato_apellidos = self.input_apellidos.get().upper()
        dato_telefono = self.input_telefono.get()
        return dato_dni, dato_nombre, dato_apellidos, dato_telefono

    def comprobar_clientes(self):
        dato_dni, dato_nombre, dato_apellidos, dato_telefono = self.recoger_datos_clientes()
        if (self.validador.validador_dni(dato_dni)) and (self.validador.validador_telefono(dato_telefono)) and dato_nombre != '' and dato_apellidos != '':
            messagebox.askyesno(message=f"DATOS:\nDNI: {dato_dni}\nNOMBRE: {dato_nombre}\nAPELLIDOS: {dato_apellidos}\nTELEFONO: {dato_telefono}")
            if self.MESSAGEBOX:
                if (self.almacen_clientes.add_clientes(dato_dni, dato_nombre, dato_apellidos, dato_telefono)):
                    messagebox.showinfo(message="CLIENTE YA REGISTRADO EN EL SISTEMA")
        else:
            self.mostrar_datos_incorrectos()

    def on_close(self):
        self.withdraw()
        self.master.deiconify()

    #PLACEHOLDERS
    def clear_placeholder_input_dni(self, event):
        if self.input_dni.get() == self.PLACEHOLDER_DNI:
            self.input_dni.delete(0, tk.END)
            self.input_dni.config(foreground='black')

    def set_placeholder_input_dni(self, event):
        if self.input_dni.get() == "":
            self.input_dni.delete(0, tk.END)
            self.input_dni.config(foreground='black')

    def clear_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == self.PLACEHOLDER_NOMBRE:
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.config(foreground='black')

    def set_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == "":
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.config(foreground='black')
        
    def clear_placeholder_input_apellidos(self, event):
        if self.input_apellidos.get() == self.PLACEHOLDER_APELLIDOS:
            self.input_apellidos.delete(0, tk.END)
            self.input_apellidos.config(foreground='black')

    def set_placeholder_input_apellidos(self, event):
        if self.input_apellidos.get() == "":
            self.input_apellidos.delete(0, tk.END)
            self.input_apellidos.config(foreground='black')

    def clear_placeholder_input_telefono(self, event):
        if self.input_telefono.get() == self.PLACEHOLDER_TELEFONO:
            self.input_telefono.delete(0, tk.END)
            self.input_telefono.config(foreground='black')

    def set_placeholder_input_telefono(self, event):
        if self.input_telefono.get() == "":
            self.input_telefono.delete(0, tk.END)
            self.input_telefono.config(foreground='black')

    @staticmethod
    def mostrar_datos_incorrectos():
        advertencia = messagebox.showinfo(message="DATOS INCORRECTOS")


