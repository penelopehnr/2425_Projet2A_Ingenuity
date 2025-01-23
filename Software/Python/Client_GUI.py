#cd C:\Users\kevin\Desktop\GitHub\2425_Projet2A_Ingenuity\Software\Python\PyQt6_Temp ; python3 TempFus.py

import sys
import pygame  # Pour jouer des sons
import socket  # Pour gérer la connexion réseau
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QDialog, QLineEdit, QFormLayout, QDialogButtonBox)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer


# Boîte de dialogue pour définir la hauteur
class HeightDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Height")
        self.setFixedSize(300, 150)
        self.height_chosen = None

        # Layout principal
        layout = QFormLayout()
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter an integer")
        layout.addRow("Height:", self.input_field)

        # Boutons OK/Annuler
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept_dialog)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def accept_dialog(self):
        input_text = self.input_field.text()
        if input_text.isdigit():
            self.height_chosen = int(input_text)
            self.accept()
        else:
            self.input_field.setText("")
            self.input_field.setPlaceholderText("Invalid input, try again")


# Fenêtre principale
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.command = ""
        self.background_label = QLabel(self)
        self.background_toggle = False
        self.height_chosen = None
        self.connection_status = "Not Connected"
        self.server_address = ("192.168.1.10", 12345)  # Adresse IP et port du Raspberry Pi
        self.socket = None  # Socket pour la connexion
        self.build_ui()
        pygame.mixer.init()

    def build_ui(self):
        self.setWindowTitle("Control Panel")
        self.showFullScreen()
        self.update_background()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Barre de connexion
        self.top_bar = QHBoxLayout()
        self.connection_label = QLabel(self.connection_status, self)
        self.connection_label.setStyleSheet("font-size: 20px; color: white;")
        self.top_bar.addWidget(self.connection_label)

        self.connect_button = QPushButton("Connect", self)
        self.connect_button.clicked.connect(self.handle_connection_button)
        self.top_bar.addWidget(self.connect_button)

        self.main_layout.addLayout(self.top_bar)

        # Espace flexible
        self.spacer_top = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(self.spacer_top)

        # Label pour afficher du texte
        self.display_label = QLabel("", self)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.display_label.setStyleSheet("font-size: 75px; color: #ffffffff; background-color: transparent;")
        self.display_label.setFixedHeight(100)
        self.main_layout.addWidget(self.display_label)

        spacer_middle = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacer_middle)

        # Layout des boutons
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.setSpacing(140)

        self.add_button("Launch", "sounds/Launch.mp3", button_layout)
        self.add_button("Height", "sounds/Height.mp3", button_layout)
        self.add_button("Photo", "sounds/Photo.mp3", button_layout)

        self.main_layout.addLayout(button_layout)

        spacer_bottom = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.main_layout.addItem(spacer_bottom)

        self.setLayout(self.main_layout)

    def update_background(self, image_path="img/NotConnected.png"):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.background_label.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding))
            self.background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.background_label.lower()

    def add_button(self, name, sound_file, layout):
        button = QPushButton("", self)
        button.setFixedSize(180, 180)
        button.setStyleSheet("background-color: transparent; border: none;")
        button.clicked.connect(lambda: self.display_button_name(name, sound_file))
        layout.addWidget(button)

    def display_button_name(self, name, sound_file):
        if name == "Launch":
            self.launch_action()
        elif name == "Height":
            self.open_height_dialog()
        elif name == "Photo":
            self.display_label.setText("Photo")
        self.play_sound(sound_file)

    def launch_action(self):
        if self.connection_status == "Connected!":
            self.background_toggle = not self.background_toggle
            self.update_background("img/ConnectedLaunch.png" if self.background_toggle else "img/ConnectedNoLaunch.png")
            self.display_label.setText("Take-off" if self.background_toggle else "Landing")

    def open_height_dialog(self):
        dialog = HeightDialog(self)
        if dialog.exec():
            self.height_chosen = dialog.height_chosen
            self.display_label.setText(f"Height -> {self.height_chosen}m")

    def play_sound(self, sound_file):
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def handle_connection_button(self):
        """Gère le clic sur le bouton de connexion."""
        if self.connection_status == "Connected!":
            self.disconnect_from_server()
        else:
            self.connect_to_server()

    def connect_to_server(self):
        self.connection_status = "Connecting..."
        self.update_background("img/Connexion.png")  # Met l'image de fond à "Connexion.png" pendant la connexion
        self.connection_label.setText(self.connection_status)
        QApplication.processEvents()  # Mettre à jour l'interface immédiatement

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(self.server_address)
            self.connection_status = "Connected!"
            self.update_background("img/ConnectedNoLaunch.png")
            self.connect_button.setText("Disconnect")
        except (socket.timeout, ConnectionRefusedError, socket.error) as e:
            self.connection_status = "Connexion Failed"
            self.connection_label.setText(self.connection_status)
            self.update_background("img/ConnexionFailed.png")
            QTimer.singleShot(5000, self.reset_connection_status)  # Réinitialiser après 5 secondes
            print("fail")
            return
        finally:
            self.connection_label.setText(self.connection_status)

    def disconnect_from_server(self):
        """Déconnecte du serveur et met à jour l'état."""
        if self.socket:
            try:
                self.socket.close()  # Ferme le socket
            except Exception as e:
                print(f"Erreur lors de la déconnexion : {e}")
            finally:
                self.socket = None

        self.connection_status = "Not Connected"
        self.connection_label.setText(self.connection_status)
        self.connect_button.setText("Connect")  # Revenir au bouton Connect

    def reset_connection_status(self):
        """Réinitialise l'état à 'Not Connected'."""
        self.connection_status = "Not Connected"
        self.connection_label.setText(self.connection_status)
        self.update_background("img/NotConnected.png")  # Réinitialiser l'image de fond

    def resizeEvent(self, event):
        self.update_background()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
