import sys
import pygame  # Importer pygame pour gérer le son
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QIcon, QKeyEvent
from PyQt6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.command = ""  # Initialiser la variable command
        self.background_label = QLabel(self)  # Label pour le fond
        self.displayed_image = QLabel(self)  # Label pour afficher l'image entre les boutons et le texte
        self.build_ui()
        pygame.mixer.init()  # Initialiser le module audio de Pygame

    def build_ui(self):
        # Configurer la fenêtre principale
        self.setWindowTitle("Button Click Display")
        self.showFullScreen()  # Fenêtre en plein écran

        # Charger l'image de fond
        self.update_background()

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(50, 50, 50, 50)  # Marges générales

        # Spacer pour centrer verticalement le texte
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # Ajouter un espace au-dessus et en-dessous du texte pour le centrer
        main_layout.addItem(spacer_top)

        # Label pour afficher le texte en grand
        self.display_label = QLabel("", self)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_label.setStyleSheet("font-size: 36px; color: #333;")
        main_layout.addWidget(self.display_label)

        # Ajouter un espace flexible en bas pour pousser le texte vers le centre
        main_layout.addItem(spacer_bottom)

        # Ajouter un label pour l'image à afficher après avoir cliqué
        self.displayed_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.displayed_image)

        # Layout horizontal pour les boutons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(200)  # Espacement entre les boutons

        # Ajouter les boutons avec des textes et associer les sons
        self.add_button("Set Height", "Height.mp3", "1.png", button_layout)
        self.add_button("Launch", "Launch.mp3", "2.png", button_layout)
        self.add_button("Picture", "Photo.mp3", "3.png", button_layout)

        # Ajouter un espace flexible réduit au-dessus pour descendre les boutons
        main_layout.addStretch(10)
        main_layout.addLayout(button_layout)
        main_layout.addStretch(1)  # Petit espace en bas pour ne pas les coller au bord

        # Appliquer le layout principal
        self.setLayout(main_layout)

    def update_background(self):
        # Vérifier si l'image de fond existe
        background_image_path = "Background.png"
        pixmap = QPixmap(background_image_path)
        if pixmap.isNull():
            print(f"Erreur : impossible de charger l'image {background_image_path}.")
        else:
            self.background_label.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding))
            self.background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.background_label.lower()  # Assurez-vous que l'image de fond est derrière les autres widgets

    def add_button(self, name, sound_file, image_path, layout):
        button = QPushButton(name, self)
        button.setFixedSize(300, 150)  # Taille carrée pour les boutons
        button.setStyleSheet("""
            background-color: white;
            font-size: 16px;
            border: 4px solid black;  /* Bordure noire et épaissie */
            border-radius: 25px;  /* Bordures arrondies */
        """)
        button.clicked.connect(lambda: self.display_button_name(name, sound_file, image_path))
        layout.addWidget(button)

    def display_button_name(self, name, sound_file, image_path):
        # Afficher le nom du bouton dans le label
        self.display_label.setText(f"Command: {name}")
        self.command = name  # Mettre à jour la variable command avec le nom du bouton
        self.play_sound(sound_file)  # Jouer le son du bouton
        self.display_image(image_path)  # Afficher l'image associée au bouton
        print(self.command)  # Afficher la valeur de la variable command dans la console

    def play_sound(self, sound_file):
        # Jouer le son correspondant au bouton
        pygame.mixer.music.load(sound_file)  # Charger le fichier audio
        pygame.mixer.music.play()  # Jouer le son

    def display_image(self, image_path):
        # Charger et afficher l'image correspondant au bouton cliqué
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Erreur : impossible de charger l'image {image_path}.")
        else:
            self.displayed_image.setPixmap(pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio))
            self.displayed_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def resizeEvent(self, event):
        # Redimensionner l'image de fond à chaque redimensionnement de la fenêtre
        self.update_background()

    def keyPressEvent(self, event: QKeyEvent):
        # Fermer la fenêtre si la touche Échap est pressée
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
