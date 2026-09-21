from PySide6.QtWidgets import QApplication, QLabel, QTextEdit, QButtonGroup, QRadioButton, QGroupBox, QPushButton, \
    QFrame, QVBoxLayout, QHBoxLayout, QLineEdit, QDialog, QMessageBox
import math


class ProbabilitesListe(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Probabilités d'un liste")

        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)

        self.disposition_liste = QHBoxLayout()
        self.libelle_liste = QLabel("Liste d'éléments")
        self.disposition_liste.addWidget(self.libelle_liste)
        self.liste_elements = QTextEdit()
        self.disposition_liste.addWidget(self.liste_elements)
        self.disposition_principale.addLayout(self.disposition_liste)

        self.groupe_options = QGroupBox()
        self.button_group_options = QButtonGroup()
        self.disposition_options = QVBoxLayout()

        self.option_combinaisons = QRadioButton("Combinaisons possibles")
        self.disposition_options.addWidget(self.option_combinaisons)
        self.option_combinaisons.setChecked(True)

        self.options_permutations = QRadioButton("Permutations possibles")
        self.disposition_options.addWidget(self.options_permutations)

        self.groupe_options.setLayout(self.disposition_options)
        self.button_group_options.addButton(self.option_combinaisons)
        self.button_group_options.addButton(self.options_permutations)

        self.disposition_nb_elements = QHBoxLayout()
        self.libelle_nb_elements = QLabel("Nombre d'éléments choisis")
        self.input_nb_elements = QLineEdit()
        self.disposition_nb_elements.addWidget(self.libelle_nb_elements)
        self.disposition_nb_elements.addWidget(self.input_nb_elements)

        self.disposition_options.addLayout(self.disposition_nb_elements)
        self.disposition_principale.addWidget(self.groupe_options)

        self.bouton_calculer = QPushButton("Calculer")
        self.bouton_calculer.clicked.connect(self.calculer)
        self.disposition_principale.addWidget(self.bouton_calculer)

    def calculer(self):
        texte = self.liste_elements.toPlainText()
        elements = texte.split("\n")
        nombre_elements_choisis = int(self.input_nb_elements.text())
        nombre_variations = 0
        option_comb = True if self.option_combinaisons.isChecked() else False

        if self.option_combinaisons.isChecked():
            nb_variations = math.comb(len(elements), nombre_elements_choisis)
        else:
            nb_variations = math.perm(len(elements), nombre_elements_choisis)

        QMessageBox.information(self, "Résultat", f"{'Nombre de combinaisons: ' if option_comb else
        'Nombre de permutations: '} {nb_variations}")


app = QApplication()
pl = ProbabilitesListe()
pl.show()
app.exec()
