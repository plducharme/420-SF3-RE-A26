from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize


class LibelleEx(QFrame):

    def __init__(self):
        super().__init__()

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        self.label_contenu = QLabel()
        self.disposition.addWidget(self.label_contenu)

        bouton_selection = QPushButton("Sélectionner")
        icone_bouton_selection = QIcon("../image.png")
        bouton_selection.setIcon(icone_bouton_selection)
        bouton_selection.pressed.connect(self.bouton_selection_pressed)
        self.disposition.addWidget(bouton_selection)

    def bouton_selection_pressed(self):
        chemin_fichiers, filtre = QFileDialog.getOpenFileNames(parent=self, caption="Choisissez une image", dir="./images", filter="Images (*.png)")
        for chemin in chemin_fichiers:
            libelle_image = QLabel()
            image = QPixmap(chemin)
            libelle_image.setPixmap(image)
            self.disposition.insertWidget(0, libelle_image)


app = QApplication()
le = LibelleEx()
le.show()
app.exec()