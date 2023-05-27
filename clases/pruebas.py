from tkinter import Tk, Button, Toplevel, Entry

class Formulario:
    def __init__(self, parent):
        self.parent = parent
        self.formulario = None

        self.btn_abrir = Button(self.parent, text="Abrir formulario", command=self.abrir_formulario)
        self.btn_abrir.pack()

    def abrir_formulario(self):
        if self.formulario is None or not self.formulario.winfo_exists():
            self.formulario = Toplevel(self.parent)
            self.formulario.protocol("WM_DELETE_WINDOW", self.cerrar_formulario)
            
            self.entry_nombre = Entry(self.formulario)
            self.entry_nombre.pack()
            
            self.btn_guardar = Button(self.formulario, text="Guardar", command=self.guardar_formulario)
            self.btn_guardar.pack()
            
        else:
            self.formulario.lift()  # Trae la ventana al frente si ya está abierta

    def guardar_formulario(self):
        # Aquí puedes guardar los datos ingresados en el formulario
        nombre = self.entry_nombre.get()
        # Realiza las operaciones de guardar los datos según tus necesidades
        
        self.cerrar_formulario()

    def cerrar_formulario(self):
        if self.formulario is not None and self.formulario.winfo_exists():
            self.formulario.destroy()
            self.formulario = None


root = Tk()
formulario = Formulario(root)
root.mainloop()

