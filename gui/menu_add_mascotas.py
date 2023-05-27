import abc
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from clases.almacen_mascotas import AlmacenMascotas

class MenuAddMascotas(tk.Toplevel):
    def __init__(self, master, almacen_mascotas):
        self.almacen_mascotas = almacen_mascotas
        super().__init__(master)
        self.withdraw()
        self.MESSAGEBOX = "yes"
        self.PLACEHOLDER_ANIMAL = "Animal:"
        self.PLACEHOLDER_RAZA = "Raza:"
        self.PLACEHOLDER_DNI = "Ej: 00000000B"
        self.title("AÑADIR MASCOTA")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(400, 350)
        self.geometry("400x350+675+100")
        self.maxsize(400, 350)
        self.danio_seleccionado = tk.StringVar()
        self.print_animal = ttk.Label(self, text="ANIMAL: ", font=("Helvetica", 12))
        self.input_animal = ttk.Entry(self, foreground="gray")
        self.input_animal.insert(0, self.PLACEHOLDER_ANIMAL)
        self.input_animal.bind('<FocusIn>', self.clear_placeholder_input_animal)
        self.input_animal.bind('<FocusOut>', self.set_placeholder_input_animal)
        self.print_raza = ttk.Label(self, text="RAZA: ", font=("Helvetica", 12))
        self.input_raza = ttk.Entry(self, foreground="gray")
        self.input_raza.insert(0, self.PLACEHOLDER_RAZA)
        self.input_raza.bind('<FocusIn>', self.clear_placeholder_input_raza)
        self.input_raza.bind('<FocusOut>', self.set_placeholder_input_raza)
        self.print_danio = ttk.Label(self, text="GRAVEDAD DEL DAÑO: ", font=("Helvetica", 12))
        self.opcion_1 = ttk.Radiobutton(self, text="LEVE", value="LEVE", variable=self.danio_seleccionado)
        self.opcion_2 = ttk.Radiobutton(self, text="MODERADO", value="MODERADO", variable=self.danio_seleccionado)
        self.opcion_3 = ttk.Radiobutton(self, text="GRAVE", value="GRAVE", variable=self.danio_seleccionado)
        self.print_duenio = ttk.Label(self, text="DUEÑO: ", font=("Helvetica", 12))
        self.input_duenio = ttk.Entry(self, foreground="gray")
        self.input_duenio.insert(0, self.PLACEHOLDER_DNI)
        self.input_duenio.bind('<FocusIn>', self.clear_placeholder_input_duenio)
        self.input_duenio.bind('<FocusOut>', self.set_placeholder_input_duenio)
        self.boton_guardar_mascotas = ttk.Button(self, text="AÑADIR MASCOTA", command=self.comprobar_mascotas)

    def visualizar_menu_principal(self):
        self.destroy
        self.withdraw()
        self.master.deiconify()

    def mostrar_menu(self):
        self.deiconify()
        self.print_animal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_animal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_raza.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_raza.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_danio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.opcion_1.pack()
        self.opcion_2.pack()
        self.opcion_3.pack()
        self.print_duenio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_duenio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_guardar_mascotas.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()
    
    def recoger_datos_mascotas(self):
        dato_animal = self.input_animal.get().upper()
        dato_raza = self.input_raza.get().upper()
        dato_danio = self.danio_seleccionado.get()
        dato_duenio = self.input_duenio.get().upper()
        dato_id_mascota = f"{dato_animal[:2]}{dato_raza[:2]}{dato_duenio}"
        return dato_id_mascota, dato_animal, dato_raza, dato_danio, dato_duenio
    
    def comprobar_mascotas(self):
        '''NO ES NECESARIO UN DNI VÁLIDADO YA QUE SI NO ESTA 
        PREVIAMENTE EN EL SISTEMA NO SE PUEDE AÑADIR UNA MASCOTA'''
        dato_id_mascota, dato_animal, dato_raza, dato_danio, dato_duenio = self.recoger_datos_mascotas()
        if self.almacen_mascotas.comprobar_duenio(dato_duenio) and dato_animal != '' and dato_raza != '' and dato_danio != '':
            messagebox.askyesno(message=f"DATOS:\nID MASCOTA: {dato_id_mascota}\nANIMAL: {dato_animal}\nRAZA: {dato_raza}\nDAÑO: {dato_danio}\nDUEÑO: {dato_duenio}")
            if self.MESSAGEBOX:
                self.almacen_mascotas.add_mascotas(dato_id_mascota, dato_animal, dato_raza, dato_danio, dato_duenio)
                self.withdraw()
                self.master.deiconify()
        else:
            messagebox.showinfo(message="EL CLIENTE NO ESTÁ REGISTRADO EN EL SISTEMA")

    def on_close(self):
        self.withdraw()
        self.master.deiconify()

    def clear_placeholder_input_animal(self, event):
        if self.input_animal.get() == self.PLACEHOLDER_ANIMAL:
            self.input_animal.delete(0, tk.END)
            self.input_animal.config(foreground='black')

    def set_placeholder_input_animal(self, event):
        if self.input_animal.get() == "":
            self.input_animal.delete(0, tk.END)
            self.input_animal.config(foreground='black')
        
    def clear_placeholder_input_raza(self, event):
        if self.input_raza.get() == self.PLACEHOLDER_RAZA:
            self.input_raza.delete(0, tk.END)
            self.input_raza.config(foreground='black')

    def set_placeholder_input_raza(self, event):
        if self.input_raza.get() == "":
            self.input_raza.delete(0, tk.END)
            self.input_raza.config(foreground='black')

    def clear_placeholder_input_duenio(self, event):
        if self.input_duenio.get() == self.PLACEHOLDER_DNI:
            self.input_duenio.delete(0, tk.END)
            self.input_duenio.config(foreground='black')

    def set_placeholder_input_duenio(self, event):
        if self.input_duenio.get() == "":
            self.input_duenio.delete(0, tk.END)
            self.input_duenio.config(foreground='black')