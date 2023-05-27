import os

from clases.mascotas import Mascota

class AlmacenMascotas:
    def __init__(self, app):
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../Ej 01-06-2023 (PYTHON)/files')
        self.DUENIO = 0
        self.ID_MASCOTA = 0
        self._mascotas = []

    def cargar_mascotas(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'mascotas.csv'), 'r', encoding="UTF-8") as fichero_mascotas:
                lineas = fichero_mascotas.readlines()[::1]
                for linea in lineas:
                    self._mascotas.append(linea)
                return self._mascotas

    def add_mascotas(self, dato_id_mascota, dato_animal, dato_raza, dato_danio, dato_duenio):
        nueva_mascota = Mascota(id_mascota=dato_id_mascota, animal=dato_animal, raza=dato_raza, danio=dato_danio, duenio=dato_duenio)
        self._mascotas.append(nueva_mascota)
        return self._mascotas

    def comprobar_duenio(self, dato_duenio):
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'r', encoding="UTF-8") as fichero_clientes:
            lineas = fichero_clientes.readlines()[::1]
            for linea in lineas:
                campos = str(linea).split(';')
                dni = str(campos[self.DUENIO].strip())
                if dato_duenio == dni:
                    return True
            return False

    def del_mascota(self, dato_id_mascota):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'mascotas.csv'), 'r', encoding="UTF-8") as fichero_mascotas:
                lineas = fichero_mascotas.readlines()[::1]
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_id_mascota = str(campos[self.ID_MASCOTA].strip())
                    if dato_id_mascota == campo_id_mascota:
                        self._mascotas.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass

    def sobreescribir_mascotas(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'mascotas.csv'), 'w', encoding="UTF-8") as nuevo_csv_mascotas:
            for linea in self._mascotas:
                nuevo_csv_mascotas.write(f"{str(linea)}") 
