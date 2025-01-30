# Run sudo python3 server.py on the rasberry and Client.py here 

import socket

# Replace 'adresse_ip_pi' with the IP address of your Raspberry Pi
ip_pi = '192.168.0.235'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_pi, port))

## Order list
command_list = ["\tLeave -> stop","\tTake photo -> take_photo", "\tA Set a height -> set_height"]
print("List of available orders :")
for elmt in command_list:
    print(elmt)

print("")
print("What do you want to do? Take a picture, stop or set the height ?")
print("")

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
        mess_height = "@"+"height="+str(height)+"#"
        client_socket.send(mess_height.encode())   

    else :
        print("Unknown Command") 
        
client_socket.close()