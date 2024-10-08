from pynput import keyboard


# Variable pour stocker les touches pressées
touche_appuyee = []

def on_press(key):
    try:
        # Ajoute la touche pressée à la liste
        touche_appuyee.append(key.char)
    except AttributeError:
        # Pour les touches spéciales (comme Shift, Ctrl, etc.)
        touche_appuyee.append(str(key))

    print(f"Touche pressée : {key}")

while True : 
    on_press(key)
