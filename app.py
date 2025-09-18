# ==========================
#   Importación de módulos
# ==========================
import socket        # Para manejar la conexión cliente-servidor
import sys           # Para salir del programa si es necesario
import sqlite3 as sql  # Para manejar la base de datos SQLite
import threading as thread  # Para posibles hilos (no usado aún)
from tkinter import *       # Para la interfaz gráfica
from tkinter import ttk, messagebox, Toplevel
from kivy.app import App    # Importado, próximamente se utilizará
from time import sleep      # Para hacer pausas (simular carga)

# ==========================
#   Clase Base de Datos
# ==========================

class Kernel(App):
    def __init__(self):
        pass

class DataBase:
    def __init__(self, conn):
        self.conn = conn
        # Guardamos y cerramos la conexión inicial
        self.conn.commit()
        self.conn.close()
        # Creamos la tabla si no existe
        self.create_table()
    
    def create_table(self):
        """Crea la tabla 'data' si no existe"""
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
        """Inserta un registro con nombre y dinero"""
        self.conn = sql.connect("logs_game.db")
        self.cursor = self.conn.cursor()
        # ⚠️ Aquí sería mejor usar parámetros en vez de f-string para evitar SQL Injection
        self.instruction = f"INSERT INTO data VALUES('{name}', {money})"
        self.cursor.execute(self.instruction)
        self.conn.commit()
        self.close()

    def read_data(self):
        """Lee y muestra todos los registros guardados"""
        self.conn = sql.connect("logs_game.db")
        self.cursor = self.conn.cursor()
        self.instruction = "SELECT * FROM data;"
        self.cursor.execute(self.instruction)
        self.save_data = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()

        # Mostramos la información recuperada
        for i in self.save_data:
            self.save_name = i[0]
            self.save_money = i[1]
        print(f"Nombre: {self.save_name}")
        print(f"Dinero en el juego: {self.save_money}")

# ==========================
#   Clase Conexión Cliente
# ==========================
class ConnectServer:
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 8080
        # Iniciamos la conexión al servidor
        self.connect_server()
    
    def connect_server(self):
        """Se conecta al servidor y maneja mensajes"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))

            while True:
                # Recibir mensaje del servidor
                self.data_receive = s.recv(1024)
                self.message = self.data_receive.decode()

                print(f"Mensaje recibido: {self.message}")

                # Responder al servidor
                s.sendall("¡Hola, desde el cliente!".encode('utf-8'))

# ==========================
#   Ejecución Principal
# ==========================
if __name__ == '__main__':
    # Inicializamos la base de datos
    conn = sql.connect("logs_game.db")
    db = DataBase(conn)

    # Intentamos conectar al servidor
    try:
        app = ConnectServer()
    except OSError:
        pass

# ==========================
#   Interfaz / Terminal
# ==========================
try:
    # Preguntamos al usuario su nombre
    user_name = input("¿Cómo te llamas?: ").title()

    # Preguntamos si está en un entorno gráfico
    response = input(f"\n¿{user_name}, usted está en un entorno gráfico (GUI)?: ").lower()
    response.strip()

    # Si está en GUI, cargamos Tkinter
    if response == "si" or response == "sí":
        root = Tk()
        root.title("GameServer")
        root.geometry("400x400")

        # Texto de bienvenida
        widget_text = Label(text="¡Hola Bienvenido(a) al juego!", fg="lightgreen")
        widget_text.grid(row=0, column=1)

        # Botón (sin acción asignada aún)
        widget_btn = ttk.Button(text="Botón")
        widget_btn.grid(row=1, column=1)

        root.mainloop()
    else:
        # Si no, cargamos la versión en terminal
        print("\nEl juego se generará en la terminal. Por favor espere un momento....")
        sleep(1)

except EOFError:
    # Si no hay entorno interactivo, se lanza una ventana gráfica por defecto
    print("No estás en un entorno interactivo de terminal o consola")
    root = Tk()
    root.title("GameServer")
    root.geometry("400x400")

    root.columnconfigure(1, weight=1)
    
    widget_btn = ttk.Button(text="Botón")
    widget_btn.grid(row=1, column=1)

    widget_input = ttk.Entry(root)
    widget_input.grid(row=2, column=2)

    menu_bar = Menu(root)
    
    file_menu = Menu(tearoff=0)
    file_menu.add_command(label="Salir")
    menu_bar.add_cascade(label="Opciones", menu=menu_bar)

    root.configure(menu=menu_bar)
    root.mainloop()
