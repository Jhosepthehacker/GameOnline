# Importamos los módulos necesarios
import socket      # Para crear la comunicación cliente-servidor
import sqlite3 as sql  # Para manejar la base de datos SQLite
import threading as thread  # Para trabajar con hilos (aunque no se usa aún)
import sys         # Para poder salir del programa con sys.exit()

# Anque podría heredar de la clase en el archivo 'app.py', sin embargo quiero hacerla independiente

class accept_Conection:
    def __init__(self):
        pass

# Clase encargada de manejar la base de datos
class DataBase:
    def __init__(self, conn):
        # Recibe una conexión a la base de datos
        self.conn = conn
        # Confirmamos cualquier cambio pendiente
        self.conn.commit()
        # Cerramos la conexión inicial
        self.conn.close()
        # Creamos la tabla (si no existe)
        self.create_table()

    def create_table(self):
        # Reabrimos la conexión con SQLite
        self.conn = sql.connect("logs_conection.db")
        self.cursor = self.conn.cursor()
        
        # Creamos una tabla llamada "data_conection"
        # para almacenar día, mes, año y dirección
        self.cursor.execute(
           """CREATE TABLE IF NOT EXISTS data_conection(
               day INTEGER,
               month INTEGER,
               year INTEGER,
               address TEXT
           )"""
        )
        # Guardamos los cambios
        self.conn.commit()
        # Cerramos la conexión
        self.conn.close()
