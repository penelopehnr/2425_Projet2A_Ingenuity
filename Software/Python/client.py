# Executer sudo python3 server.py sur la rasberry et Client.py ici 

import socket

# Remplace 'adresse_ip_pi' par l'adresse IP de ton Raspberry Pi
ip_pi = '192.168.0.235'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_pi, port))

print("")
print("What do you want to do? Take a picture, stop or set the height ?")
print("")

## Liste des commandes
command_list = ["\tLeave -> stop","\tTake photo -> take_photo", "\tA Set a height -> set_height"]
print("List of available orders :")
for elmt in command_list:
    print(elmt)

while True:
    print("")
    message = input("Enter your choice : ")

    if message.lower() == 'stop':
        print("Program exit.")
        break

    elif message.lower() == 'take_photo':
        print("Command to take a photo sent.")
        client_socket.send(message.encode())

    elif message.lower() == 'set_height':
        height = float(input("Set a height : "))
        print("Height sent.",height)
        mess_height = "height="+str(height)
        client_socket.send(mess_height.encode())   

    else :
        print("Unknown Command") 
        
client_socket.close()



"""Demande une hauteur, tant qu'elle est pas atteinte on ne demande rien d'autre. 
Quand elle est atteinte, on demande ce que veut l'utilisateiur : 
atterrir, prendre une photo ou modifier la hauteur"""