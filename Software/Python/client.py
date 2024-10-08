import socket

# Remplace 'adresse_ip_pi' par l'adresse IP de ton Raspberry Pi
ip_pi = '192.168.0.235'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_pi, port))



while True:
    message = input("Entrez un message à envoyer (ou 'quit' pour quitter) : ")
    if message.lower() == 'quit':
        break
    client_socket.send(message.encode())

    if message.lower() == 'take_picture':
        print("Commande pour prendre une photo envoyée.")
        
        client_socket.close()