import sys
import pygame  # Importer pygame pour gérer le son
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QDialog, QLineEdit, QFormLayout, QDialogButtonBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt


class HeightDialog(QDialog):
    """Boîte de dialogue pour entrer la hauteur."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Height")
        self.setFixedSize(300, 150)  # Taille fixe pour la boîte de dialogue
        self.height_chosen = None  # Variable pour stocker la hauteur

        # Layout principal
        layout = QFormLayout()

        # Champ de saisie pour entrer la hauteur
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
        """Valider l'entrée si elle est un entier."""
        input_text = self.input_field.text()
        if input_text.isdigit():  # Vérifier si c'est un entier positif
            self.height_chosen = int(input_text)
            self.accept()
        else:
            self.input_field.setText("")  # Réinitialiser le champ en cas d'entrée non valide
            self.input_field.setPlaceholderText("Invalid input, try again")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.command = ""  # Initialiser la variable command
        self.background_label = QLabel(self)  # Label pour le fond
        self.background_toggle = False  # Variable pour alterner entre les deux fonds
        self.height_chosen = None  # Variable pour stocker la hauteur choisie
        self.build_ui()
        pygame.mixer.init()  # Initialiser le module audio de Pygame

    def build_ui(self):
        # Configurer la fenêtre principale
        self.setWindowTitle("Control Panel")
        self.showFullScreen()  # Fenêtre en plein écran

        # Charger l'image de fond
        self.update_background()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Aligner les widgets en haut
        self.main_layout.setContentsMargins(10, 10, 10, 10)  # Marges de la fenêtre principale

        # Ajouter un espace flexible pour déplacer le texte plus bas ou plus haut
        self.spacer_top = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(self.spacer_top)

        # Label pour afficher le texte en grand
        self.display_label = QLabel("", self)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)  # Aligner en haut au centre
        self.display_label.setStyleSheet("""
            font-size: 75px;
            color: #ffffffff;
            background-color: transparent;  /* Légère transparence sur le fond du texte pour le faire ressortir */
        """)
        self.display_label.setFixedHeight(100)  # Fixer une hauteur pour éviter que le layout change
        self.main_layout.addWidget(self.display_label)

        # Ajouter un espace flexible au-dessus des boutons
        spacer_middle = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacer_middle)

        # Layout horizontal pour les boutons
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrer les boutons horizontalement
        button_layout.setSpacing(140)  # Espacement entre les boutons

        # Ajouter les boutons avec des textes et associer les sons
        self.add_button("Launch", "Launch.mp3", button_layout)
        self.add_button("Height", "Height.mp3", button_layout)
        self.add_button("Photo", "Photo.mp3", button_layout)

        # Ajouter le layout des boutons à la fenêtre
        self.main_layout.addLayout(button_layout)

        # Ajouter un spacer fixe pour contrôler la distance depuis le bas
        spacer_bottom = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.main_layout.addItem(spacer_bottom)

        # Appliquer le layout principal
        self.setLayout(self.main_layout)

    def update_background(self):
        # Choisir l'image de fond selon la valeur de background_toggle
        if self.background_toggle:
            background_image_path = "Background2.png"
        else:
            background_image_path = "Background1.png"
        
        pixmap = QPixmap(background_image_path)
        if pixmap.isNull():
            print(f"Erreur : impossible de charger l'image {background_image_path}.")
        else:
            self.background_label.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding))
            self.background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.background_label.lower()  # Assurez-vous que l'image de fond est derrière les autres widgets

    def add_button(self, name, sound_file, layout):
        button = QPushButton("", self)  # Ne pas mettre de texte
        button.setFixedSize(180, 180)  # Taille carrée pour les boutons
        button.setStyleSheet("""
            background-color: transparent;  /* Rendre le bouton transparent */
            border: none;  /* Enlever la bordure */
        """)
        button.clicked.connect(lambda: self.display_button_name(name, sound_file))
        layout.addWidget(button)

    def display_button_name(self, name, sound_file):
        # Si le bouton "Launch" est pressé, alterner l'image de fond et changer le texte
        if name == "Launch":
            self.background_toggle = not self.background_toggle  # Alterner la valeur
            self.update_background()  # Mettre à jour l'image de fond
            if self.background_toggle:
                self.display_label.setText("Take-off")  # Afficher "Take-off" quand on passe à Background2
            else:
                self.display_label.setText("Landing")  # Afficher "Landing" quand on revient à Background1
        
        elif name == "Height":
            self.open_height_dialog()  # Ouvrir la boîte de dialogue pour entrer la hauteur
        
        elif name == "Photo":
            self.display_label.setText("Photo")  # Afficher "Photo" peu importe l'image de fond

        # Jouer le son du bouton
        self.play_sound(sound_file)  # Jouer le son du bouton

    def open_height_dialog(self):
        """Ouvre une boîte de dialogue pour entrer une hauteur."""
        dialog = HeightDialog(self)
        if dialog.exec():  # Si l'utilisateur clique sur "OK"
            self.height_chosen = dialog.height_chosen
            self.display_label.setText(f"Height -> {self.height_chosen}m")  # Afficher la hauteur choisie

    def play_sound(self, sound_file):
        # Jouer le son correspondant au bouton
        pygame.mixer.music.load(sound_file)  # Charger le fichier audio
        pygame.mixer.music.play()  # Jouer le son

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
