

class Avion:

    def __init__(self, modele: str, constructeur: str):
        self.__modele = modele
        self.__constructeur = constructeur
        self.__moteur = None

    @property
    def modele(self) -> str:
        return self.__modele

    @modele.setter
    def modele(self, modele: str):
        self.__modele = modele

    @property
    def constructeur(self) -> str:
        return self.__constructeur

    @constructeur.setter
    def constructeur(self, constructeur: str):
        self.__constructeur = constructeur

    @property
    def moteur(self):
        return self.__moteur

    @moteur.setter
    def moteur(self, moteur: Moteur):
        self.__moteur = moteur

    def __repr__(self):
        return "Modèle: " + self.__modele + "\nConstructeur: " + self.__constructeur + "\nMoteur: " + str(self.__moteur)

    def affichage(self):
        print(f"Modèle: {self.__modele} Constructeur: {self.__constructeur} Moteur: {self.__moteur}")


class Moteur:

    def __init__(self, modele: str, puissance: int):
        self.__modele = modele
        self.__puissance = puissance

    def __str__(self):
        return "[Moteur: modèle: " + self.__modele + " puissance: " + str(self.__puissance) + " lbf]"


boeing_747 = Avion("747", "Boeing")
moteur_747 = Moteur("PW4056", 56000)
boeing_747.moteur = moteur_747
print(boeing_747)
boeing_747.affichage()


