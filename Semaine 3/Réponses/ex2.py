from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QFrame, QLabel


class Ex3(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.libelle_texte = QLabel("L'informatique, ça fait gagner beaucoup de temps... à condition d'en avoir beaucoup devant soi !")
        disposition.addWidget(self.libelle_texte)

        self.bouton_italique = QPushButton("Italique")
        # On va le transformer en bouton bascule
        self.bouton_italique.setCheckable(True)
        self.bouton_italique.toggled.connect(self.bouton_italique_toggled)
        disposition.addWidget(self.bouton_italique)

        self.bouton_gras = QPushButton("Gras")
        self.bouton_gras.setCheckable(True)
        self.bouton_gras.toggled.connect(self.bouton_gras_toggled)
        disposition.addWidget(self.bouton_gras)

        self.bouton_wordwrap = QPushButton("Word Wrap")
        self.bouton_wordwrap.setCheckable(True)
        self.bouton_wordwrap.toggled.connect(self.bouton_wordWrap_toggled)
        disposition.addWidget(self.bouton_wordwrap)

        self.bouton_augmenter_police = QPushButton("Augmenter la police")
        self.bouton_augmenter_police.clicked.connect(self.bouton_augmenter_police_clicked)
        disposition.addWidget(self.bouton_augmenter_police)

        self.bouton_diminuer_police = QPushButton("Diminuer la police")
        self.bouton_diminuer_police.clicked.connect(self.bouton_diminuer_police_clicked)
        disposition.addWidget(self.bouton_diminuer_police)


    def bouton_italique_toggled(self, etat):
        if etat:
            self.libelle_texte.setStyleSheet("font-style: italic;")
        else:
            self.libelle_texte.setStyleSheet("font-style: normal;")


    def bouton_gras_toggled(self, etat):
        if etat:
            self.libelle_texte.setStyleSheet("font-weight: bold;")
        else:
            self.libelle_texte.setStyleSheet("font-weight: normal;")

    def bouton_wordWrap_toggled(self, etat):
        self.libelle_texte.setWordWrap(etat)

    def bouton_augmenter_police_clicked(self):
        # Récupérer la police actuelle avec le getter
        police = self.libelle_texte.font()
        taille = police.pointSize()
        police.setPointSize(taille + 1)
        self.libelle_texte.setFont(police)

    def bouton_diminuer_police_clicked(self):
        police = self.libelle_texte.font()
        taille = police.pointSize()
        if taille > 1:
            police.setPointSize(taille - 1)
            self.libelle_texte.setFont(police)


app = QApplication()
ex3 = Ex3()
ex3.show()
app.exec()
