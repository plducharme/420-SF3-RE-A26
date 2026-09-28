import csv

class ElementTableauPeriodique:

    def __init__(self, numero_atomique: int, symbole: str, nom: str, annee_decouverte: int, masse_atomique: float):
        self.__numero_atomique = numero_atomique
        self.__symbole = symbole
        self.__nom = nom
        self.__annee_decouverte = annee_decouverte
        self.__masse_atomique = masse_atomique

    @property
    def numero_atomique(self):
        return self.__numero_atomique

    @numero_atomique.setter
    def numero_atomique(self, numero_atomique):
        self.__numero_atomique = numero_atomique

    @property
    def symbole(self):
        return self.__symbole

    @symbole.setter
    def symbole(self, symbole):
        self.__symbole = symbole

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def annee_decouverte(self):
        return self.__annee_decouverte

    @annee_decouverte.setter
    def annee_decouverte(self, annee_decouverte):
        self.__annee_decouverte = annee_decouverte

    @property
    def masse_atomique(self):
        return self.__masse_atomique

    @masse_atomique.setter
    def masse_atomique(self, masse_atomique):
        self.__masse_atomique = masse_atomique

    def __repr__(self):
        return f"{self.nom}:{self.numero_atomique}:{self.annee_decouverte}"

    @staticmethod
    def charger_donnees(chemin_fichier: str):

        with open(chemin_fichier, mode="r", encoding="utf-8-sig") as fichier:
            reader = csv.DictReader(fichier, delimiter=";")

            liste_elements = []
            for ligne in reader:
                masse_atomique_str = ligne["Atomic Mass"].replace("[", "").replace("]", "")
                if masse_atomique_str.find("(") != -1:
                    masse_atomique_str = masse_atomique_str[0:masse_atomique_str.index("(")]
                annee_decouverte = None
                if ligne["Year Discovered"] is not None and len(ligne["Year Discovered"]) > 0:
                    annee_decouverte = int(ligne["Year Discovered"])
                element = ElementTableauPeriodique(int(ligne["Atomic Number"]), ligne["Symbol"], ligne["Name"], annee_decouverte, float(masse_atomique_str))
                liste_elements.append(element)

            return liste_elements



    @staticmethod
    def enregistrer(chemin: str, liste_elements):
        elements_dicts = []
        for e in liste_elements:
            element = {"Atomic Number":e.numero_atomique, "Symbol": e.symbole, "Name": e.nom, "Year Discovered": e.annee_decouverte, "Atomic Mass": e.masse_atomique}
            elements_dicts.append(element)
        with open(chemin, mode="w", encoding="utf-8-sig", newline="") as fichier:
            writer = csv.DictWriter(fichier, fieldnames=["Atomic Number", "Symbol", "Name", "Year Discovered", "Atomic Mass"], delimiter=";")
            writer.writeheader()
            writer.writerows(elements_dicts)



if __name__ == "__main__":
    liste_elem = ElementTableauPeriodique.charger_donnees("periodic-table.csv")
    for e in liste_elem:
        print(e)