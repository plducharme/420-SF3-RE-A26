from PySide6.QtWidgets import QApplication, QVBoxLayout, QProgressBar, QMainWindow, QTextEdit, QPushButton, QFrame


class BarreProgressionEx(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple barre de progression")

        cadre_principale = QFrame()
        self.setCentralWidget(cadre_principale)
        disposition = QVBoxLayout()
        cadre_principale.setLayout(disposition)

        bouton_charger = QPushButton("Charger Frankenstein")
        bouton_charger.clicked.connect(self.bouton_charger_clicked)
        disposition.addWidget(bouton_charger)

        self.texte_livre = QTextEdit()
        disposition.addWidget(self.texte_livre)

        self.barre_progression_principale = QProgressBar()
        disposition.addWidget(self.barre_progression_principale)

        self.barre_progression_statut = QProgressBar()

        self.statusBar().addWidget(self.barre_progression_statut)

    def bouton_charger_clicked(self):
        self.barre_progression_principale.setValue(0)
        self.barre_progression_statut.setValue(0)
        self.texte_livre.clear()

        with open("frankenstein.txt", mode="r", encoding="utf8") as livre:
            lignes = livre.readlines()
            self.barre_progression_principale.setMaximum(len(lignes) - 1)
            self.barre_progression_statut.setMaximum(len(lignes) - 1)
            for ligne in lignes:
                self.texte_livre.append(ligne)
                self.barre_progression_principale.setValue(self.barre_progression_principale.value()+1)
                self.barre_progression_statut.setValue(self.barre_progression_statut.value() + 1)


app = QApplication()
bpe = BarreProgressionEx()
bpe.show()
app.exec()
