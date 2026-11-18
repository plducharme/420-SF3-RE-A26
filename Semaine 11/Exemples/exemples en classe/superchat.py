from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QFrame, QMessageBox, QPushButton, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout
from pymongo import MongoClient
from pymongo.synchronous.cursor import Cursor
from pymongo.synchronous.collection import Collection
from datetime import datetime


class SuperChat(QFrame):

    def __init__(self):
        super().__init__()

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)
        self.setWindowTitle("SuperChat 2026")

        self.disposition_nom = QHBoxLayout()
        self.label_nom = QLabel("Nom:")
        self.input_nom = QLineEdit()
        self.bouton_connect = QPushButton("Connexion")
        self.bouton_connect.clicked.connect(self.bouton_connect_clicked)
        self.disposition_nom.addWidget(self.label_nom)
        self.disposition_nom.addWidget(self.input_nom)
        self.disposition_nom.addWidget(self.bouton_connect)
        self.disposition.addLayout(self.disposition_nom)

        # Log du chat
        self.log_chat = QTextEdit()
        self.disposition.addWidget(self.log_chat)
        self.log_chat.setEnabled(False)

        self.input_message = QLineEdit()
        self.bouton_envoyer = QPushButton("Envoyer")
        self.bouton_envoyer.clicked.connect(self.bouton_envoyer_clicked)
        self.bouton_lol = QPushButton("\U0001F923")
        self.bouton_lol.clicked.connect(self.bouton_lol_clicked)
        self.bouton_zany = QPushButton("\U0001F92A")
        self.bouton_zany.clicked.connect(self.bouton_zany_clicked)

        self.disposition_message = QHBoxLayout()
        self.disposition_message.addWidget(self.input_message)
        self.disposition_message.addWidget(self.bouton_lol)
        self.disposition_message.addWidget(self.bouton_zany)
        self.disposition_message.addWidget(self.bouton_envoyer)
        self.disposition.addLayout(self.disposition_message)

        # variable du modèle
        self.nom = None
        self.client = None
        self.bd = None
        self.collection_bd: Collection | None = None
        self.dernier_message = datetime.now()
        self.timer = None

    def bouton_connect_clicked(self):
        self.nom = self.input_nom.text()
        if self.nom is None or len(self.nom) == 0:
            QMessageBox.information(self, "Erreur nom usager", "Vous devez vous identifier")
            return
        try:
            self.connect_mongo()
        except Exception as e:
            QMessageBox.critical(self, "Erreur MongoDB", "Erreur de connexion")
            return
        liste_message = self.collection_bd.find({})

        for message in liste_message:
            self.log_chat.append(f"{message["nom"]}: {message["message"]}")
        self.dernier_message = datetime.now()
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.recevoir_message)
        self.timer.start()
        self.bouton_connect.setEnabled(False)

    def connect_mongo(self):
        url_connexion = "mongodb+srv://user:password@server/?retryWrites=true&w=majority"
        self.client = MongoClient(url_connexion)
        self.bd = self.client["Messagerie"]
        self.collection_bd = self.bd["messages"]

    def creer_message(self, nom: str, message: str, date: datetime) -> dict:
        return {"nom": nom, "message": message, "date": date}

    def bouton_envoyer_clicked(self):
        msg = self.input_message.text()
        doc = self.creer_message(self.nom, msg, datetime.now())
        self.collection_bd.insert_one(doc)
        self.input_message.clear()

    def recevoir_message(self):
        # filtre = {"date": {"$gt": f"{self.dernier_message}"}}
        messages = self.collection_bd.find()
        self.log_chat.clear()
        for message in messages:
            self.log_chat.append(f"{message["nom"]}: {message["message"]}")
        self.dernier_message = datetime.now()

    def bouton_lol_clicked(self):
        message = self.creer_message(self.nom, "\U0001F923", datetime.now())
        self.collection_bd.insert_one(message)

    def bouton_zany_clicked(self):
        message = self.creer_message(self.nom, "\U0001F92A", datetime.now())
        self.collection_bd.insert_one(message)


app = QApplication()
sc = SuperChat()
sc.show()
app.exec()

