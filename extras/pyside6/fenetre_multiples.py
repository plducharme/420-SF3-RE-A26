from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel


class Fenetre(QWidget):

    def __init__(self, titre: str, texte: str):
        super().__init__()
        disposition = QVBoxLayout()
        etiquette = QLabel()
        self.setWindowTitle(titre)
        etiquette.setText(texte)
        disposition.addWidget(etiquette)
        self.setLayout(disposition)


class FenetresMultiples(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple fenêtres multiples")

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        bouton_fenetre1 = QPushButton("Afficher/Cacher fenêtre1")
        bouton_fenetre1.clicked.connect(self.bouton_fenetre1_clicked)
        disposition.addWidget(bouton_fenetre1)
        # On créer la fenêtre et on garde la référence (self.fenetre1), la fenêtre est invisible
        self.fenetre1 = Fenetre("Fenêtre 1", "Le temps est une illusion; l'heure de lunch, encore plus!")

        bouton_fenetre2 = QPushButton("Afficher/Cacher fenêtre 2")
        bouton_fenetre2.clicked.connect(self.bouton_fenetre2_clicked)
        disposition.addWidget(bouton_fenetre2)
        self.fenetre2 = Fenetre("Fenêtre 2", "Méfiez-vous des gens qui disent aimer le peuple mais qui"
                                             " détestent tout ce que le peuple aime...")

        bouton_fenetre3 = QPushButton("Afficher/Détruire fenêtre 3")
        bouton_fenetre3.clicked.connect(self.bouton_fenetre3_clicked)
        disposition.addWidget(bouton_fenetre3)
        self.fenetre3 = Fenetre("Fenêtre 3", "L'inégalité, c'est le risque permanent du mépris.")



    def bouton_fenetre1_clicked(self):
        if self.fenetre1.isVisible():
            self.fenetre1.hide()
        else:
            self.fenetre1.show()

    def bouton_fenetre2_clicked(self):
        if self.fenetre2.isVisible():
            self.fenetre2.hide()
        else:
            self.fenetre2.show()


    def bouton_fenetre3_clicked(self):
        if self.fenetre3 is None:
            return
        if self.fenetre3.isVisible():
            # En assignant la référence à None, on détruit la fenêtre. Elle disparaîtra, mais on ne pourra plus
            # l'afficher sans la recréer
            self.fenetre3 = None
        else:
            self.fenetre3.show()

app = QApplication()
fm = FenetresMultiples()
fm.show()
app.exec()