import sys
import pygame  # To play sounds
import socket  # To manage network connection
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QDialog, QLineEdit, QFormLayout, QDialogButtonBox)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer

class CommandWindow(QWidget):
    def __init__(self, parent, socket=None):
        super().__init__()
        self.setWindowTitle("Command Window")
        self.setFixedSize(400, 400)
        self.parent = parent  # Reference to the main window

        # Retrieve the previous height or initialize to 0
        self.height_chosen = parent.height_chosen if parent.height_chosen is not None else 0

        # Socket to send data
        self.socket = socket  # Adding the socket

        # Load background image
        self.image_label = QLabel(self)
        pixmap = QPixmap("img/Command.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.setGeometry(0, 0, 400, 400)

        # Display height
        self.height_label = QLabel(f"Height = {self.height_chosen}", self)
        self.height_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.height_label.setStyleSheet("font-size: 40px; font-weight: bold; color: black;")
        self.height_label.setGeometry(0, 400 - 20 - 50, 400, 50)  # (x, y, width, height)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

        elif event.key() == Qt.Key.Key_Up:
            if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                self.height_chosen += 10  # Increase height by 10 with Ctrl + Up Arrow
            elif event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                self.height_chosen += 1  # Increase height by 1 with Shift + Up Arrow
            else:
                self.height_chosen += 5  # Increase height by 5 with Up Arrow
            self.update_height()

        elif event.key() == Qt.Key.Key_Down:
            if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                self.height_chosen -= 10  # Decrease height by 10 with Ctrl + Down Arrow
            elif event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                self.height_chosen -= 1  # Decrease height by 1 with Shift + Down Arrow
            else:
                self.height_chosen -= 5  # Decrease height by 5 with Down Arrow
            self.update_height()

    def update_height(self):
        """Update height display and synchronize with MyWindow."""
        self.height_label.setText(f"Height = {self.height_chosen}")
        self.parent.height_chosen = self.height_chosen  # Update in the main window
        self.height_coded = "@height=" + str(self.height_chosen) + "#"
        if self.socket:  # Check if the socket is defined before sending data
            self.socket.send(self.height_coded.encode())
            print("Command sent :", self.height_coded)


# Dialog box to set height
class HeightDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Height")
        self.setFixedSize(300, 150)
        self.height_chosen = None

        # Main layout
        layout = QFormLayout()
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter an integer")
        layout.addRow("Height:", self.input_field)

        # OK/Cancel buttons
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


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        # Field for IP address
        self.ip_label = QLabel("IP Address:")
        self.ip_input = QLineEdit()
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)

        # Field for port
        self.port_label = QLabel("Port:")
        self.port_input = QLineEdit()
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)

        # OK button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_values(self):
        """Return entered values"""
        return self.ip_input.text(), self.port_input.text()
    

# Main Window
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.command = ""
        self.background_label = QLabel(self)
        self.background_toggle = False
        self.height_chosen = None
        self.connection_status = "Not Connected"
        self.server_address = None  # The IP address must be set via "Settings"
        self.socket = None  # Socket for connection
        self.display_label = QLabel("", self)  # Declaration of display_label here
        pygame.mixer.init()

        self.build_ui()

    def build_ui(self):
        self.setWindowTitle("Control Panel")
        self.showFullScreen()
        self.update_background()

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setContentsMargins(0, 100, 0, 0)

        # Connection bar
        self.top_bar = QHBoxLayout()
        self.top_bar.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.main_layout.addLayout(self.top_bar)

        # Setting button (Aligned to the left)
        self.setting_button = QPushButton("Setting", self)
        button_size = self.calculate_button_size()  # Button size
        self.setting_button.setFixedSize(button_size, button_size)
        self.setting_button.setStyleSheet("color: transparent; background-color: transparent; border-radius: 10px;")
        self.setting_button.clicked.connect(self.open_settings)
        self.top_bar.addWidget(self.setting_button)

        # Add a flexible space in the middle to separate buttons
        spacer_middle = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.top_bar.addItem(spacer_middle)

        # Connect button (Aligned to the right)
        self.connect_button = QPushButton("Connect", self)
        self.connect_button.setFixedSize(button_size, button_size)
        self.connect_button.setStyleSheet("color: transparent; background-color: transparent; border: none;")
        self.connect_button.clicked.connect(self.handle_connection_button)
        self.top_bar.addWidget(self.connect_button)

        # Label to display text
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.display_label.setStyleSheet("font-size: {}px; color: #ffffffff; background-color: transparent;".format(self.calculate_font_size(75)))
        self.display_label.setFixedHeight(100)
        self.main_layout.addWidget(self.display_label)

        spacer_middle = QSpacerItem(20, 450, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacer_middle)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.setSpacing(135)
        
        self.add_button("Command","sounds/Photo.mp3",button_layout)
        self.add_button("Photo", "sounds/Photo.mp3", button_layout)
        self.add_button("Height", "sounds/Height.mp3", button_layout)

        self.main_layout.addLayout(button_layout)

        spacer_bottom = QSpacerItem(0, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.main_layout.addItem(spacer_bottom)

        self.setLayout(self.main_layout)

    def open_command_window(self):
        self.command_window = CommandWindow(self, self.socket)
        self.command_window.show()

    def open_settings(self):
        print("Settings button clicked")  # Replace this with the settings opening logic

    def open_settings(self):
        dialog = SettingsDialog(self)
        if dialog.exec():  # If the user clicks OK
            ip, port = dialog.get_values()
            
            # Check if the port is a number
            if port.isdigit():
                self.server_address = (ip, int(port))
                print(f"New address set: {self.server_address}")  # Debugging
            else:
                print("Invalid port. Enter a number.")

    def calculate_font_size(self, base_size):
        """Calculates a font size proportional to the window size."""
        screen_size = self.size()
        return int(base_size * (screen_size.width() / 1920))  # Example: proportional to a Full HD screen

    def calculate_button_size(self):
        """Calculates button size (12% of screen width)."""
        screen_size = self.size()
        return int(screen_size.width() * 0.12)  # 12% of screen width

    def add_button(self, name, sound_file, layout):
        button = QPushButton(name, self)
        button_size = self.calculate_button_size()  # Dynamic button size
        button.setFixedSize(button_size, button_size)  # Same width and height
        button.setStyleSheet("color: transparent; background-color: transparent; border: none;")
        button.clicked.connect(lambda: self.display_button_name(name, sound_file))
        layout.addWidget(button)

    def update_background(self, image_path="img/NotConnected.png"):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.background_label.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding))
            self.background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.background_label.lower()

    def display_button_name(self, name, sound_file):
        # Check if the connection status is "Connected!" before executing an action
        if self.connection_status != "Connected!":
            print(f"Action blocked: Current state - {self.connection_status}")
            return

        # Actions associated with buttons
        elif name == "Height":
            self.open_height_dialog()
        elif name == "Command":
            self.open_command_window()
        elif name == "Photo":
            self.display_label.setText("Photo in progress...")
            self.mess_photo = 'take_photo'
            self.socket.send(self.mess_photo.encode())
            QTimer.singleShot(6000, lambda: self.display_label.setText("Photo taken"))

        # Play the associated sound
        self.play_sound(sound_file)

    def open_height_dialog(self):
        dialog = HeightDialog(self)
        if dialog.exec():
            self.height_chosen = dialog.height_chosen
            self.display_label.setText(f"Height -> {self.height_chosen}m")
            self.height_coded = "@height="+str(self.height_chosen)+"#"
            self.socket.send(self.height_coded.encode())

    def play_sound(self, sound_file):
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def handle_connection_button(self):
        if self.server_address is None:
            self.display_label.setText("Enter an IP address before connecting")  # Message in English
            return  # Stop connection attempt

        self.connect_to_server()  # If an IP address is set, try to connect

    def connect_to_server(self):
        self.connection_status = "Connecting..."
        self.update_background("img/Connexion.png")  # Set background image to "Connexion.png" during connection
        QApplication.processEvents()  # Update UI immediately

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_address))
            self.connection_status = "Connected!"
            self.update_background("img/Connected.png")
            self.connect_button.setText("Disconnect")
            return 
        except (socket.timeout, ConnectionRefusedError, socket.error) as e:
            self.connection_status = "Connection Failed"
            self.update_background("img/ConnexionFailed.png")
            QTimer.singleShot(5000, self.reset_connection_status)  # Reset after 5 seconds
            print("fail")
            return

    def disconnect_from_server(self):
        """Disconnects from the server and updates the state."""
        if self.socket:
            try:
                self.socket.close()  # Close the socket
            except Exception as e:
                print(f"Error during disconnection: {e}")
            finally:
                self.socket = None

        self.connection_status = "Not Connected"
        self.connect_button.setText("Connect")  # Revert to Connect button

    def reset_connection_status(self):
        """Resets the state to 'Not Connected'."""
        self.connection_status = "Not Connected"
        self.update_background("img/NotConnected.png")  # Reset background image

    def resizeEvent(self, event):
        """Dynamic update when resizing the window."""
        self.update_background()
        self.display_label.setStyleSheet("font-size: {}px; color: #ffffffff; background-color: transparent;".format(self.calculate_font_size(75)))
        
        # Update button size when resizing the window
        for button in self.findChildren(QPushButton):
            button.setFixedSize(self.calculate_button_size(), self.calculate_button_size())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())