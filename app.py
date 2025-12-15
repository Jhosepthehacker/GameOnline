
# ==========================
#   Importación de módulos
# ==========================

import sys                  # Para salir del programa si es necesario
import os
import requests
import sqlite3 as sql       # Para manejar la base de datos SQLite  # Para posibles hilos (no usado aún)
from tkinter import *       # Para la interfaz gráfica
from tkinter import ttk, messagebox, Toplevel
from time import sleep      # Para hacer pausas (simular carga)

# ==========================
#   Clase Base de Datos
# ==========================

class DataBase:
    def __init__(self, conn):
        self.conn = conn
        # Guardamos y cerramos la conexión inicial
        self.conn.commit()
        self.conn.close()

    def sql_command(self, command):
        try:
            self.conn = sql.connect("logs_game.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute(command)

            self.data = self.cursor.fetchall()
            return self.data
        finally:
            self.conn.commit()
            self.conn.close()

class ConnectToServer:
	def __init__(self):
		self.API_URL = "https://gameserver-jly8.onrender.com"

    def get_message_of_welcome(self):
		self.response = requests.get(self.API_URL)

        self.json = response.json()
        self.message = json["message"]
        self.status = json["status"]

        return self.message, self.status
    def send_data_of_users():
        self.API_URL = "https://gameserver-jly8.onrender.com"
		self.response = request.post(self.API_URL)

        self.json = response.json()
        self.status = json["status"]
        

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
        pass

    map = [
       list("  ###########    #########"),
       list("  # @       #####        #"),
       list("  #     E            H   #"),
       list("  #         #####        #"),
       list("  ##########     #########")
]

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
            sleep(1)
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

      # Preguntamos al usuario su nombre
user_name = input("¿Cómo te llamas?: ").title()

print("\nLa contraseña a crear, protegerá sus datos")
    
enter_password = input(f"\n¿{user_name}, podría ingresar una nueva contraseña para crear?: ")

print(f"\nGracias por su cooperación {user_name} :)")

conn = sql.connect("logs_game.db")
app = DataBase(conn)
app.sql_command(
	"""CREATE TABLE IF NOT EXISTS user(
	      id INTEGER,
		  name TEXT,
		  age INTEGER,
		  trys INTEGER
	);"""
)

# Por si acaso se añadido la columna 'id'

is_insert = app.sql_command("SELECT trys FROM user;")

if is_insert[0][0] < 1:
    for i in user_name:
        if i in (';', '(', ')', "'", '*'):
            print("Solo se aceptan letras (no carácteres ni números)")
            break
        elif user_name.split().strip() in ("SELECT", "DROP", "WHERE", "UPDATE", "SET", "select", "drop", "where", "update", "set"):
            print("No se aceptan comandos SQL en el input")
            break
        else:
            app.sql_command(f"INSERT INTO user (id, name, trys) VALUES (1, '{user_name}', 1);")
            break
    
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

    print("""
  ✓ Adivina un número del 1 al 100 (Escribe "1")
  ✓ Mapa y exploración (Escribe "2")
          """
)
    question = input("Elige un juego: ").strip()
    game_in_terminal(question)
