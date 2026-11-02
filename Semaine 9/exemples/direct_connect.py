from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QLineEdit, QWidget, QFrame


class Fenetre(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple connection direct")
        self.setMinimumSize(QSize(200, 50))
        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)
        self.libelle = QLabel("")
        self.texte_edit = QLineEdit()

        # le signal textChanged du QLine Edit émet une str contenant le nouveau texte. En le connectant à la
        # fente (slot) setText du QLabel, le setText du QLabel sera appelé avec la str contenant le nouveau texte en
        # paramètre.
        # Ceci permet de ne pas avoir à écrire une méthode pour aller chercher le texte pour le setter sur le label
        self.texte_edit.textChanged.connect(self.libelle.setText)

        self.disposition.addWidget(self.libelle)
        self.disposition.addWidget(self.texte_edit)


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()
