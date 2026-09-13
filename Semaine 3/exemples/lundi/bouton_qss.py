from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QHBoxLayout


class BoutonQss(QFrame):

    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        self.setLineWidth(3)
        self.setMidLineWidth(3)

        with open("style.qss", mode="r", encoding="utf8") as fichier:
            qss = fichier.read()
            self.setStyleSheet(qss)

        disposition = QHBoxLayout()
        self.setLayout(disposition)

        bouton_1 = QPushButton("Activé/Désactivé")
        bouton_1.setCheckable(True)
        bouton_1.toggled.connect(self.bouton_1_clicked)
        bouton_1.setObjectName("monbouton")
        disposition.addWidget(bouton_1)

        self.bouton_2 = QPushButton("Bouton 2")
        self.bouton_2.setEnabled(False)
        disposition.addWidget(self.bouton_2)

    def bouton_1_clicked(self, checked):
        self.bouton_2.setEnabled(checked)


app = QApplication()
bq = BoutonQss()
bq.show()
app.exec()
