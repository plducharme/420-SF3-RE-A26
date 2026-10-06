from PySide6.QtWidgets import QVBoxLayout, QApplication, QMainWindow, QPushButton, QWidget


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition_vbox = QVBoxLayout()
        widget_central.setLayout(disposition_vbox)

        for i in range(8):
            bouton = QPushButton(str(i))
            disposition_vbox.addWidget(bouton)

        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()


