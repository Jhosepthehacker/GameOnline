BLUE_COLOR= "\e[34m"
GREEN_COLOR= "\e[33m"

echo "${BLUE_COLOR}-----------------------------"
echo "${GREEN_COLOR}            SETUP            "
echo "${BLUE_COLOR}-----------------------------\n"

apt install python3
sleep 1

apt install python-tk
sleep 1

apt install pip
sleep 1

# Aúnque hayan librerías preinstaladas en python, igualmente hay que asegurarse de instalarlas bien

pip install kivy
sleep 1

pip install sockets
sleep 1

pip install time
sleep 1

pip install threading

# Estoy ejecutando mucho "pip", se puede usar coma por cada librería o framework que se quiera instalar??
