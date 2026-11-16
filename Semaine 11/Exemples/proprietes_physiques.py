from PySide6.QtWidgets import QApplication, QFrame, QFileDialog, QTableView, QPushButton, QMainWindow, QMenu, \
    QVBoxLayout, QToolBar
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QAction, QIcon
import csv
from pymongo import MongoClient
import json


class ProprietesPhysiquesApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualisateur de propriétés physiques")
        self.setWindowIcon(QIcon("./images/roche.png"))

        self.barre_menu = self.menuBar()
        self.menu_fichier = QMenu("Fichier")
        self.menu_import_export = QMenu("Import/Export")
        self.menu_fichier.addMenu(self.menu_import_export)
        self.barre_menu.addMenu(self.menu_fichier)

        self.action_import_csv = QAction("Importer un csv")
        self.action_import_csv.triggered.connect(self.importer_csv)
        self.action_import_csv.setIcon(QIcon("./images/import_csv.png"))
        self.menu_import_export.addAction(self.action_import_csv)

        self.action_export_mongodb = QAction("Exporter vers MongoDB")
        self.action_export_mongodb.triggered.connect(self.exporter_vers_mongodb)
        self.action_export_mongodb.setIcon(QIcon("./images/export_db.png"))
        self.menu_import_export.addAction(self.action_export_mongodb)

        self.menu_fichier.addSeparator()
        self.action_quitter = QAction("Quitter")
        self.action_quitter.setShortcut("Ctrl+Q")
        self.menu_fichier.addAction(self.action_quitter)

        self.widget_central = QFrame()
        self.setCentralWidget(self.widget_central)
        self.disposition_principale = QVBoxLayout()
        self.widget_central.setLayout(self.disposition_principale)

        self.tableau_vue = QTableView()
        self.tableau_modele: ProprietesPhysiquesModele = None
        self.disposition_principale.addWidget(self.tableau_vue)
        self.donnees = []
        self.entetes = ["NUMR_ECHN_ROCH_GEOLG", "DATE_OBSR", "VAL_DENSI", "VAL_SUSCE_MAGNE", "Coord_X", "Coord_Y"]
        self.entetes_tableau = ["No échantillon", "Date d'observation", "Valeur de densité", "Valeur de susceptibilité "
                                                                                             "magnétique", "Coord x",
                                "Coord y"]
        self.barre_outils = QToolBar()
        self.barre_outils.addAction(self.action_import_csv)
        self.barre_outils.addAction(self.action_export_mongodb)
        self.addToolBar(self.barre_outils)

    def importer_csv(self):
        chemin, filtre = QFileDialog.getOpenFileName(self, "Ouvrir un CSV", "./", "*.csv")

        if chemin == "":
            return

        self.donnees = []
        with open(chemin, mode="r", encoding="utf8") as fichier_csv:
            data_csv = csv.DictReader(fichier_csv, delimiter=",")

            for ligne in data_csv:
                self.donnees.append(ligne)

        self.tableau_modele = ProprietesPhysiquesModele(self.donnees, self.entetes, self.entetes_tableau)
        self.tableau_vue.setModel(self.tableau_modele)

    def exporter_vers_mongodb(self):
        with open("atlas.json", mode="r", encoding="utf8") as fichier_json:
            configs = json.load(fichier_json)

        client = MongoClient("mongodb+srv://" + configs['user'] + ":" + configs['password'] +
                             configs["server"] + "/?retryWrites=true&w=majority")

        bd = client["Roches"]
        collection_proprietes_physique = bd["ProprietesPhysiques"]

        donnees_a_inserer = []
        for document in self.donnees:
            proprietes_dict = {}
            for i in range(6):
                proprietes_dict[self.entetes_tableau[i]] = document[self.entetes[i]]
            # collection_proprietes_physique.insert_one(proprietes_dict)
            donnees_a_inserer.append(proprietes_dict)
        collection_proprietes_physique.insert_many(donnees_a_inserer)


class ProprietesPhysiquesModele(QAbstractTableModel):

    def __init__(self, donnees: list[dict], entetes, entetes_tableau):
        super().__init__()
        self.donnees = donnees
        self.entetes = entetes
        self.entetes_tableau = entetes_tableau

    def data(self, index, /, role=...):
        # Pour éviter que les cases à cocher apparaissent dans les cellules, seulement retourner pour le "DisplayRole"
        if role == Qt.ItemDataRole.DisplayRole:
            return self.donnees[index.row()][self.entetes[index.column()]]
        return None

    def rowCount(self, /, parent=...):
        return len(self.donnees)

    def columnCount(self, /, parent = ...):
        return 6

    def headerData(self, section, orientation, /, role = ...):

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            if 0 <= section < len(self.entetes):
                return self.entetes_tableau[section]
            return None
        else:
            return str(section + 1)


app = QApplication()
pp = ProprietesPhysiquesApp()
pp.show()
app.exec()



