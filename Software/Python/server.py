# Run sudo python3 server.py on the rasberry and Client.py here 


## Libs
import socket
import time
import subprocess
import serial 
import keyboard

## Socket creation
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Listen on all network interfaces
server_socket.listen(1)
print("Waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")


## Serial port configuration
ser = serial.Serial(port='/dev/ttyAMA0',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
   

## Photo-taking function 
def prendre_photo(i):

	photo_path = "Photo"+str(i)+".jpg"
	command = "raspistill -o {}".format(photo_path)

	try:
		subprocess.run(command, shell=True, check=True)
		print("Photo successfully taken :",photo_path)

	except subprocess.CalledProcessError as e:
		print("Camera Error",e)


## Send data to STM function
def envoi_uart(data):
	if ser.isOpen():
		ser.write(data.encode())
		print("Data sent :", data)
	else : 
		print("No Access to serial port")


## Camera initialization
Nb_photo = 0

## Main code
try:
    while True:
        # Verification of customer data
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