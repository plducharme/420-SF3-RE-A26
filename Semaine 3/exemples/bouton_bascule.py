from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QPushButton


class BoutonBascule(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QHBoxLayout()
        self.setLayout(disposition)
        self.setLineWidth(3)

        self.bouton_bascule_1 = QPushButton("Activer/Désactiver 2")
        # SetCheckable(True) le transforme en bouton bascule "cochable", ayant deux états; True si "cocher", false sinon
        self.bouton_bascule_1.setCheckable(True)
        # Lorsque le QPushButton est "cochable", il a un signal "toggled" émit lorsqu'il change d'état
        # Ce signal envoie une variable correspondant à l'état du bouton
        # Voir la méthode connectée
        self.bouton_bascule_1.toggled.connect(self.bouton_bascule_1_toggled)
        disposition.addWidget(self.bouton_bascule_1)

        self.bouton_bascule_2 = QPushButton("2")
        self.bouton_bascule_2.setEnabled(False)
        disposition.addWidget(self.bouton_bascule_2)

    def bouton_bascule_1_toggled(self, etat):
        if etat:
            self.bouton_bascule_2.setEnabled(True)
        else:
            self.bouton_bascule_2.setEnabled(False)


app = QApplication()
bb = BoutonBascule()
bb.show()
app.exec()
