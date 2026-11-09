from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit
import sqlite3


class BasesSQL(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        disposition = QVBoxLayout()
        widget.setLayout(disposition)

        self.textarea = QTextEdit()
        self.textarea.setReadOnly(True)
        disposition.addWidget(self.textarea)
        self.setCentralWidget(widget)

        # Objets jeux
        liste_jeux = []
        liste_jeux.append(Jeu("Fornite", "Epic Games", 2017))
        liste_jeux.append(Jeu("Counter-Strike 2", "Valve", 2023))
        liste_jeux.append(Jeu("Starfield", "Bethesda Game Studios", 2023))

        jeux_db = JeuxBD()
        # Exécute toutes les requêtes
        jeux_db.supprimer_table()
        jeux_db.creer_table()

        self.textarea.setText(self.textarea.toPlainText() + "\nInsertion\n")
        jeux_db.inserer_jeux(liste_jeux)

        self.textarea.setText(self.textarea.toPlainText() + "\nSélection de Fornite\n")
        jeu = jeux_db.select_jeu_par_nom("Fornite")
        self.textarea.setText(str(jeu))

        self.textarea.setText(self.textarea.toPlainText() + "\nSuppression de Fornite\n")
        jeux_db.supprimer_enregistrement("Fornite")

        self.textarea.setText(self.textarea.toPlainText() + "\nSélection de tous les enregistrement restants\n")
        jeux = jeux_db.select_tous()
        text = ""
        for j in jeux:
            text += str(j) + "\n"
        self.textarea.setText(self.textarea.toPlainText() + "\n" + text)
        self.textarea.setText(self.textarea.toPlainText() + "\nSuppression de la table\n")
        # jeux_db.supprimer_table()


# Classe représentant un jeu
class Jeu:
    def __init__(self, nom: str, studio: str, annee: int):
        self.nom = nom
        self.studio = studio
        self.annee = annee

    def __str__(self):
        return "{\nnom:\n" + self.nom + "\nstudio:\n" + self.studio + "\nannée:\n" + self.annee + "\n}"


# Classe qui manipule la BD
class JeuxBD:

    def __init__(self):
        # Ouvre une connection sur une BD contenue dans un fichier jeux.db ou la créée si inexistante
        self.con = sqlite3.connect("jeux.db")

    def creer_table(self):
        # Créer un curseur pour exécuter une requête
        curseur = self.con.cursor()
        # Créer une table Jeu
        curseur.execute("CREATE TABLE Jeu(nom, studio, annee)")

    def supprimer_table(self):
        # Créer un curseur pour exécuter une requête
        curseur = self.con.cursor()
        curseur.execute("DROP TABLE IF EXISTS Jeu")

    def inserer_jeux(self, liste_jeux: list[Jeu]):
        # Créer un curseur pour exécuter une requête
        curseur = self.con.cursor()
        # On génère les valeurs sous forme ('nom', 'studio', 'annee')
        # il est aussi possible de passer une liste de plusieurs enregistrements directement
        requete = "INSERT INTO Jeu VALUES"
        for idx in range(0, len(liste_jeux)):
            requete += ("('" + liste_jeux[idx].nom + "', '" + liste_jeux[idx].studio +
                         "', '" + str(liste_jeux[idx].annee) + "')")
            if idx != len(liste_jeux) - 1:
                requete += ","
        print(f"Insérer requête: {requete}")
        curseur.execute(requete)
        # Lorsque l'on insère un enregistrement, une transaction est implicitement créée. Il faut alors faire un
        # "commit" pour signifier la fin de la transaction et appliquer les changements
        self.con.commit()

    def supprimer_enregistrement(self, nom):
        # Créer un curseur pour exécuter une requête
        curseur = self.con.cursor()
        requete = "DELETE FROM jeu WHERE nom = '" + nom + "'"
        print(f"Supprimer requête: {requete}")
        curseur.execute(requete)
        self.con.commit()

    def select_jeu_par_nom(self, nom) -> Jeu:
        # Créer un curseur pour exécuter une requête
        curseur = self.con.cursor()
        # Sélectionne toutes les colonnes, il est possible de sélectionner seulement certaines colonnes
        requete = "SELECT * FROM jeu WHERE nom = '" + nom + "'"
        print(f"Sélection requête: {requete}")
        curseur.execute(requete)
        # va chercher le premier enregistrement, retourne un Tuple contenant la valeur de chaque colonne
        resultat = curseur.fetchone()
        return Jeu(resultat[0], resultat[1], resultat[2])

    def select_tous(self):
        # Créer un curseur pour exécuter une requête
        curseur = self.con.cursor()
        # Sélectionne toutes les colonnes
        requete = "SELECT * FROM jeu"
        print(f"Sélection tous requête: {requete}")
        curseur.execute(requete)
        # va chercher tous les enregistrements retournés par la requête, retourne une liste de Tuple
        resultats = curseur.fetchall()
        jeux = []
        for jeu in resultats:
            jeux.append(Jeu(jeu[0], jeu[1], jeu[2]))
        return jeux


app = QApplication()
bases = BasesSQL()
bases.show()
app.exec()




