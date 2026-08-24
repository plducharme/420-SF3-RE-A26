from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel, QWidget
import sys
from random import choice


class FenetrePrincipale(QMainWindow):
    label_equations = [
        "a^2 + b^2 = c^2",
        "ln(xy) = ln(x) + ln(y)",
        "i^2 = -1",
        "E = mc^2"
    ]

    def __init__(self):
        super().__init__()
        # Titre de la fenêtre
        self.setWindowTitle("PySide")

        # Création du label
        self.label = QLabel()
        self.label.setText("Cliquez pour une équation")

        # Création du bouton
        self.bouton_changer = QPushButton("Changer")
        # connecter l'évènement du click à la fonction pour gérer les changements
        self.bouton_changer.pressed.connect(self.handle_button_ok)

        # Ajout du layout et du container
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.bouton_changer)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        # Affichage de la fenêtre
        self.show()

    def handle_button_ok(self):
        # Output à la console
        print("Click")
        # Changement du texte du label lorsque la méthode est appelée
        self.label.setText(choice(self.label_equations))


# Creation de l'application
app = QApplication(sys.argv)
# Creation de la fenetre (la classe ci-haut)
w = FenetrePrincipale()
# execution
app.exec()