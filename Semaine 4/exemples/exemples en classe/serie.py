

class Serie:

    def __init__(self, nom: str, annee_sortie: int, nb_saisons: int):
        self.__nom = nom
        self.__annee_sortie = annee_sortie
        self.__nb_saisons = nb_saisons

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def annee_sortie(self):
        return self.__annee_sortie

    @annee_sortie.setter
    def annee_sortie(self, annee_sortie: int):
        self.__annee_sortie = annee_sortie

    @property
    def nb_saisons(self):
        return self.__nb_saisons

    @nb_saisons.setter
    def nb_saisons(self, nb_saisons: int):
        self.__nb_saisons = nb_saisons

    @staticmethod
    def charger_donnees() -> list[Serie]:
        blood_of_zeus = Serie("Blood of Zeus", 2020, 3)
        cyberpunk = Serie("Cyberpunk: Edgerunners", 2022, 2)
        devil_may_cry = Serie("Devil may cry", 2025, 2)
        return [blood_of_zeus, cyberpunk, devil_may_cry]

