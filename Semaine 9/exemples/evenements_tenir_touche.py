from PySide6.QtWidgets import QApplication, QTextEdit, QFrame, QVBoxLayout
from PySide6.QtCore import Qt, QTimer


class TenirTouche(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple de gestion d'événements")
        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.edit_output = QTextEdit()
        self.edit_output.setEnabled(False)
        self.disposition.addWidget(self.edit_output)
        self.touches_tenues = []

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.timeout_touches_tenues)
        self.timer.start()

    def timeout_touches_tenues(self):

        if Qt.Key.Key_F in self.touches_tenues:
            self.edit_output.append("F tenu")

    def keyPressEvent(self, event, /):

        if event.key() == Qt.Key.Key_F:
            self.edit_output.append("F pesé")
            self.touches_tenues.append(event.key())
        else:
            super().keyPressEvent(event)

    def keyReleaseEvent(self, event, /):

        if event.key() == Qt.Key.Key_F:
            self.edit_output.append("F relâché")
            self.touches_tenues.remove(event.key())
        else:
            super().keyReleaseEvent(event)


app = QApplication()
tt = TenirTouche()
tt.show()
app.exec()
