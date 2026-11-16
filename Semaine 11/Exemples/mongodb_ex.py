import pymongo.server_api
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTextEdit, QVBoxLayout
from pymongo import MongoClient
import json


class MongoExemple(QMainWindow):
    def __init__(self):
        super().__init__()
        widget_central = QWidget()
        disposition = QVBoxLayout()
        textedit = QTextEdit()
        bouton = QPushButton("Tout executer")
        bouton.clicked.connect(self.bouton_clicked)
        disposition.addWidget(textedit)
        disposition.addWidget(bouton)
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        self.mongo_client = MongoTestClient(textedit)

    def bouton_clicked(self):
        self.mongo_client.inserer_un()
        self.mongo_client.inserer_plusieurs()
        self.mongo_client.find({"nom": "Code Monkeys"}, "")
        self.mongo_client.find({"annee_debut": {"$lt": 2010}}, "nom")
        self.mongo_client.supprimer_un({"nom": "Code Monkeys"})
        # Si on passe un dictionnaire vide, il n'y a pas de critères, donc tout est supprimé
        self.mongo_client.supprimer_plusieurs({})


class MongoTestClient:
    def __init__(self, textedit: QTextEdit):
        # Charge les configs à partir du atlas.json, voir charger_configs()
        configs = MongoTestClient.charger_configs()
        # Créer la chaîne de connexion
        # Vous pouvez la remplacer par celle provenant de la console Atlas (cluster -> connect -> drivers)
        adresse_connexion = ("mongodb+srv://"+configs['user']+":" + configs['password'] +
                             configs["server"] + "/?retryWrites=true&w=majority")
        # adresse_connexion = "mongodb+srv://dutch80:<db_password>@testcluster.va4xpjo.mongodb.net/?appName=testcluster"
        self.client = MongoClient(adresse_connexion, server_api=pymongo.server_api.ServerApi('1'))
        # Se connecter à la BD
        self.db = self.client['ContenuSurDemande']
        # utiliser une collection
        self.collection = self.db['Series']
        self.textedit = textedit

    def listes_bds(self):
        return self.client.list_databases()

    def inserer_un(self):
        # Creer le dictionnaire equivalent au json
        document = {
            "nom": "The IT crowd",
            "annee_debut": 2006,
            "annee_fin": 2013,
            "comediens": [{"nom": "O'Dowd", "prenom": "Chris"}, {"nom": "Ayoade", "prenom": "Richard"}]
        }
        # L'insertion retourn un objet InsertOneResult contenant l'id généré
        resultat = self.collection.insert_one(document)
        self.append_texte("Id insert_one " + str(resultat.inserted_id))

    def inserer_plusieurs(self):
        # Creer le dictionnaire equivalent au json
        documents = [
            {
                "nom": "Code Monkeys",
                "annee_debut": 2007,
                "annee_fin": 2008,
                "comediens": [{"nom": "Mariska", "prenom": "Matt"}, {"nom": "Snuyder", "prenom": "Dana"}]
            },
            {
                "nom": "Serie Noire",
                "annee_debut": 2014,
                "annee_fin": 2016,
                "comediens": [{"nom": "Letourneau", "prenom": "Francois"}, {"nom": "Cochrane", "prenom": "Edith"}]
            }
        ]
        resultats = self.collection.insert_many(documents)
        self.append_texte("insert_many:" + str(resultats.inserted_ids))

    def find(self, query_object: dict, tri: str):
        documents = self.collection.find(query_object)
        if tri != "":
            # la direction du tri: 1->ascendant, -1->descendant
            documents = documents.sort(tri, 1)
        for doc in documents:
            self.append_texte("Find: " + str(doc))

    def append_texte(self, text: str):
        self.textedit.setText(self.textedit.toPlainText() + "\n" + text)

    def supprimer_un(self, query_object: dict):
        self.collection.delete_one(query_object)
        self.append_texte("Suppression d'un document")

    def supprimer_plusieurs(self, query_object: dict):
        # on peut specifier un filtre, voir supprimer_un. Si on ne met aucun filtre, tous les documents seront supprimes
        resultat = self.collection.delete_many(query_object)
        self.append_texte("Nb suppressions: " + str(resultat.deleted_count))

    @staticmethod
    def charger_configs():
        # Charger les configurations de connexion à la BD
        # Lors de votre inscription à MongoDB Atlas, vous pourrez créer un fichier atlas.json contenant le "user" et
        # le "password":
        # {
        #   "user": "votre_user_atlas",
        #   "password": "votre_password_atlas",
        #   "server": "adresse_du_serveur"
        # }
        with open("./atlas.json") as fichier_json:
            return json.load(fichier_json)


app = QApplication()
me = MongoExemple()
me.show()
app.exec()
