from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox
from PySide6.QtGui import QIcon


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        liste_base = QComboBox()
        liste_base.addItem(QIcon('canard.png'), "Canard")
        liste_base.addItem("Ornithorynque")
        liste_base.addItem("Chien")
        disposition.addWidget(liste_base)

        self.liste_complexe = QComboBox()
        self.liste_complexe.setEditable(True)
        self.liste_complexe.addItem("Premier Item")
        self.liste_complexe.addItem("Autre Item")
        self.liste_complexe.currentTextChanged.connect(self.liste_complexe_modifiee)
        disposition.addWidget(self.liste_complexe)

    def liste_complexe_modifiee(self):
        texte_modifie = self.liste_complexe.currentText()
        self.liste_complexe.setItemText(self.liste_complexe.currentIndex(), texte_modifie)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()

