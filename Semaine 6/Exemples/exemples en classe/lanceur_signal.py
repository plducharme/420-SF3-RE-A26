from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QComboBox, QGridLayout, QMessageBox


class LanceurSignal(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QGridLayout()
        self.setLayout(disposition)

        for r in range(3):
            for c in range(3):
                bouton = QPushButton(f"({r},{c})")
                bouton.pressed.connect(self.bouton_clicked)
                bouton.setObjectName(f"bouton_{r}_{c}")
                disposition.addWidget(bouton, r, c)

        self.combo_box = QComboBox()
        self.combo_box.addItem(f"bouton_2_2")
        self.combo_box.addItem(f"bouton_1_2")
        self.combo_box.addItem(f"bouton_0_2")
        self.combo_box.currentIndexChanged.connect(self.combo_box_changed)

        disposition.addWidget(self.combo_box, 3, 0, 1, 2)

    def bouton_clicked(self):
        # sender() retourne QObject (ex: un widget) qui a envoyé le signal
        bouton: QPushButton = self.sender()
        QMessageBox.warning(self, "Bouton cliqué", bouton.text())

    def combo_box_changed(self):
        text_bouton = self.combo_box.currentText()
        # On va aller chercher le bouton en utilisant son objectName
        bouton: QPushButton | None = self.findChild(QPushButton, text_bouton)
        bouton.click()


app = QApplication()
ls = LanceurSignal()
ls.show()
app.exec()
