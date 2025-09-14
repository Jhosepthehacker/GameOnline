import socket
import kivy
import sys
import sqlite3
import threading as thread
from tkinter import *
from time import sleep

# Posibles errores de la clase 'ConnectServer', de su método 'connect_server'.

class ConnectServer:

    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 8080

def connect_server(self):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((self.HOST, self.PORT))

        while True:
            self.data_receive = s.recv(1024)
            self.message = self.data_receive.decode()

            print(f"Mensaje recibido: {self.message}")

            s.sendall("¡Hola, desde el cliente!".encode('utf-8'))

if __name__ == '__main__':
    try:
        app = ConnectServer()
    except OSError:
        pass

try:
    user_name = input("¿Cómo te llamas?: ").title()

    response = input(f"\n¿{user_name}, usted está en un entorno gráfico (GUI)?: ").lower()
    response.strip()

    if response == "si" or response == "sí":
        root = Tk()
        root.title("GameServer")
        root.geometry("400x400")

        widget_text = Label(text="¡Hola Bienvenido(a) al juego!", fg="lightgreen")
        widget_text.grid(row=0, column=1)

        widget_btn = Button(text="Botón")
        widget_btn.grid(row=1, column=1)

        root.mainloop()
    else:
        print("El juego se generará en la terminal. Por favor espere un momento....")
        sleep(1)

except EOFError:
    print("No estás en un entorno interactivo de terminal o consola")
    root = Tk()
    root.title("GameServer")
    root.geometry("400x400")

    widget_text = Label(text="¡Hola Bienvenido(a) al juego!", fg="lightgreen")
    widget_text.grid(row=0, column=1)

    widget_btn = Button(text="Botón")
    widget_btn.grid(row=1, column=1)

    root.mainloop()
