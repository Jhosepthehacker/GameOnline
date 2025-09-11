import socket
import threading
import sys

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        try:
            try:
                conn, addr = s.accept()

                print(f"Conexión Exitosa con: {addr}")

                s.sendall("¡Hola, desde el servidor!".encode('utf-8'))
      
                data = s.recv(1024)
                message = data.decode()

            except KeyborardInterrupt:
                sys.exiimport socket
import threading

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)

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
            pass
