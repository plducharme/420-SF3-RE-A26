from PySide6.QtCore import QSize
from PySide6.QtGui import QMouseEvent, Qt
from PySide6.QtWidgets import QApplication, QLabel, QFrame, QVBoxLayout


class EvenementsDemo(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(200, 200))
        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.compteur = 0
        self.libelle = QLabel(str(self.compteur))
        self.libelle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.disposition.addWidget(self.libelle)

    # mousePressEvent() gère les événements lors qu'un bouton de souris est pesé
    def mousePressEvent(self, event: QMouseEvent) -> None:
        # On va changer le QLabel sur un click droit
        if event.button() == Qt.MouseButton.RightButton:
            self.compteur += 1
            self.libelle.setText(str(self.compteur))
        else:
            # On appelle la méthode parente pour gérer les autres boutons normalement
            super().mousePressEvent(event)


app = QApplication()
fenetre = EvenementsDemo()
fenetre.show()
app.exec()
