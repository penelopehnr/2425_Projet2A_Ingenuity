# Executer server.py sur la rasberry et Client.py ici 


## Libs
import socket
import time
import picamera
import subprocess
import serial 
import keyboard

## Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Écoute sur tous les interfaces réseau
server_socket.listen(1)
print("En attente de connexion...")

conn, addr = server_socket.accept()
print(f"Connexion établie avec {addr}")


## Config port serie 
ser = serial.Serial(port='/dev/ttyAMA0',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
CommandList= ["Command List : ", "P : Picture", "H : Height infos", "F : Stop", "Z = Go Up", "S = Go Down"]
print(" ")

for elmt in CommandList : 
	print(elmt)
    

## Fonction prise de photo 
def prendre_photo(i):

	photo_path = "Photo"+str(i)+".jpg"
	command = "raspistill -o {}".format(photo_path)

	try:
		subprocess.run(command, shell=True, check=True)
		print("succes")

	except subprocess.CalledProcessError as e:
		print("Camera Error",e)


## Fonction envoi donnes vers STM
def envoi_uart(data):
	if ser.isOpen():
		ser.write(data.encode())
		print("Data sent :", data)
	else : 
		print("No Access to serial port")


## Reception touche clavier
import keyboard
def press_keyboard():
    print("Appuyez sur des touches (appuyez sur 'Esc' pour quitter)")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
            print(f"Touche pressée : {event.name}")
            return event
	
    if event.name == 'esc':
        pass


## Initialisation de la caméra
camera = picamera.PiCamera()
Nb_photo = 0

## Boucle
try :
    while True:
        mess = press_keyboard()
    
        if not mess:
            break
		
        message = mess.decode()
    
        if message == 'Z':
            envoi_uart(message)
			
        elif message == 'S':
            envoi_uart(message)

        #if message == 'H':
            # A voir apres avec le TOF

        elif message == 'P':
            Nb_photo += 1
            prendre_photo(Nb_photo)

        elif message == 'F':
            ser.close()
            break

except KeyboardInterrupt:
	print("Stop")
	
finally : 
	ser.close()

## Closes
conn.close()
camera.close()