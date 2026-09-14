from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class StyleGlobaux(QWidget):

    def __init__(self):
        super().__init__()

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        # Bouton 1
        self.bouton1 = QPushButton("Bouton 1")
        self.bouton2 = QPushButton("Bouton 1")

        self.disposition.addWidget(self.bouton1)
        self.disposition.addWidget(self.bouton2)


# Pour appliquer globalement, on charge le QSS sur le QApplication en précisant les classes
app = QApplication()
# Aurait pu être défini dans un fichier externe
qss = """
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
        font-family: Arial;
        font-size: 14px;
    }
    QPushButton {
        background-color: #007acc;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #005999;
    }
"""
# Doit être appliqué avant de montrer la fenêtre
app.setStyleSheet(qss)
sg = StyleGlobaux()
sg.show()
app.exec()
