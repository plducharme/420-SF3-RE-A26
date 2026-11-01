from PySide6.QtCore import QPoint, QSize, QPropertyAnimation
from PySide6.QtWidgets import QWidget, QApplication


# Petit rappel, un widget sans parent est une fenêtre
class BoutonAnime(QWidget):

    def __init__(self):
        super().__init__()
        # On agrandit la fenêtre
        self.resize(QSize(800, 600))

        # Créer notre widget à animer, ne pas oublier le parent en paramètre
        widget_enfant = QWidget(self)
        widget_enfant.resize(QSize(50, 50))
        widget_enfant.setStyleSheet("background-color:blue")

        # Créer l'animation sur le widget_enfant pour la propriété "pos";
        # remarquez que le cast de la string en "bytes string"
        self.animation = QPropertyAnimation(widget_enfant, b"pos")
        # pos est un QPoint
        self.animation.setStartValue(QPoint(10, 10))
        self.animation.setEndValue(QPoint(500, 500))
        # La durée en millisecondes
        self.animation.setDuration(2000)
        self.animation.start()


app = QApplication()
ba = BoutonAnime()
ba.show()
app.exec()








