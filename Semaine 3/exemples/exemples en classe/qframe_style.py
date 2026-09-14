from PySide6.QtWidgets import QApplication, QFrame, QLabel, QVBoxLayout


class FrameAvecStyle(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadres stylés")
        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.cadre1 = QFrame()
        self.cadre1.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Sunken)
        self.cadre1.setLineWidth(3)
        self.cadre1.setMidLineWidth(2)
        self.cadre1.setBaseSize(300, 300)
        self.disposition.addWidget(self.cadre1)

        self.cadre2 = QFrame()
        self.cadre2.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)
        self.cadre2.setLineWidth(2)
        self.cadre2.setMidLineWidth(2)
        self.cadre2.setFixedSize(200, 200)
        self.disposition.addWidget(self.cadre2)


app = QApplication()
fas = FrameAvecStyle()
fas.show()
app.exec()

