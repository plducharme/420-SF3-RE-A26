from PySide6.QtWidgets import QApplication, QPushButton, QLabel
import random


class WidgetSansParent(QPushButton):
    def __init__(self):
        super().__init__("Pesez-moi!")
        self.clicked.connect(self.bouton_clicked)
        self.liste_titres = ["Bonjour!", "Bonsoir!", "Bonne nuit!"]

    def bouton_clicked(self):
        self.setWindowTitle(random.choice(self.liste_titres))


app = QApplication()
wsp = WidgetSansParent()
wsp.show()
# Un widget sans parent est toujours une fenêtre
label = QLabel()
label.setText("Ceci est un libellé dans un QLabel sans parent")
label.setWindowTitle("QLabel sans parent")
label.show()

app.exec()
