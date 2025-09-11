import socket
from tkinter import *

root = Tk()
root.title("GameServer")
root.geometry("400x400")

widget_text = Label(text="¡Hola Bienvenido(a) al juego!", fg="lightgreen")
widget_text.place(x=280, y=60)

widget_btn = Button(text="Botón")

root.mainloop()
