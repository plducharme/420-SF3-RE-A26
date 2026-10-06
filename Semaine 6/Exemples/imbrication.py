from PySide6.QtWidgets import QGridLayout, QApplication, QMainWindow, QPushButton, QWidget, QLabel,\
    QHBoxLayout, QVBoxLayout


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition_grid = QGridLayout()
        widget_central.setLayout(disposition_grid)

        disposition_hbox = QHBoxLayout()

        bouton1 = QPushButton("1")
        bouton2 = QPushButton("2")
        bouton3 = QPushButton("3")

        disposition_hbox.addWidget(bouton1)
        disposition_hbox.addWidget(bouton2)
        disposition_hbox.addWidget(bouton3)

        # addLayout(layout, row, column, rowspan, colspan)
        disposition_grid.addLayout(disposition_hbox, 0, 0, 1, 3)

        disposition_vbox = QVBoxLayout()
        disposition_vbox.addWidget(QLabel("Text1: Les opinions sont faites pour changer ; sinon comment atteindre la vérité ?"))
        disposition_vbox.addWidget(QLabel("Text2: Si tu vois tout en gris, déplace l'éléphant !"))
        disposition_vbox.addWidget(QLabel("Text3: Si haut que l'on soit placé, on n'est jamais assis que sur son cul"))

        disposition_grid.addLayout(disposition_vbox, 1, 0, 3, 3)

        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()