from PySide6.QtWidgets import QApplication, QFrame, QLabel, QMainWindow, QWidget, QHBoxLayout
from PySide6.QtCore import QSize


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        # Initialisation d'un cadre vide (QFrame)
        cadre = QFrame()
        # changer le style du cadre
        # Ceci peut se faire en combinant les options de forme et d'ombre avec l'opérateur "|" (bitwise OR)
        cadre.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        cadre.setBaseSize(QSize(250, 250))

        widget_central = QWidget()
        disposition = QHBoxLayout()
        widget_central.setLayout(disposition)
        disposition.addWidget(cadre)

        etiquette = QLabel("Etiquette")
        # Le QLabel hérite de QFrame, on peut donc aussi lui appliquer un style de cadre.
        # Il est possible de changer les options de forme et d'ombre indépendamment.
        etiquette.setFrameShape(QFrame.Shape.Panel)
        etiquette.setFrameShadow(QFrame.Shadow.Raised)
        disposition.addWidget(etiquette)

        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()