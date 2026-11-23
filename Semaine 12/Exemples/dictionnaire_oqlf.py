from PySide6.QtWidgets import (QApplication, QLineEdit, QTextEdit, QComboBox, QLabel, QGridLayout, QHBoxLayout,
                               QFrame, QPushButton, QGroupBox)
from PySide6.QtGui import QIcon
import pandas as pd


class DictionnaireOQLF(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dictionnaire des termes officialisés")
        self.setWindowIcon(QIcon("./images/livre.png"))

        self.disposition_principale = QGridLayout()
        self.setLayout(self.disposition_principale)

        self.barre_recherche = QLineEdit()
        self.barre_recherche.setMaxLength(25)
        self.disposition_principale.addWidget(self.barre_recherche, 1, 1)

        self.bouton_recherche = QPushButton("Recherche")
        self.bouton_recherche.clicked.connect(self.recherche)
        self.disposition_principale.addWidget(self.bouton_recherche, 1, 2)

        self.definition_text = QTextEdit()
        self.disposition_principale.addWidget(self.definition_text, 4, 1, 1, 2)

        self.resultat_recherche = QComboBox()
        self.disposition_principale.addWidget(self.resultat_recherche, 3, 1)

        self.groupe_filtres = QGroupBox("Filtres")
        self.disposition_filtres = QGridLayout()
        self.disposition_principale.addWidget(self.groupe_filtres, 2, 1, 1, 2)
        self.groupe_filtres.setLayout(self.disposition_filtres)

        self.df = pd.read_csv("termes_officialises_2026-01-14.csv")

    def recherche(self):
        pass


app = QApplication()
dico = DictionnaireOQLF()
dico.show()
app.exec()
