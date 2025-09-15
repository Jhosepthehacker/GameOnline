import socket
import kivy
import sys
import sqlite3
import threading as thread
from tkinter import *
from tkinter import ttk, messagebox, Toplevel
from time import sleep

# Posibles errores de la clase 'ConnectServer', de su método 'connect_server'.

class DataBase:
    def __ini__(self, conn):
        self.conn = conn
        self.conn.commit()
        self.conn.close()

        self.create_table()

# No usaré 'width' para db en este caso
    
    def create_table(self):
        self.conn = sql.connect("logs_game.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
           """CREATE TABLE IF NOT EXISTS data(
                name TEXT,
                money INTEGER
           )"""
)
        self.conn.commit()
        self.conn.close()

    def insert_data(self, name, money):
        self.conn = sql.connect("logs_game.db")
        self.cursor = self.conn.cursor()
        self.instruction = f"INSERT INTO data VALUES('{name}', {money})"
        self.cursor.execute(self.instruction)
        self.conn.commit()
        self.close()

    def read_data(self):
        self.conn = sql.connect("logs_game.db")
        self.cursor = self.conn.cursor()
        self.instruction = "SELECT * FROM data;"
        self.cursor.execute(self.instruction)
        self.save_data = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()

        for i in self.save_data:
            self.save_name = i[0]
            self.save_money = i[1]
        print(f"Nombre: {self.save_name}")
        print(f"Dinero en el juego: {self.save_money}")

class ConnectServer:
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 8080

        self.connect_server():
    
    def connect_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))

            while True:
                self.data_receive = s.recv(1024)
                self.message = self.data_receive.decode()

                print(f"Mensaje recibido: {self.message}")

                s.sendall("¡Hola, desde el cliente!".encode('utf-8'))

if __name__ == '__main__':
    conn = sql.connect("logs_game.db")
    db = DataBase(conn)

    try:
        app = ConnectServer()
    except OSError:
        pass

try:
    user_name = input("¿Cómo te llamas?: ").title()

    response = input(f"\n¿{user_name}, usted está en un entorno gráfico (GUI)?: ").lower()
    response.strip()

# Próximamente se le implementará un "weight" para 'grid()'
    
    if response == "si" or response == "sí":
        root = Tk()
        root.title("GameServer")
        root.geometry("400x400")

        widget_text = Label(text="¡Hola Bienvenido(a) al juego!", fg="lightgreen")
        widget_text.grid(row=0, column=1)

        widget_btn = ttk.Button(text="Botón")
        widget_btn.grid(row=1, column=1)

        root.mainloop()
    else:
        print("\nEl juego se generará en la terminal. Por favor espere un momento....")
        sleep(1)

except EOFError:
    print("No estás en un entorno interactivo de terminal o consola")
    root = Tk()
    root.title("GameServer")
    root.geometry("400x400")

    widget_btn = ttk.Button(text="Botón")
    widget_btn.grid(row=1, column=1)

    widget_input = Entry(root)
    widget_input.grid(row=2, column=2)
    
    root.mainloop()
