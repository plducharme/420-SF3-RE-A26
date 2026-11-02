from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget, QPushButton


class Fenetre(QMainWindow):

    def __init__(self):
        super().__init__()
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        disposition = QVBoxLayout()

        self.etiquette = QLabel("")
        self.mon_line_edit = MonQLineEdit()
        # Connecte le signal personalisé à une méthode
        self.mon_line_edit.mon_signal.connect(self.mon_signal_declenche)
        bouton_test = QPushButton("Test")
        bouton_test.clicked.connect(self.bouton_clicked)
        disposition.addWidget(self.etiquette)
        disposition.addWidget(self.mon_line_edit)
        disposition.addWidget(bouton_test)
        widget_central.setLayout(disposition)

    # Porter attention à la signature de la méthode
    def mon_signal_declenche(self, nouveau_texte: str, longueur_texte: int):
        self.etiquette.setText(nouveau_texte + " " + str(longueur_texte))

    # Utiliser un bouton pour appeler le setText() du MonQLineEdit qui déclenchera le signal "monSignal"
    def bouton_clicked(self):
        self.mon_line_edit.setText("Ceci est un test")


# Un widget personnalisé qui va envoyer le signal personnalisé lorsque le setText() est appelé
class MonQLineEdit(QLineEdit):
    # défini notre signal avec sa signature (i.e. les types qui seront envoyés)
    mon_signal = Signal(str, int)

    def __init__(self):
        super().__init__()

    # Redéfinition de QLineEdit setText()
    def setText(self, arg__1: str) -> None:
        super().setText(arg__1)
        # Émission du signal
        self.mon_signal.emit(arg__1, len(self.text()))


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()
