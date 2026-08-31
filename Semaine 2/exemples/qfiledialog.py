from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog


class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QFileDialog")

        self.dialogue = QFileDialog(self)
        self.dialogue.setFileMode(QFileDialog.FileMode.AnyFile)

        self.dialogue.fileSelected.connect(self.fichier_selectionne)

        self.dialogue.exec()

    def fichier_selectionne(self, dossier):
        print("Dossier sélectionné : ", dossier)


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()