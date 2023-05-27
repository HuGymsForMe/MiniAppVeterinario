import re
import abc
from datetime import datetime

class Validator:
    def __init__(self):
        self.patron_dni = r'^\d{8}[A-Za-z]$'
        self.patron_telef = r'^\d{9}$'
        self.formato_fecha = "%d/%m/%Y"
    
    def validador_fecha(self, dato_fecha_pedido):
        fecha_actual = datetime.now()
        try:
            dato_fecha = datetime.strptime(str(dato_fecha_pedido), self.formato_fecha)
            if dato_fecha > fecha_actual:
                return True
            return False
        except ValueError:
            return False

    def validador_dni(self, dato_dni):
        if re.match(self.patron_dni, dato_dni):
            return True
        return False

    def validador_telefono(self, dato_telefono):
        if re.match(self.patron_telef, dato_telefono):
            return True
        return False

    