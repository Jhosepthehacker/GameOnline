import socket
import threading
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
                conn.close()
                s.close()
                sys.exit()

        except OSError:
            conn.close()
            s.close()
            print("Hubo un error en la comunicación")
