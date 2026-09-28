from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QGridLayout, QHBoxLayout, QSpacerItem
from jeux_modele import JeuxModele, JeuxSortie

# La vue est la représentation graphique de l'application
class GestionnaireJeuVue(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialisation du modèle et du contrôleur
        self.modele = JeuxModele()
        self.controlleur = GestionnaireJeuControlleur(self.modele, self)

        # Initialisation de la fenêtre, on va utiliser un QGridLayout
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        self.disposition_grid = QGridLayout()
        widget_central.setLayout(self.disposition_grid)

        # Création des widgets pour les entrées, voir méthode creer_widget_edit
        self.edit_nom, disposition_nom = self.creer_widget_edit("Nom")
        self.disposition_grid.addLayout(disposition_nom, 0, 0)

        self.edit_editeur, disposition_editeur = self.creer_widget_edit("Editeur")
        self.disposition_grid.addLayout(disposition_editeur, 0, 1)

        self.edit_annee, disposition_annee = self.creer_widget_edit("Date de sortie")
        self.disposition_grid.addLayout(disposition_annee, 0, 2)

        self.edit_developpeur, disposition_developpeur = self.creer_widget_edit("Développeur")
        self.disposition_grid.addLayout(disposition_developpeur, 1, 0)

        self.edit_genre, disposition_genre = self.creer_widget_edit("Genre")
        self.disposition_grid.addLayout(disposition_genre, 1, 1)

        self.edit_systeme, disposition_systeme = self.creer_widget_edit("Système d'exploitation")
        self.disposition_grid.addLayout(disposition_systeme, 1, 2)
        # Créer QHBoxLayout pour les boutons
        disposition_boutons = QHBoxLayout()
        bouton_enregistrer = QPushButton("Enregistrer")
        bouton_enregistrer.clicked.connect(self.controlleur.bouton_enregistrer_clicked)
        # On va style le bouton enregistrer
        bouton_enregistrer.setStyleSheet("background-color: red")
        police = QFont()
        police.setBold(True)
        bouton_enregistrer.setFont(police)

        bouton_precedent = QPushButton("Précédent")
        bouton_precedent.clicked.connect(self.controlleur.precedent_clicked)
        bouton_suivant = QPushButton("Suivant")
        bouton_suivant.clicked.connect(self.controlleur.suivant_clicked)
        disposition_boutons.addWidget(bouton_precedent)
        disposition_boutons.addWidget(bouton_suivant)
        disposition_boutons.addWidget(bouton_enregistrer)
        # Ajout d'un QSpaceItem
        self.disposition_grid.addItem(QSpacerItem(40, 20), 2, 0)

        # Ajouter le QHBoxLayout à la disposition en grille
        self.disposition_grid.addLayout(disposition_boutons, 3, 0, 1, 3)

        # Index de l'enregistrement courant
        self.index_entrees = 0
        self.controlleur.afficher_entree(self.index_entrees)

    @staticmethod
    def creer_widget_edit(nom: str) -> (QLineEdit, QVBoxLayout):
        label = QLabel(nom)
        edit = QLineEdit()
        disposition = QVBoxLayout()
        disposition.addWidget(label)
        disposition.addWidget(edit)
        return edit, disposition


# Le controlleur est la "colle" entre le modèle et la vue
# Une action de l'utilisateur sur la vue va déclencher une méthode du controlleur permettant d'intéragir avce le modèle
class GestionnaireJeuControlleur:

    def __init__(self, modele: JeuxModele, vue: GestionnaireJeuVue):
        self.modele = modele
        self.vue = vue


    def bouton_enregistrer_clicked(self):
        jeu = JeuxSortie()
        jeu.nom = self.vue.edit_nom.text()
        jeu.editeur = self.vue.edit_editeur.text()
        jeu.annee = self.vue.edit_annee.text()
        jeu.developpeur = self.vue.edit_developpeur.text()
        jeu.genre = self.vue.edit_genre.text()
        jeu.systeme_exploitation = self.vue.edit_systeme.text()
        self.modele.liste_sorties[self.vue.index_entrees] = jeu
        self.modele.enregistrer_csv()
        self.vue.statusBar().showMessage("Enregistrement réussi", 2500)


    def afficher_entree(self, index: int):
        jeu = self.modele.liste_sorties[index]
        self.vue.edit_nom.setText(jeu.nom)
        self.vue.edit_editeur.setText(jeu.editeur)
        self.vue.edit_annee.setText(jeu.date_sortie)
        self.vue.edit_developpeur.setText(jeu.developpeur)
        self.vue.edit_genre.setText(jeu.genre)
        self.vue.edit_systeme.setText(jeu.systeme_exploitation)

    def precedent_clicked(self):
        self.vue.index_entrees -= 1
        self.afficher_entree(self.vue.index_entrees)

    def suivant_clicked(self):
        self.vue.index_entrees += 1
        self.afficher_entree(self.vue.index_entrees)


app = QApplication()
gjv = GestionnaireJeuVue()
gjv.show()
app.exec()

