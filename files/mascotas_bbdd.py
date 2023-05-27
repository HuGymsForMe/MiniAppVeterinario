import os

import mysql.connector
from mysql.connector import errorcode

USER = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
DATABASE = 'proyecto_veterinario'
RUTA_FICHEROS = os.path.abspath('../Ej 01-06-2023 (PYTHON)/files')
DELETE_PREVIO = f"DELETE FROM vet_mascotas;"

class ConstantesCamposMascotas:
    ID_MASCOTA = 0
    ANIMAL = 1
    RAZA = 2
    DANIO = 3
    DUENIO = 4

    @staticmethod
    def opciones():
        return range(ConstantesCamposMascotas.ID_MASCOTA,
            ConstantesCamposMascotas.DUENIO+1)

try:
    cnx = mysql.connector.connect(user=USER, password=PASSWORD,
                                  host=HOST,
                                  database=DATABASE)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error de conexión")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("No existe la BBDD")
    else:
        print(err)
else:
    cursor = cnx.cursor()
    cursor.execute(DELETE_PREVIO)
    cnx.commit()
    cursor.close()
    cursor = cnx.cursor()
    with open(os.path.join(RUTA_FICHEROS, 'mascotas.csv'), encoding='UTF-8') as informacion:
        lineas = informacion.readlines()[1:]
    for linea in lineas:
        datos = linea.split(';')
        id_mascota = str(datos[ConstantesCamposMascotas.ID_MASCOTA].strip())
        animal = str(datos[ConstantesCamposMascotas.ANIMAL].strip())
        raza = str(datos[ConstantesCamposMascotas.RAZA].strip())
        danio = str(datos[ConstantesCamposMascotas.DANIO].strip())
        duenio = str(datos[ConstantesCamposMascotas.DUENIO].strip())
        inserts = f"INSERT INTO vet_mascotas (ID_MASCOTA, ANIMAL, RAZA, DANIO, DUENIO) VALUES('{id_mascota}','{animal}','{raza}','{danio}','{duenio}');"
        cursor.execute(inserts)
        cnx.commit()
    cursor.close()