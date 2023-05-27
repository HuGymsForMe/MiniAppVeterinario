import os

from clases.clientes import Cliente

class AlmacenClientes:
    def __init__(self, app):
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../Ej 01-06-2023 (PYTHON)/files')
        self.CAMPO_DNI = 0
        self._clientes = []

    @property
    def clientes(self):
        return self._clientes

    def cargar_clientes(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'r', encoding="UTF-8") as fichero_clientes:
                lineas = fichero_clientes.readlines()[::1]
                for linea in lineas:
                    self._clientes.append(linea)
                return self._clientes
    
    def add_clientes(self, dato_dni, dato_nombre, dato_apellidos, dato_telefono):
        nuevo_cliente = Cliente(dni=dato_dni, nombre=dato_nombre, apellidos=dato_apellidos, telefono=dato_telefono)
        if isinstance(nuevo_cliente, Cliente) and nuevo_cliente not in self._clientes:
            with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'r', encoding="UTF-8") as fichero_clientes:
                lineas = fichero_clientes.readlines()[::1]
                for linea in lineas:
                    campos = linea.strip().split(';')
                    dni_cliente = campos[self.CAMPO_DNI]
                    if dni_cliente == dato_dni:
                        return True
            self._clientes.append(nuevo_cliente)
        return False
    
    def sobreescribir_clientes(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'w', encoding="UTF-8") as nuevo_csv_clientes:
            for linea in self._clientes:
                nuevo_csv_clientes.write(f"{str(linea)}") 
