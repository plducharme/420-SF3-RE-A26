from csv import DictReader, DictWriter

# JeuxSortie est une classe qui représente un enregistrement dans le fichier CSV
class JeuxSortie:

    def __init__(self):
        self._systeme_exploitation = None
        self._genre = None
        self._date_sortie = None
        self._editeur = None
        self._developpeur = None
        self._nom = None

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def developpeur(self):
        return self._developpeur

    @developpeur.setter
    def developpeur(self, developpeur):
        self._developpeur = developpeur

    @property
    def editeur(self):
        return self._editeur

    @editeur.setter
    def editeur(self, editeur):
        self._editeur = editeur

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def systeme_exploitation(self):
        return self._systeme_exploitation

    @systeme_exploitation.setter
    def systeme_exploitation(self, systeme_exploitation):
        self._systeme_exploitation = systeme_exploitation

    @property
    def date_sortie(self):
        return self._date_sortie

    @date_sortie.setter
    def date_sortie(self, date_sortie):
        self._date_sortie = date_sortie

# JeuxModele est une classe qui représente le modèle de l'application
class JeuxModele:

    def __init__(self):
        self.liste_sorties = []
        self.lire_csv()

    def lire_csv(self):
        with open("computer_games.csv", "r", encoding="utf-8") as csvfile:
            csv_reader = DictReader(csvfile)
            for entree in csv_reader:
                jeu = JeuxSortie()
                jeu.nom = entree["Name"]
                jeu.developpeur = entree["Developer"]
                jeu.editeur = entree["Producer"]
                jeu.genre = entree["Genre"]
                jeu.systeme_exploitation = entree["Operating System"]
                jeu.date_sortie = entree["Date Released"]
                self.liste_sorties.append(jeu)


    def enregistrer_csv(self):
        liste_entrees_csv = []

        for jeu in self.liste_sorties:
            entree = {"Name": jeu.nom, "Developer": jeu.developpeur, "Producer": jeu.editeur, "Genre": jeu.genre, "Operating System": jeu.systeme_exploitation, "Date Released": jeu.date_sortie}
            liste_entrees_csv.append(entree)
        with open("computer_games.csv", "w", encoding="utf-8", newline="") as csvfile:
            dict_writer = DictWriter(csvfile, fieldnames=liste_entrees_csv[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(liste_entrees_csv)

    def retourner_entree(self, index: int) -> JeuxSortie:
        return self.liste_sorties[index]





