# ==========================
#   Importación de módulos
# ==========================
import socket               # Para manejar la conexión cliente-servidor
import sys                  # Para salir del programa si es necesario
import os
import sqlite3 as sql       # Para manejar la base de datos SQLite  # Para posibles hilos (no usado aún)
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
    def __init__(self, conn, data_name):
        self.conn = conn
        # Guardamos y cerramos la conexión inicial
        self.conn.commit()
        self.conn.close()
        self.data_name = data_name
        # Creamos la tabla si no existe
        self.create_table()
        self.insert_data(self.data_name, None)
        self.read_data()
    
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

    def connect_server(self, send_message):
        try:
            try:
                while True:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((self.HOST, self.PORT))

                        self.data = s.recv(1024)
                        self.message = self.data.decode()

                        print(f"[•] Mensaje Recibido: {self.message}")
                        s.sendall(f"{send_message}".encode('utf-8'))

            except AttributeError:
                print("Usted tiene un archivo llamado 'socket', lo que impide la ejecución de la conexión. Por favor cambie de nombre o elimine el archivo para continuar")

        except OSError as e:
            print(f"Error en la conexión: {e}")

def game_in_terminal(option):
    if option == "1":
        try:
            try:
                number = random.randint(1, 100)
                trys = 0
                while True:
                    try:
                        number_to_usr = input(f"{user_name} adivina un número del 1 al 100: ")
                        trys += 1
                    except ValueError:
                        print("Ingresa un número, no texto")
                        continue

                    if number_to_usr < number:
                        print(f"El número {number_to_usr} es demasiado bajo al número secreto")
                    elif number_to_usr > number:
                        print(f"El número {number_to_usr} es demasiado alto al número secreto")
                    elif number_to_usr == number:
                        print(f"Felicidades {user_name}, has encontrado el número {number} en {trys} intentos")
                        break
            except NameError:
                print("Ha ocurrido un problema")
                sleep(1)
                sys.exit()

        except EOFError:
            print("No estás en un entorno interactivo de terminal o consola")
    elif option == "2":
        import random
        import sqlite3 as sql

        class DataBase:
        def __init__(self, conn, position, inventory):
            self.conn = conn
            self.conn.commit()
            self.conn.close()

            self.create_table()
            self.insert_data(position, inventory)

        def create_table(self):
            try:
                self.conn = sql.connect("game_logs.db")
                self.cursor = self.conn.cursor()
                self.cursor.execute(
		            """CREATE TABLE IF NOT EXISTS logs(
		                position TEXT,
		                inventory TEXT
		    )"""
)

            finally:
                self.conn.commit()
                self.conn.close()

        def insert_data(self, position, inventory):
            try:
                self.conn = sql.connect("game_logs.db")
                self.cursor = self.conn.cursor()
                self.instruction = f"INSERT INTO logs VALUES('{position}', '{inventory}')"
                self.cursor.execute(self.instruction)
            finally:
                self.conn.commit()
                self.conn.close()

         def read_data(self):
             try:
                 self.conn = sql.connect("game_logs.db")
                 self.instruction = "SELECT * FROM logs;"
                 self.cursor = self.conn.cursor()
                 self.cursor.execute(self.instruction)
                 data = self.cursor.fetchall()

                 return data
            finally:
                self.conn.commit()
                self.conn.close()

    map = [
       list("  ###########    #########"),
       list("  # @       #####        #"),
       list("  #     E            H   #"),
       list("  #         #####        #"),
       list("  ##########     #########")
]

    for i in map:
        print(len(i))

    print(
           """
  @ = Tu personaje (6 Vidas)
  E = Enemigo (4 Vidas)
  H = Hierro (Mina)
  
  // Escribe 'i' para ver tu inventario //
  // Escribe 'x' para ocultar tu inventario //
           """

)

    player_row = 1
    player_column = 4

    lifes = 6
    lifes_enemy = 4

    inventory = []
    position = map

    def print_map():
	    for i in map:
            print("".join(i))

	    print(f"\nVidas: {lifes}")
	    print("\n------\n")

    def move_character(direction):
	    global player_row, player_column, lifes, lifes_enemy
	
        row, column = player_row, player_column
	
	    if direction == "w":
		    row -= 1
        elif direction == "s":
		    row += 1
	    elif direction == "a":
		    column -= 1
	    elif direction == "d":
		    column += 1
	
	    next_row, next_column = row, column
	
	    if map[next_row][next_column] != "#":
            if map[next_row][next_column] == "E":
			    possible_attack = random.randint(1, 6)

                if possible_attack in (1, 2, 3):
                    lifes -= 1
                    print("Has perdido 1 vida\n")
			    elif possible_attack in (4, 5, 6):
                    lifes_enemy -= 1
				    print("El enemigo ha perdido una vida")
			
		    else:
                 map[player_row][player_column] = ' '
                 map[next_row][next_column] = '@'
		
                 player_row, player_column = next_row, next_column
        else:
             print("No puedes atravesar la barrera (límite del juego)")

    while True:
	    print_map()
	
        move_player = input("Escribe (w/s/a/d) para moverte, 'q' para salir: ").lower().strip()

        if move_player in ("w", "s", "a", "d"):
		    move_character(move_player)
		    time.sleep(1)
		    os.system('clear')
	    elif move_player == "q":
		    time.sleep(1)
		    sys.exit()
	    elif move_player == "i":
	        print("Inventario:\n")
	    
	        for i in inventory:
	            print(f"  {i}")
	    elif move_player == "x":
		    pass
	    else:
		    print("Ingresa un caracter válido")
        

# ==========================
#   Interfaz / Terminal
# ==========================

try:
    try:
      # Preguntamos al usuario su nombre
        user_name = input("¿Cómo te llamas?: ").title()

        print("\nLa contraseña a crear, protegerá sus datos")
    
        enter_password = input(f"\n¿{user_name}, podría ingresar una nueva contraseña para crear?: ")

        print(f"\nGracias por su cooperación {user_name} :)")

        conn = sql.connect("logs_game.db")
        app = DataBase(conn, user_name, enter_password)
    
      # Preguntamos si está en un entorno gráfico
        response = input(f"\n¿{user_name}, usted está en un entorno gráfico (GUI)?: ").lower()
        response.strip()

      # Si está en GUI, cargamos Tkinter
        if response == "si" or response == "sí":
            root = Tk()
            root.title("GameServer")
            root.geometry("400x400")

            widget_text_name = Label(root, text="Nombre:")
            widget_text_name.grid(row=0, column=0)

            widget_text_last_name = Label(root, text="Apellido:")
            widget_text_last_name.grid(row=1, column=0)

            widget_input = ttk.Entry(root, font="arial")
            widget_input.grid(row=0, column=1)

            widget_othe_input = ttk.Entry(root, font="arial black")
            widget_othe_input.grid(row=2, column=1)
        
            widget_btn = ttk.Button(root, text="Regístrate")
            widget_btn.grid(row=3, column=1)
        
            root.mainloop()
        else:
          # Si no, cargamos la versión en terminal
            print("\nEl juego se generará en la terminal. Por favor espere un momento....\n")
            sleep(1)

            while True
            
                print("""
  ✓ Adivina un número del 1 al 100 (Escribe "1")
  ✓ Mapa y exploración (Escribe "2")
            """
)
            
                question = input("Elige un juego: ").strip()
            
                game_in_terminal(question)

    except EOFError:
        try:
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
        except Tcl.Error as e:
            print(f"Error fatal de interacción: {e}, usted no está en un entorno interactivo de terminal, ni en un entorno interactivo de interfaz gráfica (GUI). El problema finalizará porqué no hay entorno interactivo ni interfaz para interactuar con usuario :(")
            sys.exit()
