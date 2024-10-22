# Executer sudo python3 server.py sur la rasberry et Client.py ici 


## Libs
import socket
import time
import subprocess
import serial 
import keyboard

## Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Écoute sur tous les interfaces réseau
server_socket.listen(1)
print("Waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")


## Config port serie 
ser = serial.Serial(port='/dev/ttyAMA0',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
   

## Fonction prise de photo 
def prendre_photo(i):

	photo_path = "Photo"+str(i)+".jpg"
	command = "raspistill -o {}".format(photo_path)

	try:
		subprocess.run(command, shell=True, check=True)
		print("Photo successfully taken :",photo_path)

	except subprocess.CalledProcessError as e:
		print("Camera Error",e)


## Fonction envoi donnes vers STM
def envoi_uart(data):
	if ser.isOpen():
		ser.write(data.encode())
		print("Data sent :", data)
	else : 
		print("No Access to serial port")


## Reception touche clavier a faire plus tard 
## Fleche du haut incrémentera de 1cm la hauteur envoyee
"""import keyboard
def press_keyboard():
    print("Appuyez sur des touches (appuyez sur 'Esc' pour quitter)")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
            print(f"Touche pressée : {event.name}")
            return event
	
    if event.name == 'esc':
        pass"""


## Initialisation de la caméra
Nb_photo = 0

## Code principal
try:
    while True:
        # Vérification des données du client
        print("")
        print("Waiting for customer message...")
        client_message = conn.recv(1024).decode()
        if client_message:
            print(f"Customer's message : {client_message}")

        else : 
              break 
        
        if "height" in client_message:
            envoi_uart(client_message)

        elif client_message == 'take_photo':
            Nb_photo += 1
            prendre_photo(Nb_photo)

        elif client_message == 'quit':
            ser.close()
            break
        
except KeyboardInterrupt:
    print("Stop")

finally:
    ser.close()
    conn.close()