from PySide6.QtWidgets import QApplication, QFrame, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
import numpy as np


class CalculateurHypothenuse(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculateur d'hypothénuse")

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)
        self.disposition_input = QHBoxLayout()
        self.label_resultat = QLabel()
        self.disposition.addWidget(self.label_resultat)
        self.disposition.addLayout(self.disposition_input)

        self.label_adjacent = QLabel("Adjacent:")
        self.disposition_input.addWidget(self.label_adjacent)
        self.input_adjacent = QLineEdit()
        self.input_adjacent.setMask("999")
        self.input_adjacent.textChanged.connect(self.calcul_hypo)
        self.disposition_input.addWidget(self.input_adjacent)

        self.disposition_input.addWidget(self.input_adjacent)
        self.label_oppose = QLabel("Opposé:")
        self.disposition_input.addWidget(self.label_oppose)
        self.input_oppose = QLineEdit()
        self.input_oppose.setMask("999")
        self.input_oppose.textChanged.connect(self.calcul_hypo)
        self.disposition_input.addWidget(self.input_oppose)

    def calcul_hypo(self):
        if len(self.input_adjacent.text()) > 0 and len(self.input_oppose.text()):
            self.label_resultat.setText(
                str(np.linalg.norm([int(self.input_adjacent.text()), int(self.input_oppose.text())])))


app = QApplication()
ch = CalculateurHypothenuse()
ch.show()
app.exec()
