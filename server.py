# Importamos los módulos necesarios
import socket      # Para crear la comunicación cliente-servidor
import sqlite3 as sql  # Para manejar la base de datos SQLite
import threading as thread  # Para trabajar con hilos (aunque no se usa aún)
import sys         # Para poder salir del programa con sys.exit()

# Configuración inicial del servidor
HOST = 'localhost'  # Dirección del servidor (en este caso, la misma máquina)
PORT = 8080         # Puerto en el que se intentará levantar el servidor

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

# Intentamos iniciar el servidor en el puerto configurado
while True:
    try:
        # Creamos el socket con IPv4 y TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Asociamos el socket al host y puerto
            s.bind((HOST, PORT))
            # Ponemos el servidor en modo escucha (máx. 5 conexiones en cola)
            s.listen(5)
        break  # Si todo salió bien, salimos del bucle
    
    except OSError:
        # Si el puerto 8080 está ocupado, cambiamos al 6785
        PORT = 6785
        print("Hubo un pequeño error")
        continue  # Reintentamos con el nuevo puerto

    # Bucle principal para aceptar conexiones
    while True:
        try:
            try:
                # Esperamos a que un cliente se conecte
                conn, addr = s.accept()
                print(f"Conexión Exitosa con: {addr}")

                # Enviamos un mensaje al cliente
                s.sendall("¡Hola, desde el servidor!".encode('utf-8'))
      
                # Recibimos datos del cliente (hasta 1024 bytes)
                data = s.recv(1024)
                # Decodificamos el mensaje recibido
                message = data.decode()

            except KeyboardInterrupt:
                # Si el usuario presiona Ctrl+C, salimos
                sys.exit()

        except OSError:
            # Si ocurre un error en la comunicación
            print("Hubo un error en la comunicación")
