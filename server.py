import socket
import pygame
import sqlite3
import threading as thr
import sys

HOST = 'localhost'
PORT = 8080

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
