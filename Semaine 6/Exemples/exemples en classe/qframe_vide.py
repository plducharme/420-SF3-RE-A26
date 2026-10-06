from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout


class FrameVide(QFrame):

    def __init__(self):
        super().__init__()

        diposition = QVBoxLayout()
        self.setLayout(diposition)


app = QApplication()
fv = FrameVide()
fv.show()
app.exec()
