import socket
import threading
from tkinter import *

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

root = Tk()
root.title("GameServer")
root.geometry("400x400")

widget_text = Label(text="¡Hola Bienvenido(a) al juego!", fg="lightgreen")
widget_text.place(x=280, y=60)

widget_btn = Button(text="Botón")
widget_btn.place(x=400, y=120)

root.mainloop()
