from PySide6.QtWidgets import QApplication, QTextEdit, QFrame, QVBoxLayout
from PySide6.QtCore import Qt


class ClavierSouris(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion événements calvier souris")
        self.disposition = QVBoxLayout()
        self.output = QTextEdit()
        self.output.setEnabled(False)
        self.disposition.addWidget(self.output)
        self.setLayout(self.disposition)

    def keyPressEvent(self, event, /):
        # on va gérer la touche "J"
        if event.key() == Qt.Key.Key_J:
            self.output.append("J pesé")
        # On va gérer le Ctrl-G
        elif event.key() == Qt.Key.Key_G and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.output.append("Ctrl-G pesé")
        else:
            # pour que les autres événements soient gérés normalement
            super().keyPressEvent(event)

    def mousePressEvent(self, event, /):

        if event.button() == Qt.MouseButton.LeftButton:
            self.output.append("Click de gauche")
        elif event.button() == Qt.MouseButton.RightButton:
            self.output.append("Click de droit")


app = QApplication()
cs = ClavierSouris()
cs.show()
app.exec()
