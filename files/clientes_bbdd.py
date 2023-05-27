import os

import mysql.connector
from mysql.connector import errorcode

USER = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
DATABASE = 'proyecto_veterinario'
RUTA_FICHEROS = os.path.abspath('../Ej 01-06-2023 (PYTHON)/files')
DELETE_PREVIO = f"DELETE FROM vet_clientes;"

class ConstantesCamposClientes:
    DNI = 0
    NOMBRE = 1
    APELLIDOS = 2
    TELEFONO = 3

    @staticmethod
    def opciones():
        return range(ConstantesCamposClientes.DNI,
            ConstantesCamposClientes.TELEFONO+1)

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
    with open(os.path.join(RUTA_FICHEROS, 'clientes.csv'), encoding='UTF-8') as informacion:
        lineas = informacion.readlines()[1:]
    for linea in lineas:
        datos = linea.split(';')
        dni = str(datos[ConstantesCamposClientes.DNI].strip())
        nombre = str(datos[ConstantesCamposClientes.NOMBRE].strip())
        apellidos = str(datos[ConstantesCamposClientes.APELLIDOS].strip())
        telefono = str(datos[ConstantesCamposClientes.TELEFONO].strip())
        inserts = f"INSERT INTO vet_clientes (DNI, NOMBRE, APELLIDOS, TELEFONO) VALUES('{dni}','{nombre}','{apellidos}',{telefono});"
        cursor.execute(inserts)
        cnx.commit()
    cursor.close()