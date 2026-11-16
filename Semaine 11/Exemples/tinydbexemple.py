from tinydb import TinyDB, Query
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import QRect


class TinyDbExemple(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple TinyDb")
        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        self.textarea = QTextEdit()
        self.textarea.setGeometry(QRect(0, 0, 100, 400))
        self.setCentralWidget(widget_central)
        disposition.addWidget(self.textarea)

        bouton_exec = QPushButton("Executer")
        bouton_exec.clicked.connect(self.executer)
        bouton_reset = QPushButton("Reset")
        bouton_reset.clicked.connect(self.reset)
        disposition.addWidget(bouton_exec)
        disposition.addWidget(bouton_reset)

        self.tinydb_client = TinyDbClient()

    def executer(self):
        id = self.tinydb_client.inserer_chien({"nom": "Frimousse", "race": "Shih Tzu", "age": 3, "couleur": "gris"})
        self.textarea.append("\nId insere: " + str(id))

        ids = self.tinydb_client.inserer_chiens(DataChien.chiens)
        self.textarea.append("\nIds inseres: " + str(ids))

        doc = self.tinydb_client.get_by_id(1)
        self.textarea.append("\nChien id 1: " + str(doc))

        docs = self.tinydb_client.get_all()
        self.textarea.append("\nChiens: " + str(docs))

        self.tinydb_client.print_all()

        docs = self.tinydb_client.find_by_race("Boston Terrier")
        self.textarea.append("\nBoston Terriers: " + str(docs))

        self.tinydb_client.update_qualite({"qualite": "sage"}, 5)

        docs = self.tinydb_client.get_all()
        self.textarea.append("\nChiens: " + str(docs))

        self.tinydb_client.remove_all_b()

        docs = self.tinydb_client.get_all()
        self.textarea.append("\nChiens: " + str(docs))

    def reset(self):
        self.tinydb_client.drop_all()


# https://tinydb.readthedocs.io/en/latest/
class TinyDbClient:
    def __init__(self):
        self.db = TinyDB("chien.json")
        # On va utiliser la table "chien"; Si aucune table n'est spécifiée, une table "_default" est utilisée, il est
        # alors possible d'utiliser directement par exemple db.insert() au lieu de table_chien.insert()
        self.table_chien = self.db.table("chien")

    def inserer_chien(self, document: dict) -> int:
        # insert le document contenu dans la table (collection), le id inséré est retourné
        id = self.table_chien.insert(document)
        return id

    def inserer_chiens(self, documents: list[dict]) -> list[int]:
        # Va retourner tous les ids insérés
        ids = self.table_chien.insert_multiple(documents)
        return ids

    def get_by_id(self, id: int):
        # Il est possible de faire des get, update et remove en utilisant les ids
        doc = self.table_chien.get(doc_id=id)
        return doc

    def get_all(self):
        # Retourne tous les documents de la collection
        return self.table_chien.all()

    def print_all(self):
        # on peut itérer sur la collection directement
        for doc in self.table_chien:
            print(doc)

    def find_by_race(self, race: str):
        # On utilise un objet Query qui spécifie les conditions sur les attributs
        query_chien = Query()
        docs = self.table_chien.search(query_chien.race == race)
        return docs

    def update_qualite(self, doc: dict, age: int):
        # Il est possible de mettre à jour plusieurs documents et aussi d'utiliser des fonctions pour tester
        query_chien = Query()
        is_sage = lambda x: x >= age
        self.table_chien.update(doc, query_chien.age.test(is_sage))

    def remove_all_b(self):
        query_chien = Query()
        # On peut aussi utiliser des expressions régulières ; ici, on supprime tous les chiens avec une couleur
        # commençant par "b"
        self.table_chien.remove(query_chien.couleur.matches("^b\w"))

    def drop_all(self):
        self.db.drop_tables()


class DataChien:
    chiens = [
        {
            "nom": "Lucien",
            "race": "Boston Terrier",
            "age": 2,
            "couleur": "noir"
        },
        {
            "nom": "Elton",
            "race": "Boston Terrier",
            "age": 1,
            "couleur": "noir"
        },
        {
            "nom": "Barney",
            "race": "Bouvier Bernois",
            "age": 5,
            "couleur": "brun"
        },
        {
            "nom": "Merlin",
            "race": "Labradoodle",
            "age": 7,
            "couleur": "blanc"
        }
    ]


app = QApplication()
tiny = TinyDbExemple()
tiny.show()
app.exec()


