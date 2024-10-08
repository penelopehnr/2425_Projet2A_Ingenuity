import keyboard

def press_keyboard():
    print("Appuyez sur des touches (appuyez sur 'Esc' pour quitter)")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
            print(f"Touche pressée : {event.name}")
	        return event
	
        if event.name == 'esc':
            break

while True:
		mess = press_keyboard
    
        if not data:
            break
		
        message = data.decode(mess)
    
        if message=='Z':
			envoi_uart(message)
			
        elif message=='S':
			envoi_uart(message)