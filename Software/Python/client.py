import sys
import socket
import pygame  # Pour les sons
import threading  # Pour gérer la connexion en arrière-plan
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal, QObject


class ConnectionThread(QObject):
    """Thread séparé pour gérer la connexion au Raspberry Pi."""
    connection_result = pyqtSignal(str)  # Signal émis pour transmettre l'état : "Success", "Failed", "Error"

    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port

    def run(self):
        """Effectue la tentative de connexion."""
        try:
            # Essayer de se connecter au Raspberry Pi
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(5)  # Timeout de 5 secondes pour éviter de bloquer
            client_socket.connect((self.ip, self.port))
            client_socket.close()  # Fermer la connexion si elle a réussi
            self.connection_result.emit("Success")  # Connexion réussie
        except socket.timeout:
            self.connection_result.emit("Failed")  # Échec (timeout)
        except Exception as e:
            print(f"Erreur de connexion : {e}")
            self.connection_result.emit("Error")  # Erreur inattendue


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.connection_status = "Connexion..."  # État initial
        self.connection_thread = None  # Thread pour la connexion
        self.init_ui()
        pygame.mixer.init()

    def init_ui(self):
        """Initialisation de l'interface graphique."""
        self.setWindowTitle("Control Panel")
        self.showFullScreen()

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Barre supérieure avec le bouton "Connect"
        self.top_bar = QHBoxLayout()
        self.top_bar.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.connect_button = QPushButton("Connect", self)
        self.connect_button.setFixedSize(120, 50)
        self.connect_button.setStyleSheet("font-size: 18px;")
        self.connect_button.clicked.connect(self.connect_to_raspberry)  # Lancer la connexion sur clic
        self.top_bar.addWidget(self.connect_button)
        self.main_layout.addLayout(self.top_bar)

        # Zone de texte pour afficher l'état de la connexion
        self.connection_label = QLabel(self.connection_status, self)
        self.connection_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.connection_label.setStyleSheet("font-size: 30px; color: white;")
        self.connection_label.setFixedHeight(50)
        self.main_layout.addWidget(self.connection_label)

        # Spacer pour organiser le layout
        self.spacer_top = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(self.spacer_top)

        # Label principal (pour d'autres actions ou commandes)
        self.display_label = QLabel("", self)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_label.setStyleSheet("font-size: 75px; color: white;")
        self.main_layout.addWidget(self.display_label)

        # Ajouter un spacer en bas
        spacer_bottom = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.main_layout.addItem(spacer_bottom)

        self.setLayout(self.main_layout)

    def connect_to_raspberry(self):
        """Lance la tentative de connexion au Raspberry Pi."""
        self.connection_label.setText("Connexion...")  # Affiche l'état initial
        self.connect_button.setEnabled(False)  # Désactive temporairement le bouton pour éviter les clics multiples

        # Démarre un thread pour gérer la connexion en arrière-plan
        self.connection_thread = ConnectionThread(ip="192.168.0.235", port=12345)
        self.connection_thread.connection_result.connect(self.update_connection_status)  # Gérer les résultats
        thread = threading.Thread(target=self.connection_thread.run)
        thread.daemon = True  # Assurer que le thread se ferme avec l'application
        thread.start()

    def update_connection_status(self, status):
        """Met à jour le texte selon le résultat de la connexion."""
        self.connection_status = status
        self.connection_label.setText(status)  # Affiche l'état ("Success", "Failed", ou "Error")
        self.connect_button.setEnabled(True)  # Réactive le bouton après la tentative


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
