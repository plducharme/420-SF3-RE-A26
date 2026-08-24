from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QVBoxLayout, QWidget, QPushButton, QLabel
from PySide6.QtGui import QPixmap


class QFileDialogExemple(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        self.disposition = QVBoxLayout()
        widget.setLayout(self.disposition)
        bouton = QPushButton("Ouvrir")
        bouton.clicked.connect(self.bouton_clicked)
        self.disposition.addWidget(bouton)

    def bouton_clicked(self):
        # cette fonction statique ouvre un QFileDialog permettant de sélectionner plusieurs fichiers
        # Retourne un Tuple() contenant la liste des fichiers et le filtre appliqué
        fichiers = QFileDialog.getOpenFileNames(self, "Choisir images", "./images", "Fichiers png (*.png)")

        for fichier in fichiers[0]:
            label = QLabel()
            label.setPixmap(QPixmap(fichier))
            self.disposition.addWidget(label)


app = QApplication()
fd = QFileDialogExemple()
fd.show()
app.exec()

