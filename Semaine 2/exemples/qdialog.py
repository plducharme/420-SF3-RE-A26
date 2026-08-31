import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Focus!!!!!")

        bouton = QPushButton("QDialog")
        bouton.clicked.connect(self.bouton_clicked)
        self.setCentralWidget(bouton)

    def bouton_clicked(self):
        print("click")

        dialogue = QDialog(self)
        dialogue.setWindowTitle("Fenêtre de dialogue")
        dialogue.exec()


app = QApplication()

window = MainWindow()
window.show()

app.exec()
