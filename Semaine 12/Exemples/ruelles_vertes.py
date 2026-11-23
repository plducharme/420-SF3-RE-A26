from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QFrame, QVBoxLayout, QTextEdit, QMenu, QToolBar, QFileDialog
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


class RuellesVertes(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Données sur les ruelles vertes de Montréal")
        self.setWindowIcon(QIcon("./images/arbre.png"))

        self.widget_central = QFrame()
        self.setCentralWidget(self.widget_central)
        self.disposition_principale = QVBoxLayout()
        self.widget_central.setLayout(self.disposition_principale)

        self.action_importer_csv = QAction("Importer un csv")
        self.action_importer_csv.triggered.connect(self.importer_csv)
        self.action_importer_csv.setIcon(QIcon("./images/csv.png"))
        self.action_importer_csv.setIconText("Importer à partir d'un csv")

        self.action_quitter = QAction("Quitter")
        self.action_quitter.setShortcut("Ctrl+Q")
        self.action_quitter.triggered.connect(self.close)
        self.action_quitter.setIcon(QIcon("./images/quitter.png"))

        self.action_exporter_excel = QAction("Exporter vers excel")
        self.action_exporter_excel.triggered.connect(self.exporter_excel)
        self.action_exporter_excel.setIcon(QIcon("./images/excel.png"))
        self.action_exporter_excel.setIconText("Exporter en format excel")
        self.action_exporter_excel.setEnabled(False)

        self.barre_menu = self.menuBar()
        self.menu_fichier = QMenu("&Fichier")
        self.menu_import_export = QMenu("Import/Export")

        self.barre_menu.addMenu(self.menu_fichier)
        self.menu_fichier.addMenu(self.menu_import_export)
        self.menu_import_export.addAction(self.action_importer_csv)
        self.menu_import_export.addAction(self.action_exporter_excel)
        self.menu_fichier.addSeparator()
        self.menu_fichier.addAction(self.action_quitter)

        self.barre_outils = QToolBar()
        self.barre_outils.addAction(self.action_importer_csv)
        self.barre_outils.addAction(self.action_exporter_excel)
        self.addToolBar(self.barre_outils)

        self.barre_outils_quitter = QToolBar()
        self.barre_outils_quitter.addAction(self.action_quitter)
        self.addToolBar(self.barre_outils_quitter)

        self.output_df = QTextEdit()
        self.output_df.setReadOnly(True)
        self.disposition_principale.addWidget(self.output_df)

        self.liste_arrondissements = QComboBox()
        self.disposition_principale.addWidget(self.liste_arrondissements)
        self.liste_arrondissements.currentIndexChanged.connect(self.arrondissement_selection)
        self.liste_arrondissements.setEditable(False)

        self.dataframe: pd.DataFrame = None
        self.dataframe_filtre: pd.DataFrame = None

    def importer_csv(self):
        chemin, filtre_selectionne = QFileDialog.getOpenFileName(self, "Importer un CSV", "./", filter="fichier csv ("
                                                                                                       "*.csv)")

        if chemin:
            self.dataframe = pd.read_csv(chemin, sep=",")
            self.action_exporter_excel.setEnabled(True)
            # self.output_df.append(str(self.dataframe.keys().values))
            self.liste_arrondissements.addItem("Tous")
            self.liste_arrondissements.addItems(list(set(self.dataframe["CODE_ARR"].values)))
            output_prop = ""
            for prop in self.dataframe["PROPRIETAIRE_REF"].values:
                output_prop += prop + "\n"
            self.output_df.setText(output_prop)
            self.dataframe_filtre = self.dataframe

    def exporter_excel(self):
        chemin, filtre = QFileDialog.getSaveFileName(self, "Exporter vers excel", "./output", "fichier excel (*.xlsx)")

        if chemin:
            self.dataframe_filtre.to_excel(chemin, index=False)

    def arrondissement_selection(self, index):

        if index == 0:
            props = self.dataframe["PROPRIETAIRE_REF"].values
        else:
            self.dataframe_filtre = self.dataframe[self.dataframe["CODE_ARR"] == self.liste_arrondissements.currentText()]
            props = self.dataframe_filtre["PROPRIETAIRE_REF"].values
        output_props = ""
        for prop in props:
            output_props += prop + "\n"

        self.output_df.setText(output_props)


app = QApplication()
rv = RuellesVertes()
rv.show()
app.exec()
