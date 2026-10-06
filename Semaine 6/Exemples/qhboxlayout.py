from PySide6.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QPushButton, QWidget


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition_hbox = QHBoxLayout()
        widget_central.setLayout(disposition_hbox)

        for i in range(8):
            bouton = QPushButton(str(i))
            disposition_hbox.addWidget(bouton)

        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()


