import pymongo.server_api
from PySide6.QtWidgets import QApplication, QTableView, QMenu, QMainWindow, QFrame, QVBoxLayout, QPushButton, \
    QHBoxLayout, QFileDialog, QToolBar
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QAction, QIcon
import csv
import json

from pymongo import MongoClient


class CollectionBA(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Import/Export Collection Beaux-Arts")

        self.widget_central = QFrame()
        self.setCentralWidget(self.widget_central)
        self.disposition_principale = QVBoxLayout()
        self.widget_central.setLayout(self.disposition_principale)

        self.tableau_vue = QTableView()
        self.disposition_principale.addWidget(self.tableau_vue)

        self.barre_menu = self.menuBar()
        self.menu_fichier = QMenu("&Fichier")
        self.barre_menu.addMenu(self.menu_fichier)

        self.action_importer = QAction("Importer d'un csv")
        self.action_importer.triggered.connect(self.importer_fichier_csv)
        self.action_importer.setIcon(QIcon("./images/import_csv.png"))
        self.menu_fichier.addAction(self.action_importer)

        self.action_exporter = QAction("Exporter vers MongoDB")
        self.action_exporter.triggered.connect(self.exporter_data)
        self.action_exporter.setIcon(QIcon("./images/export_db.png"))
        self.menu_fichier.addAction(self.action_exporter)

        self.menu_fichier.addSeparator()

        self.action_quitter = QAction("Quitter")
        self.action_quitter.triggered.connect(self.close)
        self.action_quitter.setShortcut("Ctrl+Q")
        self.menu_fichier.addAction(self.action_quitter)

        self.barre_outils = QToolBar()
        self.barre_outils.addAction(self.action_importer)
        self.barre_outils.addAction(self.action_exporter)
        self.addToolBar(self.barre_outils)

        self.data : ModeleBeauxArts = None

    def importer_fichier_csv(self):
        chemin_fichier, filtre = QFileDialog.getOpenFileName(self, "Ouvrir un CSV", "./", "*.csv")

        if chemin_fichier == "":
            return

        with open(chemin_fichier, mode="r", encoding="utf8") as fichier_csv:
            reader = csv.DictReader(fichier_csv)
            donnees = []
            for ligne in reader:
                donnees.append(ligne)

        self.data = ModeleBeauxArts(donnees)
        self.tableau_vue.setModel(self.data)

    def exporter_data(self):
        with open("atlas.json", mode="r", encoding="utf8") as fichier_config:
            configs = json.load(fichier_config)

        client = MongoClient("mongodb+srv://"+configs['user']+":" + configs['password'] +
                             configs["server"] + "/?retryWrites=true&w=majority")
        bd = client["BeauxArts"]
        collection = bd["Oeuvre"]

        for l in range(self.data.rowCount()):
            oeuvre = {}
            for c in range(self.data.columnCount()):
                index = self.data.index(l, c)
                oeuvre[self.data.entetes[c]] = self.data.data(index, Qt.ItemDataRole.DisplayRole)
            collection.insert_one(oeuvre)


class ModeleBeauxArts(QAbstractTableModel):

    def __init__(self, donnees: list[dict]):
        super().__init__()
        self.donnees = donnees
        self.entetes = ["Numero_accession", "Categorie_objet", "Sous_categorie_objet", "Artiste_artisan", "Titre",
                        "Date_accession"]

    def rowCount(self, /, parent = ...):
        return len(self.donnees)

    def columnCount(self, /, parent = ...):
        return 6

    def data(self, index, /, role = ...):
        return self.donnees[index.row()][self.entetes[index.column()]]

    def headerData(self, section, orientation, role = ...):
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            if 0 <= section < len(self.entetes):
                return self.entetes[section]
            return None
        else:
            return str(section + 1)


app = QApplication()
cba = CollectionBA()
cba.show()
app.exec()

