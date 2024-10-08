import subprocess
import serial 
import time



# Config port serie #
ser = serial.Serial(port='/dev/ttyAMA0',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
nb = 0
CommandList= ["Command List : ", "P : Picture", "H : Height infos", "Sto : Stop", "E = UART"]
print(" ")


for elmt in CommandList : 
	print(elmt)

# Fonction prise de photo #
def prendre_photo(i):

	photo_path = "Photo"+str(i)+".jpg"
	command = "raspistill -o {}".format(photo_path)

	try:
		subprocess.run(command, shell=True, check=True)
		print("succes")

	except subprocess.CalledProcessError as e:
		print("Camera Error",e)



# Fonction envoi donnees #
def envoi_uart(data):
	if ser.isOpen():
		ser.write(data.encode())
		print("Data sent :", data)
	else : 
		print("No Access to serial port")


try :
	while True : 
		Commande = str(input("Waiting for a command :"))
		
		if Commande =='E':
			envoi_uart('C')


		if Commande =='C':
			nb += 1
			prendre_photo(nb)

		elif Commande in 'NSWE' :
			envoi_uart(Commande)

		elif Commande == 'STOP':
			print("Stop")
			ser.close()
			break

		else : 
			print("Invalid Command")

except KeyboardInterrupt:
	print("Stop")
finally : 
	ser.close()




