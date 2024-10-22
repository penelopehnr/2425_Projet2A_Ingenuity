import subprocess
import serial 
import time



# Config port serie #
ser = serial.Serial(port='/dev/ttyAMA0',baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

# Fonction envoi donnees #
def envoi_uart(data):
	if ser.isOpen():
		ser.write(data.encode())
		print("Data sent :", data)
	else : 
		print("No Access to serial port")
		
while True : 
	envoi_uart("U")
	





