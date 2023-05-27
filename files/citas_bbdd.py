import os

import mysql.connector
from mysql.connector import errorcode

USER = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
DATABASE = 'proyecto_veterinario'
RUTA_FICHEROS = os.path.abspath('../Ej 01-06-2023 (PYTHON)/files')
DELETE_PREVIO = f"DELETE FROM vet_citas;"

class ConstantesCamposCitas:
    COD_CITA = 0
    FECHA_CITA = 1
    HORA = 2
    ESTABLECIMIENTO = 3
    DNI = 4

    @staticmethod
    def opciones():
        return range(ConstantesCamposCitas.COD_CITA,
            ConstantesCamposCitas.DNI+1)

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
    with open(os.path.join(RUTA_FICHEROS, 'citas.csv'), encoding='UTF-8') as informacion:
        lineas = informacion.readlines()[1:]
    for linea in lineas:
        datos = linea.split(';')
        cod_cita = str(datos[ConstantesCamposCitas.COD_CITA].strip())
        fecha_cita = str(datos[ConstantesCamposCitas.FECHA_CITA].strip())
        hora = str(datos[ConstantesCamposCitas.HORA].strip())
        establecimiento = str(datos[ConstantesCamposCitas.ESTABLECIMIENTO].strip())
        dni = str(datos[ConstantesCamposCitas.DNI].strip())
        inserts = f"INSERT INTO vet_citas (COD_CITA, FECHA_CITA, HORA, ESTABLECIMIENTO, DNI) VALUES('{cod_cita}','{fecha_cita}','{hora}','{establecimiento}','{dni}');"
        cursor.execute(inserts)
        cnx.commit()
    cursor.close()