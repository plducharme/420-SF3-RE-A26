import json


class ToDo:

    def __init__(self, id: int, description: str, completee: bool):
        self.__id = id
        self.__description = description
        self.__completee = completee

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valeur: int):
        self.__id = valeur

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, valeur: str):
        self.__description = valeur

    @property
    def completee(self):
        return self.__completee

    @completee.setter
    def completee(self, valeur: bool):
        self.__completee = valeur

    def __repr__(self):
        return f"TODO[id: {self.__id}, description: \"{self.__description}\", complétée: {self.__completee}]"


    @staticmethod
    def charger_donnees(chemin: str):
        with open(chemin, mode="r", encoding="utf8") as fichier:
            donnees = json.load(fichier)
            liste_taches = []
            for tache in donnees["taches"]:
                todo = ToDo(tache["id"], tache["description"], tache["completee"])
                liste_taches.append(todo)
            return liste_taches

    @staticmethod
    def sauvegarder_fichier(chemin: str, liste_todos):
        with open(chemin, mode="w", encoding="utf8") as fichier:
            liste_json = []
            for elem in liste_todos:
                donnee = {"id": elem.id, "description": elem.description, "completee": elem.completee}
                liste_json.append(donnee)
            donnees = {"taches": liste_json}
            json.dump(donnees, fichier)


if __name__ == "__main__":
    donnees = ToDo.charger_donnees()
    print(donnees)

