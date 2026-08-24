from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Titre de la fenetre
        self.setWindowTitle("PySide")

        bouton_fermer = QPushButton(text="Fermer")
        # connecter l'evenement du click a la fonction close de la fenetre
        bouton_fermer.pressed.connect(self.close)

        self.setCentralWidget(bouton_fermer)
        # Affichage de la fenetre
        self.show()


# Creation de l'application
app = QApplication(sys.argv)
# Creation de la fenetre (la classe ci-haut)
w = MainWindow()

# execution
app.exec()
