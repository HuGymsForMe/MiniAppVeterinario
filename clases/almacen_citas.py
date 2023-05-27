import os

from clases.citas import Cita

class AlmacenCitas:
    def __init__(self, app):
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../Ej 01-06-2023 (PYTHON)/files')
        self.CAMPO_ID_CITA = 0
        self._citas = []

    @property
    def citas(self):
        return self._citas

    def cargar_citas(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'citas.csv'), 'r', encoding="UTF-8") as fichero_citas:
                lineas = fichero_citas.readlines()[::1]
                for linea in lineas:
                    self._citas.append(linea)
                return self._citas
    
    def add_citas(self, dato_cod_cita, dato_fecha, dato_hora, dato_establecimiento, dato_dni):
            nueva_cita = Cita(cod_cita=dato_cod_cita, fecha_cita=dato_fecha, hora=dato_hora, establecimiento=dato_establecimiento, dni=dato_dni)
            self._citas.append(nueva_cita)
            return self._citas

    def comprobar_existencia_cliente(self, dato_dni):
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'r', encoding="UTF-8") as fichero_clientes:
            for linea in fichero_clientes:
                if dato_dni in linea:
                    return True
            return False

    def comprobar_fecha_fijada(self, dato_fecha, dato_hora, dato_establecimiento):
        fecha_fijada = f"{dato_fecha};{dato_hora};{dato_establecimiento}"
        with open(os.path.join(self.RUTA_FICHEROS, 'citas.csv'), 'r', encoding="UTF-8") as fichero_clientes:
            for linea in fichero_clientes:
                if fecha_fijada in linea:
                    return True
            return False

    def del_citas(self, dato_borrar_cita):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'citas.csv'), 'r', encoding="UTF-8") as fichero_citas:
                lineas = fichero_citas.readlines()[::1]
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    id_cita = str(campos[self.CAMPO_ID_CITA].strip())
                    if id_cita == dato_borrar_cita:
                        self._citas.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass
                    
    def sobreescribir_citas(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'citas.csv'), 'w', encoding="UTF-8") as nuevo_csv_citas:
            for linea in self._citas:
                nuevo_csv_citas.write(f"{str(linea)}") 


            
