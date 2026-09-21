from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCheckBox, QButtonGroup
from PySide6.QtGui import QIcon


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        self.case_canard = QCheckBox()
        self.case_canard.setIcon(QIcon('canard.png'))
        self.case_canard.setText("Canard")
        self.case_canard.stateChanged.connect(self.case_canard_changee)
        self.case_ornithorynque = QCheckBox()
        self.case_ornithorynque.setText("Ornithorynque")
        self.case_chien = QCheckBox()
        self.case_chien.setText("Chien")

        disposition.addWidget(self.case_canard)
        disposition.addWidget(self.case_ornithorynque)
        disposition.addWidget(self.case_chien)

    def case_canard_changee(self):
        print("Case canard clicked")


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()