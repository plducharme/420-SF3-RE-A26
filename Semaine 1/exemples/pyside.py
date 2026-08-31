from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton

import sys


# On hérite de la classe QMainWindow pour la personnaliser. Cette classe permet de créer une fenêtre avec des widgets
# prédéfinis.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Titre de la fenêtre
        self.setWindowTitle("PySide")

        self.bouton_fermer = QPushButton(text="Fermer")
        # connecter l'événement du click à la fonction "close()" de la fenetre
        self.bouton_fermer.pressed.connect(self.close)

        self.setCentralWidget(self.bouton_fermer)


# Création de l'application
app = QApplication(sys.argv)
# Creation de la fenêtre (la classe ci-haut)
fenetre_principale = MainWindow()
# Affichage de la fenêtre
fenetre_principale.show()
# execution
app.exec()
