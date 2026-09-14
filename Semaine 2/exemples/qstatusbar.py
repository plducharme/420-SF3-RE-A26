from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QStatusBar


class MaBarreDeStatut(QMainWindow):

    def __init__(self):
        super().__init__()
        bouton = QPushButton("Message")
        bouton.clicked.connect(self.bouton_clicked)
        self.setCentralWidget(bouton)

        self.barre_de_statut = QStatusBar()
        self.label_normal = QLabel("Ceci est un message normal")
        self.compte_temporaire = 0
        label_permanent = QLabel("Ceci est un message permanent")
        self.barre_de_statut.addWidget(self.label_normal)
        self.barre_de_statut.addPermanentWidget(label_permanent)
        self.setStatusBar(self.barre_de_statut)

    def bouton_clicked(self):
        self.barre_de_statut.showMessage("Message temporaire", timeout=5000)
        self.compte_temporaire += 1
        self.label_normal.setText("Ceci est un message normal. Nb temp: " + str(self.compte_temporaire))


app = QApplication()
mbs = MaBarreDeStatut()
mbs.show()
app.exec()
