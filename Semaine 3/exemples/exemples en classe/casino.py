from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QSize

import random


class MachineASous(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma première machine à sous")

        self.jeu = Jeu()
        # self.setStyleSheet("background-image: url(\"images/arriere.png\"); background-position: center;")

        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)

        self.police_solde = QFont()
        self.police_solde.setFamily("Century")
        self.police_solde.setPointSize(24)
        self.police_solde.setBold(True)

        self.disposition_solde = QHBoxLayout()
        self.libelle_solde = QLabel("Solde:")
        self.libelle_solde.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.libelle_solde.setFont(self.police_solde)

        self.libelle_solde_valeur = QLabel()
        self.libelle_solde_valeur.setNum(self.jeu.solde)
        self.libelle_solde_valeur.setFont(self.police_solde)
        self.disposition_solde.addWidget(self.libelle_solde)
        self.disposition_solde.addWidget(self.libelle_solde_valeur)
        self.disposition_principale.addLayout(self.disposition_solde)

        self.disposition_items = QHBoxLayout()
        self.item1 = QLabel()
        self.item1.setFrameStyle(QLabel.Shadow.Raised | QLabel.Shape.Panel)
        self.item1.setMinimumSize(200, 200)
        self.item1.setMaximumSize(300, 300)
        self.disposition_items.addWidget(self.item1)

        self.item2 = QLabel()
        self.item2.setFrameStyle(QLabel.Shadow.Raised | QLabel.Shape.Panel)
        self.item2.setMinimumSize(200, 200)
        self.item2.setMaximumSize(300, 300)
        self.disposition_items.addWidget(self.item2)

        self.item3 = QLabel()
        self.item3.setFrameStyle(QLabel.Shadow.Raised | QLabel.Shape.Panel)
        self.item3.setMinimumSize(200, 200)
        self.item3.setMaximumSize(300, 300)
        self.disposition_items.addWidget(self.item3)
        self.disposition_principale.addLayout(self.disposition_items)

        self.bouton_levier = QPushButton()
        self.image_levier = QPixmap("./images/levier.png")
        self.image_levier = self.image_levier.scaled(QSize(64, 64))
        # self.bouton_levier.setFixedSize(QSize(128, 128))
        self.bouton_levier.setIcon(self.image_levier)
        self.bouton_levier.setIconSize(QSize(64, 64))
        self.bouton_levier.setFixedHeight(64)
        self.bouton_levier.setStyleSheet("background-color: #e8e81e;")
        self.bouton_levier.clicked.connect(self.bouton_levier_clicked)
        self.disposition_principale.addWidget(self.bouton_levier)

        self.mise_a_jour()

    def bouton_levier_clicked(self):
        self.jeu.tour_de_jeu()
        self.jeu.verification_gagnant()
        self.mise_a_jour()

    def mise_a_jour(self):
        self.item1.setPixmap(self.jeu.item_jeu_1.pixmap)
        self.item2.setPixmap(self.jeu.item_jeu_2.pixmap)
        self.item3.setPixmap(self.jeu.item_jeu_3.pixmap)
        self.libelle_solde_valeur.setNum(self.jeu.solde)



class Jeu:

    ETAT_JOUER = 0
    ETAT_PERDU = 1

    def __init__(self):
        self.solde = 500

        self.item_jeu_1: ItemJeu | None = None
        self.item_jeu_2: ItemJeu | None = None
        self.item_jeu_3: ItemJeu | None = None

        self.etat = Jeu.ETAT_JOUER

        self.item_etoile = ItemJeu("etoile", QPixmap("./images/etoile.png"))
        self.item_champi = ItemJeu("champignon", QPixmap("./images/champi.png"))
        self.item_gateau = ItemJeu("gateau", QPixmap("./images/gateau.png"))
        self.liste_items = [self.item_etoile, self.item_champi, self.item_gateau]

        self.tour_de_jeu()

    def tour_de_jeu(self):
        self.item_jeu_1 = random.choice(self.liste_items)
        self.item_jeu_2 = random.choice(self.liste_items)
        self.item_jeu_3 = random.choice(self.liste_items)

    def verification_gagnant(self):
        self.solde -= 50
        if self.item_jeu_1 == self.item_jeu_2 == self.item_jeu_3:
            self.solde += 250
        if self.solde == 0:
            self.etat = Jeu.ETAT_PERDU


class ItemJeu:

    def __init__(self, nom: str, pixmap: QPixmap):
        self.nom = nom
        self.pixmap = pixmap.scaled(QSize(200, 200), Qt.AspectRatioMode.KeepAspectRatio)


    def __eq__(self, other):
        return self.nom == other.nom


app = QApplication()
mas = MachineASous()
mas.show()
app.exec()






