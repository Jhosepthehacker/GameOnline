# Importamos los módulos necesarios
import socket      # Para crear la comunicación cliente-servidor
import sqlite3 as sql  # Para manejar la base de datos SQLite
import threading as thread  # Para trabajar con hilos (aunque no se usa aún)
import sys         # Para poder salir del programa con sys.exit()

# Anque podría heredar de la clase en el archivo 'app.py', sin embargo quiero hacerla independiente

class connect_Interface_Client:
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 8080

    def send_and_receive(self):
        self.data = self.my_socket.recv(1024)
        self.message = self.data.decode()

        self.my_socket.sendall("¡Hola, desde el servidor!".encode('utf-8'))
    
    def accept_conection(self):
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind((self.HOST, self.PORT))
                    s.listen(5)

                    self.conn, self.addr = s.accept()

                    print(f"Conexión exitosa con: {self.addr}")

                    self.my_socket = self.conn

                    self.an_thread = thread.Thread(target=self.send_and_receive)
                    self.an_thread.start()
            
            except OSError as e:
                print(f"Hubo un error en la conexión: {e}")

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

if __name__ == '__main__':
    app = connect_Interface_Client()
    app.accept_conection()
