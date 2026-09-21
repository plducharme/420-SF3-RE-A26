from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QComboBox, QPushButton, QLineEdit, QHBoxLayout, QMessageBox


# <a href="https://www.flaticon.com/free-icons/lightning" title="lightning icons">Lightning icons created by Good Ware - Flaticon</a>
class ComboBoxExemple(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple listes déroulantes")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.combobox_vehicules = QComboBox()
        self.combobox_vehicules.setDuplicatesEnabled(False)
        self.combobox_vehicules.addItem(QIcon("lightning.png"), "Kia Soul EV")
        self.combobox_vehicules.addItem("Dodge Challenger SRT8")
        self.combobox_vehicules.addItem("\U0001F3CD Kawasaki Ninja 1200cc")
        disposition.addWidget(self.combobox_vehicules)

        self.line_edit_ajout_vehicule = QLineEdit()
        self.line_edit_ajout_vehicule.setPlaceholderText("Nom du véhicule")
        self.bouton_ajout_vehicule = QPushButton("+")

        self.bouton_ajout_vehicule.clicked.connect(self.bouton_ajout_vehicule_clicked)
        self.bouton_enlever_vehicule = QPushButton("-")
        self.bouton_enlever_vehicule.clicked.connect(self.bouton_enlever_vehicule_clicked)

        disposition_boutons_vehicule = QHBoxLayout()
        disposition_boutons_vehicule.addWidget(self.line_edit_ajout_vehicule)
        disposition_boutons_vehicule.addWidget(self.bouton_ajout_vehicule)
        disposition_boutons_vehicule.addWidget(self.bouton_enlever_vehicule)
        disposition.addLayout(disposition_boutons_vehicule)

    def bouton_ajout_vehicule_clicked(self):
        texte = self.line_edit_ajout_vehicule.text()
        if len(texte) == 0:
            QMessageBox.warning(self, "Avertissement", "Texte vide")
            return

        self.combobox_vehicules.addItem(texte)
        self.line_edit_ajout_vehicule.clear()
        self.combobox_vehicules.setCurrentIndex(self.combobox_vehicules.count()-1)

    def bouton_enlever_vehicule_clicked(self):
        self.combobox_vehicules.removeItem(self.combobox_vehicules.currentIndex())


app = QApplication()
cbe = ComboBoxExemple()
cbe.show()
app.exec()
