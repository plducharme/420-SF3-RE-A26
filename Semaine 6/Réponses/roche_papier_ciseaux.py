from random import Random

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton


class Joueur:
    def __init__(self, nom, isCpu: bool):
        self.nom = nom
        self.score = 0
        self.isCpu = isCpu


class RochePapierCiseau(QMainWindow):

    # Définir une variable de classe pour la taille des icônes (i.e. une constante)
    GRANDEUR_ICONE = 50

    def __init__(self):
        super().__init__()

        # variables pour l'état du jeu, en pure MVC, ces variables devraient être dans un modèle
        self.choix_cpu = None
        self.score_cpu_score = None
        self.choix_humain = None
        self.score_humain_score = None

        self.setWindowTitle("Roche, Papier, Ciseaux")

        widget_central = QWidget()
        disposition_jeu = QHBoxLayout()
        widget_central.setLayout(disposition_jeu)
        # Liste des joueurs, les joueurs sont représentés par la classe Joueur
        self.joueurs = []
        humain = Joueur("Humain", False)
        cpu = Joueur("CPU", True)

        self.joueurs.append(humain)
        self.joueurs.append(cpu)

        self.disposition_joueur = self.creer_disposition_joueur(humain)
        self.disposition_table = self.creer_table_jeu()
        self.disposition_cpu = self.creer_disposition_joueur(cpu)

        disposition_jeu.addLayout(self.disposition_joueur)
        disposition_jeu.addLayout(self.disposition_table)
        disposition_jeu.addLayout(self.disposition_cpu)

        self.setCentralWidget(widget_central)

        # Pour éviter de les initialiser à chaque fois, on les initialise ici. Plus performant.
        self.image_roche = QPixmap("roche.png").scaled(RochePapierCiseau.GRANDEUR_ICONE, RochePapierCiseau.GRANDEUR_ICONE)
        self.image_papier = QPixmap("papier.png").scaled(RochePapierCiseau.GRANDEUR_ICONE, RochePapierCiseau.GRANDEUR_ICONE)
        self.image_ciseaux = QPixmap("ciseaux.png").scaled(RochePapierCiseau.GRANDEUR_ICONE, RochePapierCiseau.GRANDEUR_ICONE)

    # Créer la disposition pour le score et les choix des joueurs
    def creer_table_jeu(self) -> QVBoxLayout:
        disposition = QVBoxLayout()

        self.score_humain_score = QLabel("0")
        self.score_cpu_score = QLabel("0")

        hbox = QHBoxLayout()
        hbox.addWidget(self.score_humain_score)
        hbox.addWidget(self.score_cpu_score)

        disposition.addLayout(hbox)

        self.choix_humain = QLabel("Choix Humain")
        self.choix_cpu = QLabel("Choix CPU")

        disposition.addWidget(self.choix_humain)
        disposition.addWidget(self.choix_cpu)

        return disposition

    # Créer la disposition pour un joueur
    def creer_disposition_joueur(self, joueur: Joueur) -> QVBoxLayout:
        disposition = QVBoxLayout()
        disposition.addWidget(QLabel(joueur.nom))
        roche_bouton = QPushButton("Roche")
        papier_bouton = QPushButton("Papier")
        ciseaux_bouton = QPushButton("Ciseaux")
        disposition.addWidget(roche_bouton)
        disposition.addWidget(papier_bouton)
        disposition.addWidget(ciseaux_bouton)
        # Si le joueur est un CPU, on désactive les boutons et on ne connecte pas les signaux
        if joueur.isCpu:
            roche_bouton.setDisabled(True)
            papier_bouton.setDisabled(True)
            ciseaux_bouton.setDisabled(True)
        else:
            roche_bouton.clicked.connect(self.choix_humain_clicked)
            papier_bouton.clicked.connect(self.choix_humain_clicked)
            ciseaux_bouton.clicked.connect(self.choix_humain_clicked)

        return disposition

    # La méthode est statique car elle ne dépend pas de l'état de l'objet
    @staticmethod
    def choix_cpu_jeu():
        return Random().choice(["Roche", "Papier", "Ciseaux"])

    @staticmethod
    def resolution_jeu(choix_humain, choix_cpu):
        if choix_humain == choix_cpu:
            return "Égalité"
        elif choix_humain == "Roche" and choix_cpu == "Ciseaux":
            return "Humain"
        elif choix_humain == "Papier" and choix_cpu == "Roche":
            return "Humain"
        elif choix_humain == "Ciseaux" and choix_cpu == "Papier":
            return "Humain"
        else:
            return "CPU"

    # Lorsque l'utilisateur fait un choix, on génère un choix pour le CPU et on résout le jeu
    def choix_humain_clicked(self):
        bouton = self.sender()
        choix_humain = bouton.text()
        # On génère un choix pour le CPU
        # Remarquer comment on utilise la méthode statique
        choix_cpu = RochePapierCiseau.choix_cpu_jeu()
        resultat = self.resolution_jeu(choix_humain, choix_cpu)
        self.afficher_choix(choix_humain, self.choix_humain)
        self.afficher_choix(choix_cpu, self.choix_cpu)
        if resultat == "Humain":
            self.joueurs[0].score += 1
        elif resultat == "CPU":
            self.joueurs[1].score += 1
        self.score_humain_score.setText(str(self.joueurs[0].score))
        self.score_cpu_score.setText(str(self.joueurs[1].score))

    # Ajoute une image correspondant au choix dans les QLabel
    def afficher_choix(self, choix, qlabel):
        match choix:
            case "Roche":
                qlabel.setPixmap(self.image_roche)
            case "Papier":
                qlabel.setPixmap(self.image_papier)
            case "Ciseaux":
                qlabel.setPixmap(self.image_ciseaux)
            case _:
                qlabel.setText("Erreur")


app = QApplication()
rpc = RochePapierCiseau()
rpc.show()
app.exec()


