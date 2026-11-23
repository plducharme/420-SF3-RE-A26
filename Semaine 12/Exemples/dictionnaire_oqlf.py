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

        self.definition_texte = QTextEdit()
        self.disposition_principale.addWidget(self.definition_texte, 4, 1, 1, 2)

        self.resultat_recherche = QComboBox()
        self.resultat_recherche.currentIndexChanged.connect(self.resultat_selectionne)
        self.disposition_principale.addWidget(self.resultat_recherche, 3, 1)
        self.terme_anglais = QLabel()
        self.terme_anglais.setStyleSheet("color: green")
        self.disposition_principale.addWidget(self.terme_anglais, 3, 2)

        self.groupe_filtres = QGroupBox("Filtres")
        self.disposition_filtres = QGridLayout()
        self.disposition_principale.addWidget(self.groupe_filtres, 2, 1, 1, 2)
        self.groupe_filtres.setLayout(self.disposition_filtres)

        self.df = pd.read_csv("termes_officialises_2026-01-14.csv")
        self.df["Definition"].fillna("").astype("str")

    def recherche(self):
        self.resultat_recherche.clear()
        recherche_str = self.barre_recherche.text()
        series_termes = self.df["Termes_Officialises"]
        resultat = series_termes[series_termes.str.contains(recherche_str)]

        for index, terme in enumerate(resultat):
            self.resultat_recherche.addItem(terme, resultat.index[index])

    def resultat_selectionne(self):
        selection = self.resultat_recherche.currentData()
        if not selection:
            self.terme_anglais.setText("")
            return
        item = self.df.iloc[selection]
        definition = item["Definition"]
        if str(definition) == "nan":
            self.definition_texte.setText("Définition non disponible!")
        else:
            self.definition_texte.setText(definition)

        self.terme_anglais.setText(item["Equivalent_anglais"])


app = QApplication()
dico = DictionnaireOQLF()
dico.show()
app.exec()
