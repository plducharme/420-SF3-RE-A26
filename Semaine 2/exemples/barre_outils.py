from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtGui import QAction, QIcon


class BarreOutils(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de barre d'outils")

        self.barre_outils = QToolBar()
        self.addToolBar(self.barre_outils)
        self.bouton_test = QPushButton("Test")
        self.bouton_test.clicked.connect(self.bouton_test_clicked)
        self.barre_outils.addWidget(self.bouton_test)

        self.action_outils = QAction(parent=self)
        self.action_outils.setText("SuperDuper!")
        self.action_outils.triggered.connect(self.action_outils_triggered)
        self.barre_outils.addAction(self.action_outils)

        self.barre_statut = QStatusBar()
        # self.barre_statut.setVisible(True)
        self.setStatusBar(self.barre_statut)

    def action_outils_triggered(self):
        self.setStatusTip("SuperDuper!")

    def bouton_test_clicked(self):
        self.setStatusTip("TEST!")


app = QApplication()
bo = BarreOutils()
bo.show()
app.exec()
