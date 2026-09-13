import csv

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel


class TimesCover(QMainWindow):

    def __init__(self):
        super().__init__()
        # Permet de donner un titre à la fenêtre
        self.setWindowTitle("Times Cover")

        self.disposition = QVBoxLayout()
        widget_central = QWidget()
        widget_central.setLayout(self.disposition)
        self.setCentralWidget(widget_central)

        # Création des libellés en utilisant une méthode (voir plus bas)
        self.annee = self.creer_libelles("Année")
        self.honneur = self.creer_libelles("Honneur")
        self.nom = self.creer_libelles("Nom")
        self.pays = self.creer_libelles("Pays")
        self.naissance = self.creer_libelles("Naissance")
        self.deces = self.creer_libelles("Décès")
        self.titre = self.creer_libelles("Titre")
        self.categorie = self.creer_libelles("Catégorie")
        self.contexte = self.creer_libelles("Contexte")

        disposition_boutons = QHBoxLayout()
        self.bouton_precedent = QPushButton("Précédent")
        self.bouton_precedent.setEnabled(False)
        self.bouton_precedent.clicked.connect(self.bouton_precedent_clicked)
        self.bouton_suivant = QPushButton("Suivant")
        self.bouton_suivant.clicked.connect(self.bouton_suivant_clicked)
        disposition_boutons.addWidget(self.bouton_precedent)
        disposition_boutons.addWidget(self.bouton_suivant)
        self.disposition.addLayout(disposition_boutons)
        # Création d'une liste pour stocker les entrées du fichier CSV
        self.entrees = []
        # Création d'un index pour se déplacer dans la liste des entrées
        self.index_entrees = 0
        # Lecture du CSV pour remplir la liste des entrées
        with open("../times.csv", "r", encoding="utf8") as fichier_csv:
            lignes = csv.DictReader(fichier_csv)
            for ligne in lignes:
                self.entrees.append(ligne)
        # Méthode mettant à jour les valeurs des libellés selon l'index courant
        self.afficher_entree()

    # Méthode pour créer les libellés pour éviter la répétition de code
    def creer_libelles(self, nom_propriete: str):
        disposition_libelle = QHBoxLayout()
        libelle_titre = QLabel(nom_propriete + ":")
        libelle_valeur = QLabel("")
        disposition_libelle.addWidget(libelle_titre)
        disposition_libelle.addWidget(libelle_valeur)
        self.disposition.addLayout(disposition_libelle)
        return libelle_valeur

    # Méthode pour afficher les valeurs des libellés selon l'index courant
    def afficher_entree(self):
        entree = self.entrees[self.index_entrees]
        self.annee.setText(entree["Year"])
        self.honneur.setText(entree["Honor"])
        self.nom.setText(entree["Name"])
        self.pays.setText(entree["Country"])
        self.naissance.setText(entree["Birth Year"])
        self.deces.setText(entree["Death Year"])
        self.titre.setText(entree["Title"])
        self.categorie.setText(entree["Category"])
        self.contexte.setText(entree["Context"])

    # Méthode pour gérer le clic sur le bouton précédent
    def bouton_precedent_clicked(self):
        self.index_entrees -= 1
        # Dans ce cas-ci, on désactive le bouton précédent si on est à la première entrée
        if self.index_entrees == 0:
            self.bouton_precedent.setEnabled(False)
        self.afficher_entree()

        if not self.bouton_suivant.isEnabled():
            self.bouton_suivant.setEnabled(True)

    def bouton_suivant_clicked(self):
        self.index_entrees += 1
        # Dans ce cas-ci, on désactive le bouton suivant si on est à la dernière entrée
        if self.index_entrees == len(self.entrees) - 1:
            self.bouton_suivant.setEnabled(False)
        self.afficher_entree()

        if not self.bouton_precedent.isEnabled():
            self.bouton_precedent.setEnabled(True)


app = QApplication()
tc = TimesCover()
tc.show()
app.exec()
