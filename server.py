import socket
import sqlite3
import threading as thread
import sys

HOST = 'localhost'
PORT = 8080

class DataBase:
    def __init__(self, conn):
        self.conn = conn
        self.conn.commit()
        self.conn.close()

        self.create_table()

    def create_table(self):
        self.conn = sql.connect("logs_conection.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
           """CREATE TABLE IF NOT EXISTS data_conection(
               day INTEGER,
               month INTEGER,
               year INTEGER
               address TEXT,
           )"""
)
        self.conn.commit()
        self.conn.close()

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(5)
        break
    
    except OSError:
        PORT = 6785
        print("Hubo un pequeño error")
        continue
    
    while True:
        try:
            try:
                conn, addr = s.accept()

                print(f"Conexión Exitosa con: {addr}")

                s.sendall("¡Hola, desde el servidor!".encode('utf-8'))
      
                data = s.recv(1024)
                message = data.decode()

            except KeyboardInterrupt:
                sys.exit()

        except OSError:
            print("Hubo un error en la comunicación")
