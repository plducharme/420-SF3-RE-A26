from PySide6.QtWidgets import QApplication, QFrame, QLabel, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap, QFont


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        etiquette_pixmap = QLabel()
        # Un QPixmap est un objet qui représente une image
        # Son constructeur peut prendre en argument le chemin vers un fichier image
        pixmap = QPixmap('pyside6.png')
        etiquette_pixmap.setPixmap(pixmap)

        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        disposition.addWidget(etiquette_pixmap)

        etiquette_texte_riche = QLabel("Ceci est un texte riche!")
        police = QFont()
        police.setBold(True)
        police.setPointSize(14)
        police.setItalic(True)
        etiquette_texte_riche.setFont(police)
        disposition.addWidget(etiquette_texte_riche)

        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()