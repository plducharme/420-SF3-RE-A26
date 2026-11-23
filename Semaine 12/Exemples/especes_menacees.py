from PySide6.QtWidgets import QApplication, QComboBox, QFrame, QVBoxLayout, QLabel, QFileDialog, QPushButton, QTextEdit
from PySide6.QtCore import Qt
import pandas as pd


class EspecesMenacees(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liste des menaces par espèce")

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.libelle_especes = QLabel("")
        self.libelle_especes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.disposition.addWidget(self.libelle_especes)

        self.textedit_statistiques_menaces = QTextEdit("")
        self.textedit_statistiques_menaces.setEnabled(False)
        self.disposition.addWidget(self.textedit_statistiques_menaces)

        self.combo_especes = QComboBox()
        self.combo_especes.currentIndexChanged.connect(self.combo_changed)
        self.disposition.addWidget(self.combo_especes)

        self.bouton_import_data = QPushButton("Importer le csv")
        self.bouton_import_data.clicked.connect(self.ouvrir_csv)
        self.disposition.addWidget(self.bouton_import_data)

        self.df: pd.DataFrame = None

    def ouvrir_csv(self):
        chemin, filtre = QFileDialog.getOpenFileName(self, "Ouvrir le csv", "./", "*.csv")

        if chemin:
            self.df = pd.read_csv(chemin, sep=",")
            for cle in self.df.keys():
                if not cle.startswith("Men"):
                    self.combo_especes.addItem(cle, userData=(self.df[cle], self.df["Men_descr"]))

    def combo_changed(self, index):
        self.libelle_especes.setText(self.combo_especes.currentText())
        cle_series, menaces_series = self.combo_especes.currentData()
        texte = ""
        for i in range(len(cle_series)):

            if pd.notna(cle_series[i]):
                texte += f"{menaces_series[i]}\t{cle_series[i]}\n"

        self.textedit_statistiques_menaces.setText(texte)


app = QApplication()
em = EspecesMenacees()
em.show()
app.exec()

