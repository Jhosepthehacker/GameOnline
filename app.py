import time # Se importa la librería "time" para pausar el hilo principal de la app por un tiempo específico (simular carga)
import random # Se importa la librería "random" para obtener un valor aleatorio
from tkinter import * # Se importa todo sobre la librería "tkinter" para la UI main (interfaz de usuario principal)
from tkinter import messagebox, ttk, Toplevel # Se importa "messagebox" para cajas de mensajes y proporcionar información a el usuario, se agrega de importación "ttk" para realizar la interfaz gráfica más moderna y bonita, e incluímos (importamos) "Toplevel" para diseñar ventanas secundarias (otras ventanas), esto se importa desde tkinter

app = Tk() # Se inicia el objeto para diseñar la ventana principal
app.title("Graphical Window") # Se le agrega un título llamado "Graphical Window" a la ventana
app.geometry("400x400") # Se declara una geometría de "400x400" a la ventana

list_of_numbers = []
add_number = 0

for i in range(1, 101):
    add_number += 1
    
    number_string = str(add_number)
    list_of_numbers.append(number_string)

# --- Categoría de funciones ---

# [*] Algoritmo de color del tema (cambio)

def theme_background_color(color): # Se declara una función llamada "theme_background_color" para cambiar el tema de la ventana
    if color == "white": # Se comprueba si el valor de la variable "color" es igual a "white"
        app.config(bg="#ffffff") # Si la condición se evalúa dn True, entonces se cambia el fondo de la ventana a blanco intenso (#ffffff)
    elif color == "black": # Se comprueba si el valor de la variable "color" es igual a "black"
        app.config(bg="#222222") # Si la condición evalúa en True, entonces se cambia el fondo de la ventana a gris oscuro (#222222)
    else:                        # De lo contrario (si todas las condiciones evaluaron en False, se lanza una caja de mensaje de error de especificación en el color (no se recibió un color correcto, aunque solo esto es una medida de seguridad extra)
        messagebox.showerror(
            title="Error de especificación de color",
            message="No se pudo asignar correctamente el color de fondo a la UI"
        )

def process_integers():
    global list_of_numbers
    integers = widget_input.get()
    
    if integers in list_of_numbers:
        integers = int(integers)
    else:
        print("ValueError: Error in the input, 'str' can't converssion to 'int'")
        
        messagebox.showerror(
          title="ValueError",
          message="Por favor solo ingrese números"
        )
        return None

    if integers > number_random:
        messagebox.showinfo(
          title="Mensaje del juego",
          message="El número ingresado es demasiado alto"
        )
    elif integers < number_random:
        messagebox.showinfo(
          title="Mensaje del juego",
          message="El número ingresado es demasiado bajo"
        )
    elif integers == number_random:
        messagebox.showinfo(
          title="Mensaje del juego",
          message="¡Felicidades, has ganado!"
        )
        
        question = messagebox.askquestion(
          title="Pregunta",
          message="¿Deseas continuar?"
        )
        
        if question == "yes":
            time.sleep(0.2)
            app.destroy()
        else:
            start_game()

def start_game():
    time.sleep(0.2)

    number_random = random.randint(1, 100)

    widget_title.destroy()
    widget_start_game_button.destroy()
    
    app.config(bg="#aaaaaa")
    
    menu_bar = Menu(app)
    
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Claro", command=lambda: theme_background_color("white"))
    file_menu.add_command(label="Oscuro", command=lambda: theme_background_color("black"))
    
    menu_bar.add_cascade(label="Tema", menu=file_menu)
    
    widget_text = Label(app, text="Adivina un número del 1 al 100", bg="#ffffff", fg="#0000ff")
    widget_text.grid(row=0, column=1, pady=20)
    
    widget_input = ttk.Entry(app)
    widget_input.grid(row=1, column=1)

    widget_send_integers_button = ttk.Button(
        app, 
        text="Enviar", 
        command=process_integers
      )
    widget_send_integers_button.grid(row=2, column=1, pady=20)
    
    app.config(menu=menu_bar)

    global widget_input, number_random
    
    messagebox.showwarning(
      title="Advertencia",
      message="¡El juego puede presentar problemas (en desarrollo)"
    )

app.columnconfigure(0, weight=3)
app.columnconfigure(2, weight=2)
app.columnconfigure(3, weight=1)

widget_title = Label(app, text="Game")
widget_title.grid(row=0, column=1, pady=20)

widget_start_game_button = ttk.Button(
    app, 
    text="Start Game", 
    command=start_game
)
widget_start_game_button.grid(row=1, column=1)

app.config(bg="#6200d2")
app.mainloop()
