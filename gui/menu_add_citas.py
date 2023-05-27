import abc
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from clases.almacen_citas import AlmacenCitas
from clases.validator import Validator

class MenuAddCitas(tk.Toplevel):
    def __init__(self, master, almacen_citas):
        self.almacen_citas = almacen_citas
        self.validador = Validator()
        super().__init__(master)
        self.MESSAGEBOX = "yes"
        #VALORES PLACEHOLDERS
        self.PLACEHOLDER_FECHA = "DD/MM/YYYY"
        self.PLACEHOLDER_DNI = "Ej: 00000000B"
        self.PLACEHOLDER_ESTABLECIMIENTO = "Ej: SEGOVIA"
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close) 
        self.formato_hora = time.strftime("%I:%M")
        self.fecha_seleccionada= tk.StringVar()
        self.hora_seleccionada = tk.StringVar(value=self.formato_hora)
        self.establecimiento_seleccionado = tk.StringVar()
        self.title("PEDIR CITA")
        self.minsize(450, 300)
        self.geometry("450x300+600+150")
        self.maxsize(450, 300)
        self.print_fecha_cita = ttk.Label(self, text="FECHA DE LA CITA: ", font=("Helvetica", 12))
        self.input_fecha_cita = ttk.Entry(self, foreground="gray", textvariable=self.fecha_seleccionada)
        self.input_fecha_cita.insert(0, self.PLACEHOLDER_FECHA)
        self.input_fecha_cita.bind('<FocusIn>', self.clear_placeholder_fecha_input)
        self.input_fecha_cita.bind('<FocusOut>', self.set_placeholder_fecha_input)
        self.print_hora = ttk.Label(self, text="HORA DE LA CITA: ", font=("Helvetica", 12))
        self.horas_posibles = [ "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"]
        self.eleccion_hora = ttk.Combobox(self, textvariable=self.hora_seleccionada, values=self.horas_posibles)
        self.print_establecimiento = ttk.Label(self, text="ESTABLECIMIENTO: ", font=("Helvetica", 12))
        self.establecimientos_posibles = ['GUADALAJARA', 'MADRID', 'SORIA', 'SEGOVIA']
        self.eleccion_establecimiento = ttk.Combobox(self, textvariable=self.establecimiento_seleccionado, values=self.establecimientos_posibles, foreground="gray")
        self.eleccion_establecimiento.insert(0, self.PLACEHOLDER_ESTABLECIMIENTO)
        self.eleccion_establecimiento.bind('<FocusIn>', self.clear_placeholder_eleccion_establecimiento)
        self.eleccion_establecimiento.bind('<FocusOut>', self.set_placeholder_eleccion_establecimiento)
        self.print_dni = ttk.Label(self, text="DNI: ", font=("Helvetica", 12))
        self.input_dni = ttk.Entry(self, foreground="gray")
        self.input_dni.insert(0, self.PLACEHOLDER_DNI)
        self.input_dni.bind('<FocusIn>', self.clear_placeholder_dni_input)
        self.input_dni.bind('<FocusOut>', self.set_placeholder_dni_input)
        self.boton_guardar_citas = ttk.Button(self, text="AÑADIR CITA", command=self.comprobar_citas)  

    def visualizar_menu_principal(self):
        self.destroy
        self.withdraw()
        self.master.deiconify()

    def mostrar_menu(self):
        self.deiconify()
        self.print_fecha_cita.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_fecha_cita.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_hora.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_hora.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_establecimiento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_establecimiento.pack(side=TOP, expand=True, padx=10, pady=2)
        self.print_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_guardar_citas.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def recoger_datos_citas(self):
        dato_fecha = self.fecha_seleccionada.get()
        dato_hora = self.hora_seleccionada.get()
        dato_establecimiento = self.establecimiento_seleccionado.get()
        dato_cod_cita = f"{dato_fecha[:2]}{dato_hora[:2]}{dato_establecimiento[:3]}"
        dato_dni = self.input_dni.get().upper()
        return dato_cod_cita, dato_fecha, dato_hora, dato_establecimiento, dato_dni

    def comprobar_citas(self):
        '''NO ES NECESARIO UN DNI VÁLIDADO YA QUE SI NO ESTA 
        PREVIAMENTE EN EL SISTEMA NO SE PUEDE AÑADIR UNA MASCOTA'''
        dato_cod_cita, dato_fecha, dato_hora, dato_establecimiento, dato_dni = self.recoger_datos_citas()
        if (dato_hora in self.horas_posibles and dato_establecimiento in self.establecimientos_posibles and self.validador.validador_fecha(dato_fecha)):
            messagebox.askyesno(message=f"DATOS:\nID DE CITA: {dato_cod_cita}\nFECHA: {dato_fecha}\nHORA: {dato_hora}\nESTABLECIMIENTO: {dato_establecimiento}\nDNI: {dato_dni}")
            if self.MESSAGEBOX:
                if not self.almacen_citas.comprobar_existencia_cliente(dato_dni):
                    messagebox.showinfo(message="EL CLIENTE NO ESTÁ REGISTRADO EN EL SISTEMA") 
                elif self.almacen_citas.comprobar_fecha_fijada(dato_fecha, dato_hora, dato_establecimiento):
                    messagebox.showinfo(message="LA FECHA YA ESTÁ FIJADA") 
                else:
                    self.almacen_citas.add_citas(dato_cod_cita, dato_fecha, dato_hora, dato_establecimiento, dato_dni)
                    self.withdraw()
                    self.master.deiconify()
        else:
            self.mostrar_datos_incorrectos()
    
    def on_close(self):
        self.withdraw()
        self.master.deiconify()

    #PLACEHOLDERS
    def clear_placeholder_fecha_input(self, event):
        if self.input_fecha_cita.get() == self.PLACEHOLDER_FECHA:
            self.input_fecha_cita.delete(0, tk.END)
            self.input_fecha_cita.config(foreground='black')

    def set_placeholder_fecha_input(self, event):
        if self.input_fecha_cita.get() == "":
            self.input_fecha_cita.insert(0, self.PLACEHOLDER_FECHA)
            self.input_fecha_cita.config(foreground='gray')

    def clear_placeholder_dni_input(self, event):
        if self.input_dni.get() == self.PLACEHOLDER_DNI:
            self.input_dni.delete(0, tk.END)
            self.input_dni.config(foreground='black')

    def set_placeholder_dni_input(self, event):
        if self.input_dni.get() == "":
            self.input_dni.delete(0, tk.END)
            self.input_dni.config(foreground='black')

    def clear_placeholder_eleccion_establecimiento(self, event):
        if self.eleccion_establecimiento.get() == self.PLACEHOLDER_ESTABLECIMIENTO:
            self.eleccion_establecimiento.delete(0, tk.END)
            self.eleccion_establecimiento.config(foreground='black')

    def set_placeholder_eleccion_establecimiento(self, event):
        if self.eleccion_establecimiento.get() == "":
            self.eleccion_establecimiento.delete(0, tk.END)
            self.eleccion_establecimiento.config(foreground='black')

    @staticmethod
    def mostrar_datos_incorrectos():
        advertencia = messagebox.showinfo(message="DATOS INCORRECTOS")
        return advertencia